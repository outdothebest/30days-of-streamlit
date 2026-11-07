# st.cache_data

`st.cache_data` allows you to optimize the performance of your Streamlit app.

Streamlit provides a caching mechanism that allows your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations. This is done with the `@st.cache_data` decorator.

`@st.cache_data` caches a function's return value based on its input parameters and function code. On a cache miss, Streamlit runs the function and stores the result. A later call with the same inputs and unchanged function code can return the cached result without running the function again.

Streamlit uses hashing to identify the function's inputs and code. Cached data is serialized, and each call returns a copy of the cached value.

Finally, `@st.cache_data` supports arguments to configure the cache's behavior. You can find more information on those in our API reference.

## How to use?

You can simply add the `st.cache_data` decorator on the preceding line of a custom function that you define in your Streamlit app. See the example below.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## Code

Save this example as `day24.py` and run it with `streamlit run day24.py`. It uses `st.cache_data`, which is available in this repository's Streamlit 1.21.0 environment.

Both calls use the same input and calculation and return the same small integer. The one-second `sleep()` simulates slow work, such as fetching data; it is an intentional teaching aid, not a benchmark of real computation.

```python
import streamlit as st
from time import perf_counter, sleep

st.title('st.cache_data')

def slow_calculation(n):
  sleep(1)  # Simulate a slow data fetch or computation.
  return sum(range(n))

@st.cache_data(show_spinner=False)
def cached_calculation(n):
  return slow_calculation(n)

n = st.number_input('Input', min_value=1, max_value=100000, value=10000)
if st.button('Clear cached result'):
  cached_calculation.clear()
st.button('Rerun')

start = perf_counter()
cached_result = cached_calculation(n)
cached_seconds = perf_counter() - start

start = perf_counter()
uncached_result = slow_calculation(n)
uncached_seconds = perf_counter() - start

st.subheader('Using st.cache_data')
st.write('Result:', cached_result)
st.info(f'Elapsed: {cached_seconds:.6f} seconds')

st.subheader('Without caching')
st.write('Result:', uncached_result)
st.info(f'Elapsed: {uncached_seconds:.6f} seconds')
st.write('Results match:', cached_result == uncached_result)
```

## Line-by-line explanation

Import Streamlit and the timing functions, then set the app title. `perf_counter()` measures elapsed time with a high-resolution clock.

```python
import streamlit as st
from time import perf_counter, sleep

st.title('st.cache_data')
```

`slow_calculation(n)` waits one second and sums the integers from `0` to `n - 1`. `cached_calculation(n)` calls that same function, so caching is the only difference between the two paths. The cached return value is a small integer, which keeps serialization and copying costs small. `show_spinner=False` disables the cache spinner so it does not add UI work to the timed call.

```python
def slow_calculation(n):
  sleep(1)  # Simulate a slow data fetch or computation.
  return sum(range(n))

@st.cache_data(show_spinner=False)
def cached_calculation(n):
  return slow_calculation(n)
```

Choose an input and use **Rerun** to run the script again with that input. A Streamlit button triggers a rerun when clicked; it does not need to call a rerun API here. **Clear cached result** removes this function's cached values before the next call on that run.

```python
n = st.number_input('Input', min_value=1, max_value=100000, value=10000)
if st.button('Clear cached result'):
  cached_calculation.clear()
st.button('Rerun')
```

Measure only the two function calls. The cached call includes the cache lookup and, on a miss, calculation and storage. Both paths use the same `n`. Keep all screen output outside these intervals.

```python
start = perf_counter()
cached_result = cached_calculation(n)
cached_seconds = perf_counter() - start

start = perf_counter()
uncached_result = slow_calculation(n)
uncached_seconds = perf_counter() - start
```

After timing, show the results and elapsed seconds. `Results match: True` confirms that both calls returned the same value.

```python
st.subheader('Using st.cache_data')
st.write('Result:', cached_result)
st.info(f'Elapsed: {cached_seconds:.6f} seconds')

st.subheader('Without caching')
st.write('Result:', uncached_result)
st.info(f'Elapsed: {uncached_seconds:.6f} seconds')
st.write('Results match:', cached_result == uncached_result)
```

On a **cold run** (no cached value for this input), both calls perform the one-second work. The cached call also stores its result, so it is not guaranteed to be faster on the first run.

Keep the input unchanged and click **Rerun** several times. These **warm runs** reuse the cached result, while the uncached call still waits one second every time. Click **Clear cached result**, or choose an input that has not been cached, to observe another cold call. Returning to an already cached input can reuse its value. Changing the cached function's code also invalidates its cache. Exact timings depend on your environment; compare repeated warm calls rather than expecting a particular number of seconds.

## Further reading
- [`st.cache_data` API Documentation](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)
- [Caching overview](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [`st.cache_resource` API Documentation](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)
