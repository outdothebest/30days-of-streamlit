# st.cache

`st.cache`를 사용하면 Streamlit 앱의 성능을 최적화할 수 있습니다.

Streamlit은 웹에서 데이터를 불러오거나, 대규모 데이터셋을 다루거나, 비용이 큰 연산을 수행할 때도 앱 성능을 유지할 수 있도록 캐싱 기능을 제공합니다. 이 기능은 `@st.cache` 데코레이터로 사용합니다.

함수에 @st.cache 데코레이터를 붙이면 Streamlit은 그 함수가 호출될 때마다 다음 사항을 확인합니다.

1. 함수를 호출할 때 전달한 입력 매개변수
2. 함수에서 사용하는 외부 변수의 값
3. 함수 본문
4. 캐시된 함수 안에서 사용하는 다른 함수의 본문

Streamlit이 이 네 가지 요소의 값, 조합, 순서를 처음 접했다면 함수를 실행하고 결과를 로컬 캐시에 저장합니다. 이후 캐시된 함수가 다시 호출되었을 때 이 요소들이 하나도 바뀌지 않았다면 함수 실행을 완전히 건너뛰고, 이전에 캐시에 저장한 출력을 반환합니다.

Streamlit은 해싱을 통해 이러한 요소의 변경을 추적합니다. 캐시를 메모리 안의 키-값 저장소라고 생각하면 됩니다. 키는 위의 모든 요소를 해시한 값이고, 값은 참조로 전달되는 실제 출력 객체입니다.

또한 `@st.cache`는 캐시의 동작을 설정할 수 있는 인수를 지원합니다. 자세한 내용은 API 참조 문서에서 확인할 수 있습니다.

## 사용 방법

Streamlit 앱에서 직접 정의한 함수 바로 윗줄에 `st.cache` 데코레이터를 추가하면 됩니다. 아래 예제를 살펴보세요.

## 데모 앱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## 코드
`st.cache`는 다음과 같이 사용합니다.
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오고, 앱에서 사용하는 다른 라이브러리도 가져오는 것입니다.
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

이어서 앱의 제목을 만듭니다.
```python
st.title('Streamlit Cache')
```

다음으로 큰 DataFrame을 생성하는 함수 두 개를 정의합니다. 첫 번째 함수에는 `st.cache` 데코레이터를 사용하고, 두 번째 함수에는 사용하지 않습니다.
```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

마지막으로 직접 정의한 함수를 실행하면서 `time()` 명령으로 실행 시간도 측정합니다.
```python
# Using cache
a0 = time()
st.subheader('Using st.cache')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

처음 실행할 때는 두 실행 시간이 거의 비슷할 수 있습니다. 앱을 새로고침한 뒤 `st.cache` 데코레이터를 사용했을 때 실행 시간이 어떻게 달라지는지 살펴보세요. 속도가 빨라졌나요?

## 더 알아보기
- [`st.cache` API 문서](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [`st.cache`로 성능 최적화하기](https://docs.streamlit.io/library/advanced-features/caching)
- [실험적 캐시 기본 기능](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
