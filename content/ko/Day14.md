# Streamlit 컴포넌트

컴포넌트는 Streamlit의 기능을 확장하는 서드파티 Python 모듈입니다[[1](https://docs.streamlit.io/library/components)].

## 어떤 Streamlit 컴포넌트가 있나요?

Streamlit 웹사이트에는 수십 개의 Streamlit 컴포넌트가 소개되어 있습니다[[2](https://streamlit.io/components)].

Streamlit Creator인 Fanilo는 위키 게시물에 유용한 Streamlit 컴포넌트 목록을 정리했습니다[[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)]. 이 목록에는 2022년 4월 기준으로 약 85개의 Streamlit 컴포넌트가 나와 있습니다.

## 어떻게 사용하나요?

Streamlit 컴포넌트는 pip로 설치하기만 하면 사용할 수 있습니다.

이번 튜토리얼에서는 `streamlit_pandas_profiling` 컴포넌트를 사용해 보겠습니다[[4](https://github.com/okld/streamlit-pandas-profiling)].

#### 컴포넌트 설치하기

```bash
pip install streamlit_pandas_profiling ydata-profiling
```

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## 코드
컴포넌트를 사용하는 Streamlit 앱을 만드는 방법은 다음과 같습니다.
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df)
st_profile_report(pr)
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오고 앱에서 사용하는 다른 라이브러리도 가져오는 것입니다.
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

이어서 앱의 헤더 텍스트를 만듭니다.
```python
st.header('`streamlit_pandas_profiling`')
```

다음으로 `pandas`의 `read_csv` 명령으로 Penguins 데이터셋을 불러옵니다.
```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

마지막으로 [`ydata-profiling`](https://docs.profiling.ydata.ai/4.12/getting-started/quickstart/)의 `ProfileReport(df)`로 프로파일링 보고서를 생성하고 `st_profile_report`로 표시합니다.
```python
pr = ProfileReport(df)
st_profile_report(pr)
```

## 나만의 컴포넌트 만들기

직접 컴포넌트를 만드는 데 관심이 있다면 다음 자료를 확인해 보세요.
- [컴포넌트 만들기](https://docs.streamlit.io/develop/concepts/custom-components/components-v1/create)
- [컴포넌트 게시하기](https://docs.streamlit.io/library/components/publish)
- [컴포넌트 API](https://docs.streamlit.io/develop/concepts/custom-components/components-v1/intro)
- [Streamlit 컴포넌트 소개 (공식 포럼)](https://discuss.streamlit.io/t/introducing-streamlit-components/6115)

동영상으로 배우는 것을 선호한다면 엔지니어 Tim Conkling이 만든 유익한 튜토리얼도 있습니다.
- [Streamlit 컴포넌트 만드는 방법 | 1부: 설정과 아키텍처](https://youtu.be/BuD3gILJW-Q)
- [Streamlit 컴포넌트 만드는 방법 | 2부: 슬라이더 위젯 만들기](https://youtu.be/QjccJl_7Jco)

## 컴포넌트에 관해 더 읽어 보기
1. [Streamlit 컴포넌트 - API 문서](https://docs.streamlit.io/library/components)
2. [주요 Streamlit 컴포넌트](https://streamlit.io/components)
3. [Streamlit 컴포넌트 - 커뮤니티 트래커](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling` - 소스 코드와 설치 방법](https://github.com/okld/streamlit-pandas-profiling)
