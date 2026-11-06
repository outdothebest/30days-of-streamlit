# st.button

`st.button`은 버튼 위젯을 표시합니다.

## 무엇을 만들까요?

버튼을 눌렀는지에 따라 서로 다른 메시지를 출력하는 간단한 앱을 만듭니다.

앱의 동작 흐름은 다음과 같습니다.

1. 기본적으로 앱은 `Goodbye`를 출력합니다.
2. 버튼을 클릭하면 앱은 다른 메시지인 `Why hello there`를 표시합니다.

## 데모 앱

배포한 Streamlit 앱은 아래 링크의 앱과 비슷한 모습입니다.

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## 코드

앞에서 설명한 앱을 구현하는 코드는 다음과 같습니다.

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## 코드 한 줄씩 살펴보기

Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.

```python
import streamlit as st
```

이어서 앱의 헤더 텍스트를 만듭니다.

```python
st.header('st.button')
```

다음으로 `if`와 `else` 조건문을 사용하여 서로 다른 메시지를 출력합니다.

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

위 코드에서 볼 수 있듯이 `st.button()` 명령은 `label` 입력 인수로 `Say hello`를 받습니다. 이 텍스트가 버튼에 표시됩니다.

`st.write` 명령은 버튼을 클릭했는지에 따라 `Why hello there` 또는 `Goodbye`라는 텍스트 메시지를 출력합니다. 다음 코드로 이를 구현합니다.

```python
st.write('Why hello there')
```

그리고

```python
st.write('Goodbye')
```

위에서 설명한 것처럼 서로 다른 메시지를 표시하려면 위의 `st.write` 문을 각각 `if`와 `else` 조건 아래에 배치해야 한다는 점이 중요합니다.

## 다음 단계

로컬에서 Streamlit 앱을 만들었으니 이제 [Streamlit Community Cloud](https://streamlit.io/cloud)에 배포할 차례입니다. 배포 방법은 곧 이어지는 챌린지에서 설명합니다.

이번 주는 챌린지의 첫 주이므로 전체 코드(위 코드 상자 참고)와 해답(데모 앱)을 이 웹페이지에서 바로 제공합니다.

앞으로의 챌린지에서는 먼저 직접 Streamlit 앱을 구현해 보는 것을 권장합니다.

막히더라도 걱정하지 마세요. 언제든 해답을 살짝 살펴볼 수 있습니다.

## 참고 자료

Streamlit API 문서에서 [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button)을 읽어 보세요.
