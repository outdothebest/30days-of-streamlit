# Bored API 앱을 만들며 API 사용법 배우기

Bored API 앱은 심심할 때 할 만한 재미있는 활동을 추천합니다!

기술적인 측면에서는 Streamlit 앱 안에서 API를 사용하는 방법도 보여 줍니다.

## 데모 앱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## 코드
Bored API 앱은 다음과 같이 구현합니다.
```python
import streamlit as st
import requests

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
    
st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오고 `requests` 라이브러리도 가져오는 것입니다.
```python
import streamlit as st
import requests
```

`st.title`로 앱의 제목을 표시합니다.
```python
st.title('🏀 Bored API app')
```

다음으로 `st.selectbox` 명령을 사용해 사용자에게 **활동 유형**을 입력받습니다.
```python
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
```

위에서 선택한 활동 유형을 f-string으로 URL에 추가한 뒤, 그 URL로 요청해 결과를 JSON 데이터로 가져옵니다.
```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

여기서는 `st.expander` 명령으로 앱 소개와 JSON 데이터를 표시합니다.
```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

그런 다음 추천 활동을 다음과 같이 표시합니다.
```python
st.header('Suggested activity')
st.info(suggested_activity['activity'])
```

마지막으로 추천 활동에 대한 추가 정보인 `Number of Participants`(참가자 수), `Type of Activity`(활동 유형), `Price`(비용)도 표시합니다.
```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## 더 알아보기
- [Bored API](http://www.boredapi.com/)
