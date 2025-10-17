import pandas as pd

print("Pandas version:", pd.__version__)

print("--- Object dtype ---")
s_obj = pd.Series(["a", "b", None], dtype=object)
print(s_obj.to_json(orient="table", index=False))

print("\n--- StringDtype ---")
s_str = pd.Series(["a", "b", None], dtype="string")
print(s_str.to_json(orient="table", index=False))
