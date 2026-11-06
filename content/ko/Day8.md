# st.slider

`st.slider`는 슬라이더 입력 위젯을 표시합니다.

지원하는 데이터 형식은 int, float, date, time, datetime입니다.

## 무엇을 만들까요?

슬라이더 위젯을 조정하여 사용자 입력을 받는 다양한 방법을 보여 주는 간단한 앱을 만듭니다.

앱의 동작 흐름은 다음과 같습니다.
1. 사용자가 슬라이더 위젯을 조정하여 값을 선택합니다.
2. 앱이 선택한 값을 출력합니다.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)

## 코드
st.slider를 사용하는 방법은 다음과 같습니다.

```python
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
from datetime import time, datetime
```

이어서 앱의 헤더 텍스트를 만듭니다.
```python
st.header('st.slider')
```

**예제 1**

슬라이더:

```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

보시는 것처럼 `st.slider()` 명령은 사용자의 나이를 입력받는 데 사용됩니다.

첫 번째 입력 인수는 **슬라이더** 위젯 바로 위에 `'How old are you?'`라는 질문을 표시합니다.

그다음 세 정수 `0, 130, 25`는 각각 최솟값, 최댓값, 기본값을 나타냅니다.

**예제 2**

범위 슬라이더:

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

범위 슬라이더에서는 하한값과 상한값의 쌍을 선택할 수 있습니다.

첫 번째 입력 인수는 **범위 슬라이더** 위젯 바로 위에 `'Select a range of values'`라는 안내 문구를 표시합니다.

그다음 인수 `0.0, 100.0, (25.0, 75.0)`에서 앞의 두 값은 최솟값과 최댓값을 나타내고, 마지막 튜플은 선택된 하한값(25.0)과 상한값(75.0)의 기본값을 나타냅니다.

**예제 3**

시간 범위 슬라이더:

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```

시간 범위 슬라이더에서는 날짜 및 시간의 하한값과 상한값 쌍을 선택할 수 있습니다.

첫 번째 입력 인수는 **시간 범위 슬라이더** 위젯 바로 위에 `'Schedule your appointment:'`라는 안내 문구를 표시합니다.

날짜 및 시간의 하한값과 상한값의 기본값은 각각 11:30과 12:45로 설정되어 있습니다.

**예제 4**

날짜 및 시간 슬라이더:

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

날짜 및 시간 슬라이더에서는 날짜와 시간을 선택할 수 있습니다.

첫 번째 입력 인수는 **날짜 및 시간** 슬라이더 위젯 바로 위에 `'When do you start?'`라는 질문을 표시합니다.

날짜 및 시간의 기본값은 `value` 옵션으로 2020년 1월 1일 9시 30분으로 설정했습니다.

## 더 읽어 보기
다음 관련 위젯도 살펴볼 수 있습니다.
- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)
