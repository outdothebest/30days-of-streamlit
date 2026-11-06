# st.line_chart

`st.line_chart`는 선 그래프를 표시합니다.

이 명령은 `st.altair_chart`를 더 간편한 문법으로 사용할 수 있게 해 줍니다. 가장 큰 차이점은 데이터 자체의 열과 인덱스로 차트의 명세를 결정한다는 점입니다. 따라서 단순히 데이터를 그리려는 여러 상황에서 사용하기 쉽지만, 세부 설정의 자유도는 더 낮습니다.

`st.line_chart`가 데이터 명세를 올바르게 추론하지 못한다면 st.altair_chart로 원하는 차트를 직접 지정해 보세요.

## 무엇을 만들까요?

선 그래프를 표시하는 간단한 앱을 만듭니다.

앱의 동작 흐름은 다음과 같습니다.
1. `NumPy`로 무작위로 생성한 숫자로 `Pandas` DataFrame을 만듭니다.
2. `st.line_chart()` 명령으로 선 그래프를 만들고 표시합니다.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## 코드
[`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart)를 사용하는 방법은 다음과 같습니다.
```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오고 다른 라이브러리도 가져오는 것입니다.
```python
import streamlit as st
import pandas as pd
import numpy as np
```

다음으로 앱의 헤더 텍스트를 만듭니다.
```python
st.header('Line chart')
```

이어서 무작위로 생성한 숫자를 담은 열 3개의 DataFrame을 만듭니다.
```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

마지막으로 `chart_data` 변수에 저장된 DataFrame을 입력 데이터로 전달하여 `st.line_chart()`로 선 그래프를 만듭니다.
```python
st.line_chart(chart_data)
```

## 더 읽어 보기
[`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart)의 기반이 되는 다음 Streamlit 명령에 관해 더 읽어 보세요.
- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
