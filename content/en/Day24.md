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
Here's how to use `st.cache_data`:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache_data')

# Using cache
a0 = time()
st.subheader('Using st.cache_data')

@st.cache_data
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache_data')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` as well as other libraries used in the app like so:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

This is followed by creating a title text for the app:
```python
st.title('Streamlit Cache')
```

Next, we'll define 2 custom functions for generating a large DataFrame where the first one makes use of the `st.cache_data` decorator while the second does not:
```python
@st.cache_data
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

Finally, we run the custom function while also timing the run time using the `time()` command.
```python
# Using cache
a0 = time()
st.subheader('Using st.cache_data')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache_data')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

Notice how the first run may provide roughly similar run time. Reload the app and notice how the run time changes when using the `st.cache_data` decorator. Did you observe any speed increase?

## Further reading
- [`st.cache_data` API Documentation](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)
- [Caching overview](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [`st.cache_resource` API Documentation](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)
