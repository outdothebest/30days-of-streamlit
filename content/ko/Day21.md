# st.progress

`st.progress`는 반복 작업이 진행됨에 따라 그래픽으로 갱신되는 진행률 표시줄을 보여 줍니다.

## 데모 앱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/)

## 코드
`st.progress`는 다음과 같이 사용합니다.
```python
import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오고 `time` 라이브러리도 가져오는 것입니다.
```python
import streamlit as st
import time
```

다음으로 앱의 제목을 만듭니다.
```python
st.title('st.progress')
```

`st.expander`로 **앱 소개 상자**를 만들고, `st.write`로 설명을 표시합니다.
```python
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
```

마지막으로 진행률 표시줄을 정의하고 시작 값을 `0`으로 초기화합니다. 그런 다음 `for` 반복문으로 `0`부터 `100`에 도달할 때까지 반복합니다. 매번 `time.sleep(0.05)`를 사용해 앱이 `0.05`초 동안 기다리게 한 뒤 `my_bar` 진행률 표시줄의 값을 `1`씩 늘립니다. 이렇게 하면 반복할 때마다 표시줄이 점점 채워집니다.
```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## 더 알아보기
- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)
