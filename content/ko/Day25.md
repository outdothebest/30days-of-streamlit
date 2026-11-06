# st.session_state

브라우저 탭에서 Streamlit 앱에 접속하는 것을 세션이라고 합니다. Streamlit 서버에 연결하는 브라우저 탭마다 새로운 세션이 만들어집니다. Streamlit은 사용자가 앱을 조작할 때마다 스크립트를 처음부터 끝까지 다시 실행합니다. 매번 아무것도 없는 상태에서 시작하므로 실행 간에 변수가 공유되지 않습니다.

세션 상태(Session State)는 각 사용자 세션에서 앱을 다시 실행해도 변수를 공유할 수 있게 해 주는 방법입니다. Streamlit은 상태를 저장하고 유지하는 기능에 더해 콜백(Callback)으로 상태를 조작하는 기능도 제공합니다.

이 튜토리얼에서는 무게 변환 앱을 만들면서 세션 상태와 콜백을 사용하는 방법을 살펴봅니다.

`st.session_state`를 사용하면 Streamlit 앱에서 세션 상태를 구현할 수 있습니다.

## 데모 앱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## 코드
`st.session_state`는 다음과 같이 사용합니다.
```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

먼저 앱의 제목을 만듭니다.
```python
st.title('st.session_state')
```

다음으로 무게를 lbs에서 kg으로, 그리고 kg에서 lbs로 변환하는 함수를 정의합니다.
```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

여기서는 `st.number_input`으로 무게의 숫자 값을 입력받습니다.
```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```
`st.number_input` 명령으로 만든 숫자 입력 상자에 값을 입력하면 위에서 정의한 두 함수가 호출됩니다. `on_change` 옵션에 `lbs_to_kg`와 `kg_to_lbs` 함수가 지정되어 있다는 점을 살펴보세요.

즉, `st.number_input` 상자에 숫자를 입력하면 이 함수들이 숫자를 변환합니다.

마지막으로 세션 상태의 `st.session_state.kg`와 `st.session_state.lbs`에 저장된 `kg`, `lbs` 단위의 무게 값을 `st.write`로 출력합니다.
```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## 더 알아보기
- [세션 상태](https://docs.streamlit.io/library/api-reference/session-state)
- [앱에 상태 유지 기능 추가하기](https://docs.streamlit.io/library/advanced-features/session-state)
