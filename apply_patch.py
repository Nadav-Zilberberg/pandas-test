import textwrap

with open('pandas/core/reshape/merge.py', 'r') as f:
    content = f.read()

old_code = """        if validate in ["one_to_one", "1:1"]:
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

new_code = """        if validate in ["one_to_one", "1:1"]:
            if not left_unique or not right_unique:
                from pandas import Index, MultiIndex

                left_dupes = []
                if not left_unique:
                    if self.left_index:
                        idx = self.orig_left.index
                    else:
                        keys = self.left_join_keys
                        names = self.left_keys
                        if len(keys) > 1:
                            idx = MultiIndex.from_arrays(keys, names=names)
                        else:
                            idx = Index(keys[0], name=names[0])
                    left_dupes = idx[idx.duplicated()].unique().tolist()

                right_dupes = []
                if not right_unique:
                    if self.right_index:
                        idx = self.orig_right.index
                    else:
                        keys = self.right_join_keys
                        names = self.right_keys
                        if len(keys) > 1:
                            idx = MultiIndex.from_arrays(keys, names=names)
                        else:
                            idx = Index(keys[0], name=names[0])
                    right_dupes = idx[idx.duplicated()].unique().tolist()

                # Truncate for display
                max_dupes = 10
                if len(left_dupes) > max_dupes:
                    left_dupes = left_dupes[:max_dupes] + ["..."]
                if len(right_dupes) > max_dupes:
                    right_dupes = right_dupes[:max_dupes] + ["..."]

                if not left_unique and not right_unique:
                    msg = (
                        "Merge keys are not unique in either left "
                        "or right dataset; not a one-to-one merge."
                    )
                    if left_dupes:
                        msg += f" Left duplicates: {left_dupes}."
                    if right_dupes:
                        msg += f" Right duplicates: {right_dupes}."
                    raise MergeError(msg)
                elif not left_unique:
                    msg = (
                        "Merge keys are not unique in left dataset; "
                        "not a one-to-one merge."
                    )
                    if left_dupes:
                        msg += f" Duplicates: {left_dupes}."
                    raise MergeError(msg)
                else:  # not right_unique
                    msg = (
                        "Merge keys are not unique in right dataset; "
                        "not a one-to-one merge."
                    )
                    if right_dupes:
                        msg += f" Duplicates: {right_dupes}."
                    raise MergeError(msg)
"""

# The original code has 8 spaces of indentation, but the first line has 4.
# Let's adjust.
old_code = textwrap.dedent(old_code)
new_code = textwrap.dedent(new_code)

# The first line of old_code is the `if` statement, which is at 8 spaces.
# The `if` in `new_code` is also at 8 spaces.
# The issue is that `dedent` removes all common whitespace.
# I need to be more careful.

old_code = """        if validate in ["one_to_one", "1:1"]:
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

new_code = """        if validate in ["one_to_one", "1:1"]:
            if not left_unique or not right_unique:
                from pandas import Index, MultiIndex

                left_dupes = []
                if not left_unique:
                    if self.left_index:
                        idx = self.orig_left.index
                    else:
                        keys = self.left_join_keys
                        names = self.left_keys
                        if len(keys) > 1:
                            idx = MultiIndex.from_arrays(keys, names=names)
                        else:
                            idx = Index(keys[0], name=names[0])
                    left_dupes = idx[idx.duplicated()].unique().tolist()

                right_dupes = []
                if not right_unique:
                    if self.right_index:
                        idx = self.orig_right.index
                    else:
                        keys = self.right_join_keys
                        names = self.right_keys
                        if len(keys) > 1:
                            idx = MultiIndex.from_arrays(keys, names=names)
                        else:
                            idx = Index(keys[0], name=names[0])
                    right_dupes = idx[idx.duplicated()].unique().tolist()

                # Truncate for display
                max_dupes = 10
                if len(left_dupes) > max_dupes:
                    left_dupes = left_dupes[:max_dupes] + ["..."]
                if len(right_dupes) > max_dupes:
                    right_dupes = right_dupes[:max_dupes] + ["..."]

                if not left_unique and not right_unique:
                    msg = (
                        "Merge keys are not unique in either left "
                        "or right dataset; not a one-to-one merge."
                    )
                    if left_dupes:
                        msg += f" Left duplicates: {left_dupes}."
                    if right_dupes:
                        msg += f" Right duplicates: {right_dupes}."
                    raise MergeError(msg)
                elif not left_unique:
                    msg = (
                        "Merge keys are not unique in left dataset; "
                        "not a one-to-one merge."
                    )
                    if left_dupes:
                        msg += f" Duplicates: {left_dupes}."
                    raise MergeError(msg)
                else:  # not right_unique
                    msg = (
                        "Merge keys are not unique in right dataset; "
                        "not a one-to-one merge."
                    )
                    if right_dupes:
                        msg += f" Duplicates: {right_dupes}."
                    raise MergeError(msg)"""

content = content.replace(old_code, new_code)

with open('pandas/core/reshape/merge.py', 'w') as f:
    f.write(content)

print("Patch applied successfully.")
