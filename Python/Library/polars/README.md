# Polars

## Cheatsheet Link
https://www.rhosignal.com/posts/polars-pandas-cheatsheet

## Tutorials
### Comparing two dataframes
```py
# Pandas
import pandas as pd
pd.DataFrame().compare

# Polars
import polars as pl

a_df = pl.DataFrame(pd.DataFrame({
    "key": ["A", "B", "C", "D],
    "val1": ["1", "2", pd.NA, ""].
    "val2": ["5", pd.NA, 7, pd.NA]
}))

b_df = pl.DataFrame(pd.DataFrame({
    "key": ["A", "B", "E", "C", "C"],
    "val1": ["1", "2", pd.NA, "", pd.NA],
    "val2": ["5", pd.NA, pd.NA, 7, 7]
}))

a_df = a_df.with_columns(pl.DataFrame({"__index": range(len(a_df))}))
b_df = b_df.with_columns(pl.DataFrame({"__index": range(len(b_df))}))

b_df_columns = [name.lower() for name in b_df.columns]

def strip_or_none(x):
    stripped = str(x).strip()
    return "<NULL>" if stripped == "None" else "<EMPTY>" if stripped == "" else stripped

for col in a_df.columns:
    if col != "__index":
        a_df = _df.with_columns(
            a_df[col].map_elements(strip_or_none, return_dtype=str, skip_nulls=False).alias(col))
        )

for col in b_df.columns:
    if col != "__index":
        b_df = b_df.with_columns(
            b_df[col].map_elements(strip_or_none, return_dtype=str, skip_nulls=False).alias(col))
        )

a_df_cols = list(a_df.columns)
b_df_cols = list(b_df.columns)
a_df_cols.remove("__index")
b_df_cols.remove("__index")
a_df = a_df.sort(a_df_cols)
b_df = b_df.sort(b_df_cols)

merged_df = a_df.join(
    b_df,
    on=a_df.columns,
    how="full",
    suffix="_a"
    join_nulls=True,
    # validate='1:1',
)

pk_not_found_on_both_side = merged_df.filter(
    merged_df["key"].is_null() | merged_df["key_a"].is_null()
)

pk_available_on_both_side = merged_df.filter(
    merged_df["key"].is_not_null() & merged_df["key_a"].is_not_null()
)

col_names = [name for name in pk_available_on_both_side.columns if name != "key" and not name.endswith("_a")]


# Initiate the empty dataframe for comparison results
df_comparison = pl.DataFrame().with_columns(
    [pk_available_on_both_side["key"]]
)

# Compare each column and add comparison results to df_comparison
for col in col_names:
    comparison = pk_available_on_both_side[col].eq_missing(
        pk_available_on_both_side[f"{col}_a"]
    ).alias(f"{col}_comparison")

    # Add the comparison result as a new column
    df_comparison = df_comparison.with_columns([comparison])

# Show the final comparison results
print(df_comparison)
num_rows_with_false = (df_comparison == False).row().any().sum()

```

### Finding the missing primary keys
```py
df1 = pl.DataFrame({
    "key": ["A", "B", "C", "D"],
    "val1": [1, 2, 3, 4],
    "val2": [5, pd.NA, 7, pd.NA]
})

df2 = pl.DataFrame({
    "key": ["A", "B", "D", "E"],
    "val1": [1, 2, 4, 4],
    "val2": [5, pd.NA, 7, pd.NA]
})

df1["key"].is_duplicated(keep=False)

# Count the occurrences of duplicates
df1["keys"].is_duplicated().sum()

# Getting all the duplicates
df1_duplicated_keys = sorted(set(df1.filter(df1["key"].is_duplicated())["key"]))
df2_duplicated_keys = sorted(set(df2.filter(df2["key"].is_duplicated())["key"]))

## Pandas version
df1_duplicated_keys = df1[df1.duplicated(subset=["key"], keep=False)]["key"].unique().tolist()

# Primary keys where both dfs don't have in common
missing_keys = set(df1["key"]) ^ set(df2["key"])
df1_missing_keys = set(df1["key"]) - set(df2["key"])
df2_missing_keys = set(df2["key"]) - set(df1["key"])
missing_keys = df1_missing_keys.union(df2_missing_keys)

```
