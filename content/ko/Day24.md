# st.cache_data

Streamlit은 사용자 상호작용이 있을 때마다 앱을 처음부터 실행합니다. 캐싱을 사용하면 실행 시간이 긴 함수의 결과를 다음 실행에서 재사용할 수 있습니다.

DataFrame, NumPy 배열, API 응답처럼 데이터를 반환하는 함수에는 `@st.cache_data`를 사용합니다. Streamlit은 결과를 저장하고, 같은 입력으로 함수를 다시 호출하면 복사본을 반환합니다. 데이터베이스 연결이나 머신러닝 모델처럼 여러 실행에서 공유할 리소스에는 `@st.cache_resource`를 사용합니다.

## 캐시 사용 방법

데이터를 반환하는 함수 위에 `@st.cache_data`를 붙입니다. 아래 예제의 두 함수는 같은 크기의 DataFrame을 만듭니다. 캐시 함수는 시간이 오래 걸리는 연산을 흉내 내기 위해 1초를 기다리고, 캐시하지 않는 함수도 같은 작업을 합니다.

## 코드

```python
import time

import numpy as np
import pandas as pd
import streamlit as st

st.title("Streamlit 데이터 캐시")


@st.cache_data
def load_data_cached():
    time.sleep(1)  # 시간이 오래 걸리는 연산을 흉내 냅니다.
    return pd.DataFrame(
        np.random.rand(10_000, 5),
        columns=["a", "b", "c", "d", "e"],
    )


def load_data_uncached():
    time.sleep(1)  # 캐시하지 않고 같은 작업을 합니다.
    return pd.DataFrame(
        np.random.rand(10_000, 5),
        columns=["a", "b", "c", "d", "e"],
    )


if st.button("실행 시간 비교"):
    started = time.perf_counter()
    cached_df = load_data_cached()
    cached_seconds = time.perf_counter() - started

    started = time.perf_counter()
    uncached_df = load_data_uncached()
    uncached_seconds = time.perf_counter() - started

    st.write(f"캐시 함수: {cached_seconds:.3f}초")
    st.write(f"캐시하지 않는 함수: {uncached_seconds:.3f}초")
    st.caption("캐시된 미리보기는 그대로이고, 캐시하지 않은 미리보기는 클릭할 때마다 바뀝니다.")
    st.subheader("캐시된 데이터 미리보기")
    st.dataframe(cached_df.head())
    st.subheader("캐시하지 않은 데이터 미리보기")
    st.dataframe(uncached_df.head())
```

## 코드 한 줄씩 살펴보기

가져온 모듈은 Streamlit, NumPy, pandas와 Python 타이머를 제공합니다. `load_data_cached()`와 `load_data_uncached()`는 각각 작은 DataFrame을 만듭니다. 1초 대기는 다운로드나 데이터 변환처럼 시간이 걸리는 작업을 흉내 냅니다. 함수 코드와 입력이 같으면 `@st.cache_data`가 첫 함수의 결과를 재사용할 수 있습니다.

버튼을 누르면 두 함수가 실행됩니다. `time.perf_counter()`로 각 함수 호출 시간을 측정하고, 두 타이머가 멈춘 뒤 결과를 표시하므로 DataFrame 렌더링 시간은 비교에 포함되지 않습니다. `.head()`를 사용해 작은 미리보기만 표시합니다.

## 확인할 점

캐시가 비어 있을 때 **실행 시간 비교**를 한 번 클릭합니다. 두 함수 모두 1초를 기다립니다. 다시 클릭하면 Streamlit이 앱을 실행하지만, 함수 코드와 입력이 바뀌지 않았으므로 `load_data_cached()`는 저장한 결과를 재사용할 수 있습니다. `load_data_uncached()`는 클릭할 때마다 다시 실행됩니다. 캐시된 미리보기 값은 그대로이고, 캐시하지 않은 미리보기 값은 새로 생성됩니다.

타이머는 DataFrame을 화면에 표시하는 시간은 제외하고 함수 호출 시간만 측정합니다. 실제 실행 시간은 컴퓨터에 따라 다릅니다. 캐시가 비어 있을 때는 첫 호출이 결과를 계산하고 저장하므로 눈에 띄는 속도 향상을 기대하기 어렵습니다.

## 더 알아보기

- [캐싱 개요](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [`st.cache_data` API 문서](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)
- [`st.cache_resource` API 문서](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)
