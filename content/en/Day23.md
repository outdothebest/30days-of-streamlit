# st.query_params

`st.query_params` allows the retrieval of query parameters directly from the URL of the user's browser.

## Demo app

This standalone example requires Streamlit 1.30.0 or later. Use a separate Python environment from this repository's tutorial viewer, which uses a bundled Streamlit 1.21.0 wheel.

Save the complete code below as `day23.py`, then run:

```sh
python -m pip install "streamlit>=1.30.0"
python -m streamlit run day23.py
```

1. Open [http://localhost:8501](http://localhost:8501) without query parameters to see instructions for supplying both names.
2. Open [the URL with both names](http://localhost:8501/?firstname=Jack&surname=Beanstalk) to see the greeting.

## Code
Here's how to use `st.query_params`:
```python
import streamlit as st

st.title('st.query_params')

with st.expander('About this app'):
  st.write("`st.query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://localhost:8501/`
such that it becomes 
`http://localhost:8501/?firstname=Jack&surname=Beanstalk`
''')


# 2. Contents of st.query_params
st.header('2. Contents of st.query_params')
st.write(st.query_params)


# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.query_params.get('firstname', '')
surname = st.query_params.get('surname', '')

if firstname and surname:
  st.write(f'Hello **{firstname} {surname}**, how are you?')
else:
  st.info('Add ?firstname=Jack&surname=Beanstalk to the URL to provide both names.')
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

Next, we'll give the app a title:
```python
st.title('st.query_params')
```

Let's also add an About drop-down box:
```python
with st.expander('About this app'):
  st.write("`st.query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")
```

Then, we'll provide instructions to visitors of the app on how they can pass query parameters directly to the URL:
```python
# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://localhost:8501/`
such that it becomes 
`http://localhost:8501/?firstname=Jack&surname=Beanstalk`
''')
```

Subsequently, we'll display the contents of `st.query_params`.
```python
# 2. Contents of st.query_params
st.header('2. Contents of st.query_params')
st.write(st.query_params)
```

Finally, we'll read both names as strings with `.get()`. Missing keys default to empty strings, so missing or empty names display URL instructions instead of raising an exception. Unlike the old experimental API, string values do not need `[0]` indexing. For repeated keys, `.get()` returns the last value:
```python
# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.query_params.get('firstname', '')
surname = st.query_params.get('surname', '')

if firstname and surname:
  st.write(f'Hello **{firstname} {surname}**, how are you?')
else:
  st.info('Add ?firstname=Jack&surname=Beanstalk to the URL to provide both names.')
```

## Further reading
- [`st.query_params`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params)
