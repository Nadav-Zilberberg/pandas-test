import pandas as pd

series_object = pd.Series(["a", "b", None], dtype=object)
json_object = series_object.to_json(orient="table", index=False)
print(f"Object dtype: {json_object}")

series_string = pd.Series(["a", "b", None], dtype="string")
json_string = series_string.to_json(orient="table", index=False)
print(f"StringDtype: {json_string}")

