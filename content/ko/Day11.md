# st.multiselect

`st.multiselect`는 다중 선택 위젯을 표시합니다.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## 코드
`st.multiselect`를 사용하는 방법은 다음과 같습니다.
```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

이어서 앱의 헤더 텍스트를 만듭니다.
```python
st.header('st.multiselect')
```

다음으로 `st.multiselect` 위젯으로 입력을 받습니다. 사용자는 원하는 색상을 하나 이상 선택할 수 있습니다.

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

마지막으로 선택한 색상을 출력합니다.
```python
st.write('You selected:', options)
```

## 더 읽어 보기
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
