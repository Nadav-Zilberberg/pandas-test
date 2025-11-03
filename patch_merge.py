import re

def get_new_method_string():
    return r"""    @final
    def _validate_validate_kwd(self, validate: str) -> None:
        # Check uniqueness of each
        if self.left_index:
            left_unique = self.orig_left.index.is_unique
        else:
            left_unique = MultiIndex.from_arrays(self.left_join_keys).is_unique

        if self.right_index:
            right_unique = self.orig_right.index.is_unique
        else:
            right_unique = MultiIndex.from_arrays(self.right_join_keys).is_unique

        def _get_duplicated_keys(keys, side):
            from pandas import DataFrame
            temp_df = DataFrame({"key": keys[0]})
            duplicated_keys = temp_df[temp_df.duplicated()].drop_duplicates()
            return duplicated_keys["key"].to_list()

        # Check data integrity
        if validate in ["one_to_one", "1:1"]:
            if not left_unique and not right_unique:
                left_dupes = _get_duplicated_keys(self.left_join_keys, "left")
                right_dupes = _get_duplicated_keys(self.right_join_keys, "right")
                raise MergeError(
                    "Merge keys are not unique in either left "
                    "or right dataset; not a one-to-one merge. "
                    f"Left duplicates: {left_dupes}. Right duplicates: {right_dupes}."
                )
            if not left_unique:
                dupes = _get_duplicated_keys(self.left_join_keys, "left")
                raise MergeError(
                    "Merge keys are not unique in left dataset; not a one-to-one merge. "
                    f"Duplicates: {dupes}."
                )
            if not right_unique:
                dupes = _get_duplicated_keys(self.right_join_keys, "right")
                raise MergeError(
                    "Merge keys are not unique in right dataset; not a one-to-one merge. "
                    f"Duplicates: {dupes}."
                )

        elif validate in ["one_to_many", "1:m"]:
            if not left_unique:
                dupes = _get_duplicated_keys(self.left_join_keys, "left")
                raise MergeError(
                    "Merge keys are not unique in left dataset; not a one-to-many merge. "
                    f"Duplicates: {dupes}."
                )

        elif validate in ["many_to_one", "m:1"]:
            if not right_unique:
                dupes = _get_duplicated_keys(self.right_join_keys, "right")
                raise MergeError(
                    "Merge keys are not unique in right dataset; "
                    "not a many-to-one merge. "
                    f"Duplicates: {dupes}."
                )

        elif validate in ["many_to_many", "m:m"]:
            pass

        else:
            raise ValueError(
                f'"{validate}" is not a valid argument. '
                "Valid arguments are:\n"
                '- "1:1"\n'
                '- "1:m"\n'
                '- "m:1"\n'
                '- "m:m"\n'
                '- "one_to_one"\n'
                '- "one_to_many"\n'
                '- "many_to_one"\n'
                '- "many_to_many"'
            )
"""

file_path = '/usr/local/lib/python3.11/site-packages/pandas/core/reshape/merge.py'

with open(file_path, 'r') as f:
    content = f.read()

old_method_pattern = re.compile(r"(\s*@final\s*\n\s*def _validate_validate_kwd\(self, validate: str\) -> None:.*?)(?=\n\s*@final|\n\s*def get_join_indexers|\Z)", re.DOTALL)
new_method = get_new_method_string()

new_content, num_replacements = old_method_pattern.subn(new_method, content)

if num_replacements == 0:
    print("Error: Could not find the method to replace.")
else:
    with open(file_path, 'w') as f:
        f.write(new_content)
    print("Successfully patched merge.py.")

