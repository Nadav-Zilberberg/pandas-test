
import pandas as pd

ser = pd.Series(
    [5.4954145e29, -9.791984e-21, 9.3715776e-26, pd.NA, 1.8790257e-28],
    dtype="Float64",
)
ser2 = ser.astype(object)

print("Float64 Series rank:")
print(ser.rank(method="min"))

print("\nObject Series rank:")
print(ser2.rank(method="min"))
