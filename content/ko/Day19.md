# Streamlit 앱의 레이아웃 구성하기

이번 튜토리얼에서는 다음 명령으로 Streamlit 앱의 레이아웃을 구성합니다.
- `st.set_page_config(layout="wide")` - 앱의 콘텐츠를 넓은 화면 모드로 표시합니다. 기본 설정에서는 콘텐츠가 고정 너비의 상자 안에 표시됩니다.
- `st.sidebar` - 위젯이나 텍스트, 이미지를 사이드바에 배치합니다.
- `st.expander` - 텍스트나 이미지를 접고 펼칠 수 있는 컨테이너 상자 안에 배치합니다.
- `st.columns` - 콘텐츠를 배치할 수 있는 표 형태의 공간(열)을 만듭니다.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## 코드
Streamlit 앱의 레이아웃을 사용자 지정하는 방법은 다음과 같습니다.
```python
import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

먼저 페이지 레이아웃을 `wide` 모드로 표시하도록 정의합니다. 이 모드에서는 페이지 콘텐츠를 브라우저 너비까지 확장할 수 있습니다.
```python
st.set_page_config(layout="wide")
```

다음으로 Streamlit 앱에 제목을 붙입니다.
```python
st.title('How to layout your Streamlit app')
```

앱 제목 아래에는 `About this app`이라는 제목의 펼칠 수 있는 상자를 배치합니다. 상자를 펼치면 안에 있는 추가 설명을 볼 수 있습니다.
```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

사용자 입력을 받는 입력 위젯은 사이드바에 배치합니다. 이를 위해 Streamlit의 `text_input`과 `selectbox` 명령 앞에 `st.sidebar`를 붙입니다. 사용자가 입력하거나 선택한 값은 `user_name`, `user_emoji`, `user_food` 변수에 할당되어 저장됩니다.
```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

마지막으로 `st.columns` 명령으로 `col1`, `col2`, `col3`에 해당하는 열 3개를 만듭니다. 그런 다음 `with` 문으로 시작하는 개별 코드 블록을 만들어 각 열에 콘텐츠를 배치합니다. 그 아래에 조건문을 작성하여 사용자가 사이드바에서 입력 데이터를 제공했는지에 따라 두 가지 텍스트 중 하나를 표시합니다. 기본적으로 페이지에는 `else` 문 아래의 텍스트가 표시됩니다. 사용자가 값을 입력하면 앱에 제공한 해당 정보가 `Output` 헤더 아래에 표시됩니다.
```python
st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```
텍스트와 사용자가 입력한 값을 결합하기 위해 `f` 문자열을 사용했다는 점도 알아 두세요.

## 더 읽어 보기
- [레이아웃과 컨테이너](https://docs.streamlit.io/library/api-reference/layout)
