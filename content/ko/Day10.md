# st.selectbox

`st.selectbox`는 선택 위젯을 표시합니다.

## 무엇을 만들까요?

사용자가 가장 좋아하는 색상을 묻는 간단한 앱을 만듭니다.

앱의 동작 흐름은 다음과 같습니다.
1. 사용자가 색상을 선택합니다.
2. 앱이 선택한 색상을 출력합니다.

## 데모 앱
배포한 Streamlit 앱은 아래 링크의 앱과 비슷한 모습입니다.

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## 코드
앞에서 설명한 앱을 구현하는 코드는 다음과 같습니다.
```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

이어서 앱의 헤더 텍스트를 만듭니다.
```python
st.header('st.selectbox')
```

다음으로 `option`이라는 변수를 만듭니다. `st.selectbox()` 명령의 **선택** 입력 위젯으로 받은 사용자 입력을 이 변수에 저장합니다.

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```
위 코드에서 볼 수 있듯이 `st.selectbox()` 명령은 입력 인수 2개를 받습니다.
1. 선택 위젯 위에 표시할 텍스트, 즉 `'What is your favorite color?'`
2. 선택 가능한 값 `('Blue', 'Red', 'Green')`

마지막으로 선택한 색상을 다음과 같이 출력합니다.
```python
st.write('Your favorite color is ', option)
```

## 다음 단계
다음 챌린지도 같은 실습 폴더의 `app.py`에서 이어갑니다. 앱을 공유하고 싶다면 7일차의 선택 과정인 Streamlit Community Cloud 배포를 살펴보세요.

## 참고 자료
[`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)에 관해 더 알아보세요.
