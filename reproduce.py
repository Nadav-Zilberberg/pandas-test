
import pandas as pd

df = pd.DataFrame({"a": [1, 1, 3], "b": [4, 5, 6]})
try:
    df.merge(df, on="a", validate="one_to_one")
except pd.errors.MergeError as e:
    print(e)

