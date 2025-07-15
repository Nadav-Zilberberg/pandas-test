import pandas as pd

# test_mask_stringdtype
obj = pd.DataFrame(
    {"A": ["foo", "bar", "baz", pd.NA]},
    index=["id1", "id2", "id3", "id4"],
    dtype=pd.StringDtype(),
)
filtered_obj = pd.DataFrame(
    {"A": ["this", "that"]}, index=["id2", "id3"], dtype=pd.StringDtype()
)
expected = pd.DataFrame(
    {"A": [pd.NA, "this", "that", pd.NA]},
    index=["id1", "id2", "id3", "id4"],
    dtype=pd.StringDtype(),
)

filter_ser = pd.Series([False, True, True, False], index=["id1", "id2", "id3", "id4"])
print(obj.mask(filter_ser, filtered_obj))
#         A
# id1  <NA>
# id2  this
# id3  that
# id4  <NA>

filter_ser = pd.Series([True, False, False, True], index=["id1", "id2", "id3", "id4"])
print(obj.mask(filter_ser, filtered_obj))
#         A
# id1  <NA>
# id2  this
# id3  that
# id4  <NA>

filter_ser = pd.Series([False, False, False, False], index=["id1", "id2", "id3", "id4"])
print(obj.mask(filter_ser, filtered_obj))
#         A
# id1  <NA>
# id2  this
# id3  that
# id4  <NA>

filter_ser = pd.Series([True, True, True, True], index=["id1", "id2", "id3", "id4"])
print(obj.mask(filter_ser, filtered_obj))
#         A
# id1  <NA>
# id2  this
# id3  that
# id4  <NA>