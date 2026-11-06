# st.latex

`st.latex`는 LaTeX 형식의 수식을 표시합니다.

## 무엇을 만들까요?

`st.latex` 명령으로 LaTeX 문법을 사용한 수식을 표시하는 간단한 앱을 만듭니다.

## 데모 앱
[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## 코드
`st.latex`를 사용하는 방법은 다음과 같습니다.
```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

이어서 앱의 헤더 텍스트를 만듭니다.
```python
st.header('st.latex')
```

다음으로 `st.latex`로 수식을 표시합니다.
```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## 참고 자료
- Streamlit API 문서에서 [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)에 관해 더 읽어 보세요.
