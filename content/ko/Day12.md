# st.checkbox

`st.checkbox`는 체크박스 위젯을 표시합니다.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## 코드
`st.checkbox`를 사용하는 방법은 다음과 같습니다.
```python
import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

이어서 앱의 헤더 텍스트를 만듭니다.
```python
st.header('st.checkbox')
```

다음으로 `st.write`로 질문을 표시합니다.
```python
st.write ('What would you like to order?')
```

그런 다음 선택할 수 있는 메뉴 항목을 제공합니다.
```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

마지막으로 어떤 체크박스를 선택했는지에 따라 각기 다른 텍스트를 출력합니다.
```python
if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```  

## 더 읽어 보기
- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
