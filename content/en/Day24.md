# st.cache_data

Streamlit runs your app from top to bottom after each interaction. Caching lets the app reuse results from functions that take time to run.

Use `@st.cache_data` for functions that return data, such as a pandas DataFrame, NumPy array, or API response. Streamlit saves the result and returns a copy on later calls with the same inputs. Use `@st.cache_resource` for shared resources such as database connections or machine-learning models.

## How to use caching

Add `@st.cache_data` above a function that returns data. In the example below, both functions build the same size DataFrame. The cached function waits one second to represent a slow computation; the uncached function does the same work without caching.

## Code

```python
import time

import numpy as np
import pandas as pd
import streamlit as st

st.title("Streamlit data cache")


@st.cache_data
def load_data_cached():
    time.sleep(1)  # Imitate a slow computation.
    return pd.DataFrame(
        np.random.rand(10_000, 5),
        columns=["a", "b", "c", "d", "e"],
    )


def load_data_uncached():
    time.sleep(1)  # Do the same work without caching.
    return pd.DataFrame(
        np.random.rand(10_000, 5),
        columns=["a", "b", "c", "d", "e"],
    )


if st.button("Compare run times"):
    started = time.perf_counter()
    cached_df = load_data_cached()
    cached_seconds = time.perf_counter() - started

    started = time.perf_counter()
    uncached_df = load_data_uncached()
    uncached_seconds = time.perf_counter() - started

    st.write(f"Cached function: {cached_seconds:.3f} seconds")
    st.write(f"Uncached function: {uncached_seconds:.3f} seconds")
    st.caption("The cached preview stays the same; the uncached preview changes after each click.")
    st.subheader("Cached data preview")
    st.dataframe(cached_df.head())
    st.subheader("Uncached data preview")
    st.dataframe(uncached_df.head())
```

## Line-by-line explanation

The imports provide Streamlit, NumPy, pandas, and Python's timer. `load_data_cached()` and `load_data_uncached()` each generate a small DataFrame. The one-second `sleep` stands in for a slow operation, such as downloading or transforming data. `@st.cache_data` lets Streamlit reuse the first function's result when its code and inputs stay the same.

The button runs both functions when clicked. `time.perf_counter()` measures each function call, and the results are displayed after both timers stop so DataFrame rendering does not affect the comparison. The `.head()` calls keep the previews small.

## What to observe

With an empty cache, click **Compare run times** once. Both functions do the one-second wait. Click it again: Streamlit re-runs the app, but `load_data_cached()` can reuse its result because its code and inputs have not changed. `load_data_uncached()` runs again each time. The cached preview stays the same, while the uncached preview contains newly generated values.

The timer measures only each function call; it does not include displaying the DataFrames. Actual times vary by machine, and the first cached call may not look faster because it must compute and store the result.

## Further reading

- [Caching overview](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [`st.cache_data` API reference](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)
- [`st.cache_resource` API reference](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)
