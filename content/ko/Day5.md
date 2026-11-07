# st.write

`st.write`를 사용하면 텍스트와 인수를 Streamlit 앱에 출력할 수 있습니다.

`st.write()` 명령은 텍스트뿐 아니라 다음 항목도 표시할 수 있습니다.

- 문자열 출력: `st.markdown()`처럼 작동합니다.
- Python `dict` 표시
- `pandas` DataFrame을 표로 표시
- `matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh`의 플롯, 그래프, 그림 표시
- 그 밖의 기능([API 문서의 st.write](https://docs.streamlit.io/library/api-reference/write-magic/st.write) 참고)

## 무엇을 만들까요?

`st.write()` 명령으로 텍스트, 숫자, DataFrame, 플롯을 표시하는 다양한 방법을 보여 주는 간단한 앱을 만듭니다.

## 데모 앱

배포한 Streamlit 앱은 아래 링크의 앱과 비슷한 모습입니다.

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## 코드

st.write를 사용하는 방법은 다음과 같습니다.

```python
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## 코드 한 줄씩 살펴보기

Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.

```python
import streamlit as st
```

이어서 앱의 헤더 텍스트를 만듭니다.

```python
st.header('st.write')
```

**예제 1**
가장 기본적인 사용법은 일반 텍스트와 Markdown 형식의 텍스트를 표시하는 것입니다.

```python
st.write('Hello, *World!* :sunglasses:')
```

**예제 2**
앞서 언급했듯이 숫자와 같은 다른 데이터 형식도 표시할 수 있습니다.

```python
st.write(1234)
```

**예제 3**
DataFrame도 다음과 같이 표시할 수 있습니다.

```python
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
```

**예제 4**
여러 인수를 전달할 수 있습니다.

```python
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
```

**예제 5**
마지막으로 다음과 같이 플롯을 변수에 담아 전달하면 플롯도 표시할 수 있습니다.

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## 데모 앱

배포한 Streamlit 앱은 아래 링크의 앱과 비슷한 모습입니다.

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## 다음 단계

다음 챌린지도 같은 실습 폴더의 `app.py`에서 이어갑니다. 앱을 다른 사람과 공유하고 싶다면 7일차의 선택 과정인 Streamlit Community Cloud 배포를 살펴보세요.

이번 주는 챌린지의 첫 주이므로 전체 코드(위 코드 상자 참고)와 해답(데모 앱)을 이 웹페이지에서 바로 제공합니다.

앞으로의 챌린지에서는 먼저 직접 Streamlit 앱을 구현해 보는 것을 권장합니다.

막히더라도 걱정하지 마세요. 언제든 해답을 살짝 살펴볼 수 있습니다.

## 더 읽어 보기

[`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) 외에도 텍스트를 표시하는 다른 방법을 살펴볼 수 있습니다.

- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)
