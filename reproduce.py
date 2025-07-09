
import pandas as pd
import numpy as np
import pyarrow

print(pd.__version__)
print(np.__version__)
print(pyarrow.__version__)

df = pd.DataFrame(data={"A": [np.nan, 1]}, dtype="double[pyarrow]")

print(df.aggregate(lambda x: x.mean()).dtypes)