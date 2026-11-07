# Streamlit 컴포넌트

컴포넌트를 사용하면 Streamlit 앱에 HTML 콘텐츠나 서드파티 위젯을 넣어 기능을 확장할 수 있습니다[[1](https://docs.streamlit.io/library/components)].

## 어떤 Streamlit 컴포넌트가 있나요?

Streamlit 웹사이트에는 수십 개의 Streamlit 컴포넌트가 소개되어 있습니다[[2](https://streamlit.io/components)].

Streamlit Creator인 Fanilo는 위키 게시물에 유용한 Streamlit 컴포넌트 목록을 정리했습니다[[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)]. 이 목록에는 2022년 4월 기준으로 약 85개의 Streamlit 컴포넌트가 나와 있습니다.

## 어떻게 사용하나요?

이번 튜토리얼에서는 Streamlit의 HTML 컴포넌트로 데이터 프로파일링 보고서를 표시합니다[[4](https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.html)]. 이전 예제의 프로파일링 래퍼 대신 HTML 보고서를 직접 표시하여 현재 실습 환경에서도 같은 데이터를 살펴볼 수 있습니다.

필요한 라이브러리는 실습 환경에 준비되어 있습니다. 아래 전체 코드를 `app.py`에 저장해 실행하세요.

## 보고서 예시

[프로파일링 보고서 예시 보기 (Titanic 데이터셋)](https://docs.profiling.ydata.ai/latest/examples/titanic/titanic_report.html)

이 정적 HTML 보고서는 Titanic 데이터셋을 사용하며, 아래 학습 예제는 Penguins 데이터셋을 사용합니다.

## 코드
컴포넌트를 사용하는 Streamlit 앱을 만드는 방법은 다음과 같습니다.
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components

st.header('Data profiling report')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df)
components.html(pr.to_html(), height=1000, scrolling=True)
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오고 앱에서 사용하는 다른 라이브러리도 가져오는 것입니다.
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components
```

이어서 앱의 헤더 텍스트를 만듭니다.
```python
st.header('Data profiling report')
```

다음으로 `pandas`의 `read_csv` 명령으로 Penguins 데이터셋을 불러옵니다.
```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

마지막으로 [`ydata-profiling`](https://docs.profiling.ydata.ai/4.12/getting-started/quickstart/)의 `ProfileReport(df)`로 프로파일링 보고서를 생성합니다. `pr.to_html()`로 HTML을 만들고 `components.html`로 앱에 표시합니다. `height`는 표시 영역의 높이를 지정하며 `scrolling=True`는 긴 보고서를 스크롤할 수 있게 합니다.
```python
pr = ProfileReport(df)
components.html(pr.to_html(), height=1000, scrolling=True)
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
4. [`components.html` - HTML 콘텐츠 표시](https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.html)
