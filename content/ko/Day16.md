# Streamlit 앱의 테마 사용자 지정하기

앱과 같은 폴더 안의 `.streamlit` 폴더에 저장된 설정 파일인 `config.toml`의 매개변수를 조정하여 테마를 사용자 지정할 수 있습니다.

## 무엇을 만들까요?

테마를 사용자 지정한 결과를 보여 주는 간단한 앱을 만듭니다. [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) 파일 안의 HTML HEX 색상 코드를 바꾸어 구현합니다.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## 코드
[`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py) 파일의 코드는 다음과 같습니다.
```python
import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

[`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) 파일의 코드는 다음과 같습니다.
```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

이어서 앱의 제목 텍스트를 만듭니다.
```python
st.title('Theming with config.toml')
```

다음으로 `.streamlit/config.toml` 파일의 내용을 보여 줍니다. 먼저 `st.write`로 이에 대한 안내를 표시하고, 이어서 `st.code`로 실제 코드를 표시합니다.
```python
st.write('Contents of the ./streamlit/config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
```

마지막으로 사이드바에 슬라이더 위젯을 만들고 선택한 숫자를 표시합니다.
```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

이제 `.streamlit/config.toml` 파일에 지정하여 앱에 사용한 사용자 지정 색상을 살펴보겠습니다.
- `primaryColor="#F39C12"` - 기본 색상을 주황색으로 설정합니다. 슬라이더 위젯의 주황색을 확인해 보세요.
- `backgroundColor="#2E86C1"` - 배경색을 파란색으로 설정합니다. 메인 패널의 배경색이 파란색인 것을 확인해 보세요.
- `secondaryBackgroundColor="#AED6F1"` - 보조 배경색을 짙은 회색으로 설정합니다. 사이드바의 회색 배경색과 메인 패널에 있는 코드 상자의 배경색을 확인해 보세요.
- `textColor="#FFFFFF"` - 텍스트 색상을 흰색으로 설정합니다.
- `font="monospace"` - 글꼴을 monospace로 설정합니다.

## 더 읽어 보기
- [테마 설정](https://docs.streamlit.io/library/advanced-features/theming)
- [HTML Color Codes](https://htmlcolorcodes.com/)는 원하는 색상을 선택하기에 좋은 도구입니다.
