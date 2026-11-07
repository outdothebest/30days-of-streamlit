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

아래 예제를 실습 폴더의 `app.py`에 저장하세요. 제공된 환경에서 `st.cache_data`의 동작을 확인할 수 있습니다.

두 호출은 같은 입력으로 같은 계산을 수행하며, 같은 작은 정수를 반환합니다. 1초 동안 대기하는 `sleep()`은 데이터 조회처럼 오래 걸리는 작업을 흉내 내기 위한 학습용 장치입니다. 실제 연산 성능을 측정하는 벤치마크는 아닙니다.

```python
import streamlit as st
from time import perf_counter, sleep

st.title('st.cache_data')

def slow_calculation(n):
  sleep(1)  # Simulate a slow data fetch or computation.
  return sum(range(n))

@st.cache_data(show_spinner=False)
def cached_calculation(n):
  return slow_calculation(n)

n = st.number_input('Input', min_value=1, max_value=100000, value=10000)
if st.button('Clear cached result'):
  cached_calculation.clear()
st.button('Rerun')

start = perf_counter()
cached_result = cached_calculation(n)
cached_seconds = perf_counter() - start

start = perf_counter()
uncached_result = slow_calculation(n)
uncached_seconds = perf_counter() - start

st.subheader('Using st.cache_data')
st.write('Result:', cached_result)
st.info(f'Elapsed: {cached_seconds:.6f} seconds')

st.subheader('Without caching')
st.write('Result:', uncached_result)
st.info(f'Elapsed: {uncached_seconds:.6f} seconds')
st.write('Results match:', cached_result == uncached_result)
```

## 코드 한 줄씩 살펴보기

Streamlit과 시간 측정에 필요한 함수를 가져오고 앱 제목을 설정합니다. `perf_counter()`는 고해상도 시계로 경과 시간을 측정합니다.

```python
import streamlit as st
from time import perf_counter, sleep

st.title('st.cache_data')
```

`slow_calculation(n)`은 1초 동안 기다린 뒤 `0`부터 `n - 1`까지의 정수를 더합니다. `cached_calculation(n)`도 같은 함수를 호출하므로 두 경로의 차이는 캐시 사용 여부뿐입니다. 반환값이 작은 정수이므로 직렬화와 복사 비용도 작습니다. `show_spinner=False`는 캐시 스피너를 끄는 설정으로, 측정하는 호출에 스피너 표시 작업이 포함되지 않게 합니다.

```python
def slow_calculation(n):
  sleep(1)  # Simulate a slow data fetch or computation.
  return sum(range(n))

@st.cache_data(show_spinner=False)
def cached_calculation(n):
  return slow_calculation(n)
```

입력을 정한 뒤 **Rerun** 버튼을 누르면 같은 입력으로 스크립트를 다시 실행할 수 있습니다. Streamlit 버튼은 클릭할 때 재실행을 일으키므로 여기서 재실행 API를 따로 호출할 필요는 없습니다. **Clear cached result** 버튼을 누르면 이번 실행에서 함수를 호출하기 전에 이 함수에 저장된 캐시를 비웁니다.

```python
n = st.number_input('Input', min_value=1, max_value=100000, value=10000)
if st.button('Clear cached result'):
  cached_calculation.clear()
st.button('Rerun')
```

두 함수 호출에 걸린 시간만 측정합니다. 캐시를 사용하는 호출에는 캐시 조회가 포함되며, 캐시가 없으면 계산과 저장도 포함됩니다. 두 경로 모두 같은 `n`을 사용합니다. 화면 출력은 이 측정 구간 밖에 둡니다.

```python
start = perf_counter()
cached_result = cached_calculation(n)
cached_seconds = perf_counter() - start

start = perf_counter()
uncached_result = slow_calculation(n)
uncached_seconds = perf_counter() - start
```

시간 측정을 마친 뒤 결과와 경과 시간을 초 단위로 표시합니다. `Results match: True`이면 두 호출의 반환값이 같다는 뜻입니다.

```python
st.subheader('Using st.cache_data')
st.write('Result:', cached_result)
st.info(f'Elapsed: {cached_seconds:.6f} seconds')

st.subheader('Without caching')
st.write('Result:', uncached_result)
st.info(f'Elapsed: {uncached_seconds:.6f} seconds')
st.write('Results match:', cached_result == uncached_result)
```

해당 입력의 캐시가 없는 **최초 실행(cold run)**에서는 두 호출 모두 1초가 걸리는 작업을 수행합니다. 캐시를 사용하는 호출은 결과도 저장해야 하므로 첫 실행부터 더 빠르다고 보장할 수는 없습니다.

입력을 바꾸지 않고 **Rerun** 버튼을 여러 번 눌러 보세요. 이후 **캐시 적중 실행(warm run)**에서는 저장된 값을 재사용하지만, 캐시를 사용하지 않는 호출은 매번 1초 동안 기다립니다. **Clear cached result**를 누르거나 아직 캐시되지 않은 입력을 선택하면 다시 캐시가 없는 상태의 호출을 확인할 수 있습니다. 이미 캐시된 입력으로 돌아가면 저장된 값을 재사용할 수 있습니다. 캐시된 함수의 코드를 바꿔도 캐시가 무효화됩니다. 정확한 시간은 실행 환경에 따라 달라지므로 특정 시간에 맞추기보다 여러 번 반복한 캐시 적중 실행을 비교해 보세요.

## 더 알아보기
- [`st.cache_data` API 문서](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)
- [캐싱 개요](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [`st.cache_resource` API 문서](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)
