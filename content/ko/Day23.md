# st.query_params

`st.query_params`를 사용하면 사용자 브라우저의 URL에서 쿼리 매개변수를 직접 가져올 수 있습니다.

## 데모 앱

이 독립 실행 예제에는 Streamlit 1.30.0 이상이 필요합니다. 이 저장소의 튜토리얼 뷰어는 번들 Streamlit 1.21.0을 사용하므로 별도의 Python 환경에서 실행하세요.

아래 전체 코드를 `day23.py`로 저장한 뒤 실행합니다.

```sh
python -m pip install "streamlit>=1.30.0"
python -m streamlit run day23.py
```

1. 쿼리 매개변수 없이 [http://localhost:8501](http://localhost:8501)에 접속하면 두 이름을 입력하는 방법을 안내합니다.
2. [두 이름을 포함한 URL](http://localhost:8501/?firstname=Jack&surname=Beanstalk)에 접속하면 인사말을 표시합니다.

## 코드
`st.query_params`는 다음과 같이 사용합니다.
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

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

다음으로 앱에 제목을 붙입니다.
```python
st.title('st.query_params')
```

앱을 소개하는 펼침 상자도 추가합니다.
```python
with st.expander('About this app'):
  st.write("`st.query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")
```

그런 다음 앱 방문자가 URL에 쿼리 매개변수를 직접 전달하는 방법을 안내합니다.
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

이어서 `st.query_params`의 내용을 표시합니다.
```python
# 2. Contents of st.query_params
st.header('2. Contents of st.query_params')
st.write(st.query_params)
```

마지막으로 `.get()`으로 두 이름을 문자열로 읽습니다. 키가 없으면 빈 문자열을 사용하므로, 이름이 누락되거나 비어 있을 때 예외 대신 URL 입력 방법을 안내합니다. 기존 experimental API와 달리 문자열 값에 `[0]` 인덱싱을 하지 않습니다. 같은 키가 반복되면 `.get()`은 마지막 값을 반환합니다.
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

## 더 알아보기
- [`st.query_params`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params)
