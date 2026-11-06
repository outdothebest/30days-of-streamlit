# st.file_uploader

`st.file_uploader`는 파일 업로드 위젯을 표시합니다[[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

기본적으로 업로드할 수 있는 파일 크기는 200MB로 제한됩니다. server.maxUploadSize 설정 옵션으로 이를 변경할 수 있습니다. 설정 옵션을 지정하는 방법은 [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)]를 참고하세요.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## 코드
`st.file_uploader`를 사용하는 방법은 다음과 같습니다.
```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오고 필요한 다른 라이브러리도 가져오는 것입니다.
```python
import streamlit as st
import pandas as pd
```

이어서 앱의 제목 텍스트를 만듭니다.
```python
st.title('st.file_uploader')
```

다음으로 `st.file_uploader`로 파일 업로드 위젯을 표시하여 사용자가 파일을 입력할 수 있도록 합니다.
```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

마지막으로 조건문을 정의합니다. 처음에는 사용자에게 파일 업로드를 안내하는 환영 메시지를 표시합니다(`else` 조건으로 구현). 파일을 업로드하면 `if` 문이 실행되어 `pandas` 라이브러리로 CSV 파일을 읽고 `st.write` 명령으로 표시합니다.
```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## 더 읽어 보기
1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [설정 옵션 지정하기](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
