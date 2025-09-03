
import pandas as pd

ser = pd.Series(
    [5.4954145e29, -9.791984e-21, 9.3715776e-26, pd.NA, 1.8790257e-28],
    dtype="Float64",
)
ser2 = ser.astype(object)

print("Original Series with Float64 dtype:")
print(ser)
print("\nRank of Original Series:")
print(ser.rank(method="min"))

print("\nSeries with object dtype:")
print(ser2)
print("\nRank of Series with object dtype:")
print(ser2.rank(method="min"))
