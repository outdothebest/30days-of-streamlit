# st.cache_data

`st.cache_data`를 사용하면 Streamlit 앱의 성능을 최적화할 수 있습니다.

Streamlit은 웹에서 데이터를 불러오거나, 대규모 데이터셋을 다루거나, 비용이 큰 연산을 수행할 때도 앱 성능을 유지할 수 있도록 캐싱 기능을 제공합니다. 이 기능은 `@st.cache_data` 데코레이터로 사용합니다.

`@st.cache_data`는 함수의 입력 매개변수와 함수 코드를 기준으로 반환값을 캐싱합니다. 캐시가 없으면 함수를 실행하고 결과를 저장합니다. 이후 입력과 함수 코드가 같으면 함수를 다시 실행하지 않고 저장된 결과를 반환할 수 있습니다.

Streamlit은 해싱으로 함수의 입력과 코드를 식별합니다. 캐시된 데이터는 직렬화되며, 호출할 때마다 저장된 값의 복사본을 반환합니다.

또한 `@st.cache_data`는 캐시의 동작을 설정할 수 있는 인수를 지원합니다. 자세한 내용은 API 참조 문서에서 확인할 수 있습니다.

## 사용 방법

Streamlit 앱에서 직접 정의한 함수 바로 윗줄에 `st.cache_data` 데코레이터를 추가하면 됩니다. 아래 예제를 살펴보세요.

## 데모 앱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## 코드
`st.cache_data`는 다음과 같이 사용합니다.
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache_data')

# Using cache
a0 = time()
st.subheader('Using st.cache_data')

@st.cache_data
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
st.subheader('Not using st.cache_data')

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

다음으로 큰 DataFrame을 생성하는 함수 두 개를 정의합니다. 첫 번째 함수에는 `st.cache_data` 데코레이터를 사용하고, 두 번째 함수에는 사용하지 않습니다.
```python
@st.cache_data
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
st.subheader('Using st.cache_data')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache_data')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

처음 실행할 때는 두 실행 시간이 거의 비슷할 수 있습니다. 앱을 새로고침한 뒤 `st.cache_data` 데코레이터를 사용했을 때 실행 시간이 어떻게 달라지는지 살펴보세요. 속도가 빨라졌나요?

## 더 알아보기
- [`st.cache_data` API 문서](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)
- [캐싱 개요](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [`st.cache_resource` API 문서](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)
