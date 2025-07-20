import pandas as pd
df = pd.DataFrame({'a': [3,6,1,1,None,6]}, dtype='Int64[pyarrow]')
df['a_mask'] = df['a'].isna()
print(df.groupby('a_mask').rank(method='min'))

