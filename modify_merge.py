import re

with open("pandas/core/reshape/merge.py", "r") as f:
    content = f.read()

# This is the original block
original_block = r"""        if validate in ["one_to_one", "1:1"]:
            if not left_unique and not right_unique:
                raise MergeError(
                    "Merge keys are not unique in either left "
                    "or right dataset; not a one-to-one merge"
                )
            if not left_unique:
                raise MergeError(
                    "Merge keys are not unique in left dataset; not a one-to-one merge"
                )
            if not right_unique:
                raise MergeError(
                    "Merge keys are not unique in right dataset; not a one-to-one merge"
                )"""

# This is the new block
new_block = r"""        if validate in ["one_to_one", "1:1"]:
            if not left_unique or not right_unique:
                from pandas import Index, MultiIndex

                msg = "Merge keys are not unique"
                if not left_unique and not right_unique:
                    msg += " in either left or right dataset"
                elif not left_unique:
                    msg += " in left dataset"
                else:
                    msg += " in right dataset"
                msg += "; not a one-to-one merge."

                if not left_unique:
                    if len(self.left_join_keys) == 1:
                        dupes = Index(self.left_join_keys[0]).get_duplicates()
                    else:
                        dupes = MultiIndex.from_arrays(
                            self.left_join_keys
                        ).get_duplicates()
                    msg += f" The duplicate keys in the left dataset are: {dupes.tolist()}"
                if not right_unique:
                    if len(self.right_join_keys) == 1:
                        dupes = Index(self.right_join_keys[0]).get_duplicates()
                    else:
                        dupes = MultiIndex.from_arrays(
                            self.right_join_keys
                        ).get_duplicates()
                    msg += f" The duplicate keys in the right dataset are: {dupes.tolist()}"
                raise MergeError(msg)"""

content = content.replace(original_block, new_block)

with open("pandas/core/reshape/merge.py", "w") as f:
    f.write(content)
