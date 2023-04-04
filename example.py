import polars as pl
from my_polars_functions import hamming_distance, modify_py_dataframe

a = pl.Series("a", ["foo", "bar"])
b = pl.Series("b", ["fooy", "ham"])

dist = hamming_distance(a, b)
expected = pl.Series("", [None, 2], dtype=pl.UInt32)

# run on 2 Series
print("hamming distance: ", hamming_distance(a, b))
assert dist.series_equal(expected, null_equal=True)

# or use in polars expressions
print(
    pl.DataFrame([a, b]).select(
        pl.map(["a", "b"], lambda series: hamming_distance(series[0], series[1]))
    )
)

df = pl.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]})

# print(df)

print(modify_py_dataframe(df))

# print(df.to_dict())
