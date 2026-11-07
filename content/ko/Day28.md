# streamlit-shap

[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)은 [Streamlit](https://streamlit.io/)에서 [SHAP](https://github.com/slundberg/shap) 그래프를 표시할 수 있는 래퍼를 제공하는 Streamlit 컴포넌트입니다.

이 라이브러리는 [Streamlit 문서](https://docs.streamlit.io/) 웹사이트를 관리하는 Streamlit 직원 [Snehan Kekre](https://github.com/snehankekre)가 개발했습니다.

먼저 Streamlit을 설치한 뒤(물론 필요하겠죠!), pip로 `streamlit-shap` 라이브러리를 설치합니다.

```bash
pip install streamlit
pip install streamlit-shap
```

아직 설치하지 않았다면 다른 필수 라이브러리(예: `matplotlib`, `pandas`, `scikit-learn`, `xgboost`)도 설치해야 합니다.


## 데모 앱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-shap/)

## 코드
`streamlit-shap`은 다음과 같이 사용합니다.

```python
import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

@st.experimental_memo
def load_data():
    return shap.datasets.adult()

@st.experimental_memo
def load_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    d_train = xgboost.DMatrix(X_train, label=y_train)
    d_test = xgboost.DMatrix(X_test, label=y_test)
    params = {
        "eta": 0.01,
        "objective": "binary:logistic",
        "subsample": 0.5,
        "base_score": np.mean(y_train),
        "eval_metric": "logloss",
        "n_jobs": -1,
    }
    model = xgboost.train(params, d_train, 10, evals = [(d_test, "test")], verbose_eval=100, early_stopping_rounds=20)
    return model

st.title("`streamlit-shap` for displaying SHAP plots in a Streamlit app")

with st.expander('About the app'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit component that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/). 
                    The library is developed by our in-house staff [Snehan Kekre](https://github.com/snehankekre) who also maintains the [Streamlit Documentation](https://docs.streamlit.io/) website.
                ''')

st.header('Input data')
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

with st.expander('About the data'):
    st.write('Adult census data is used as the example dataset.')
with st.expander('X'):
    st.dataframe(X)
with st.expander('y'):
    st.dataframe(y)

st.header('SHAP output')
 
# train XGBoost model
model = load_model(X, y)

# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Waterfall plot'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Beeswarm plot'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.

```python
import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd
```

다음으로 Streamlit 앱의 내용이 페이지 전체 너비를 사용할 수 있도록 페이지 레이아웃을 넓게 설정합니다.

```python
st.set_page_config(layout="wide")
```

그런 다음 `shap` 라이브러리에서 데이터셋을 불러옵니다.

```python
@st.experimental_memo
def load_data():
    return shap.datasets.adult()
```

이어서 `X, y` 행렬 쌍을 입력받고, 데이터를 학습용과 테스트용으로 나누고, `DMatrix`를 구성한 뒤 XGBoost 모델을 만드는 `load_model` 함수를 정의합니다.

```python
@st.experimental_memo
def load_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    d_train = xgboost.DMatrix(X_train, label=y_train)
    d_test = xgboost.DMatrix(X_test, label=y_test)
    params = {
        "eta": 0.01,
        "objective": "binary:logistic",
        "subsample": 0.5,
        "base_score": np.mean(y_train),
        "eval_metric": "logloss",
        "n_jobs": -1,
    }
    model = xgboost.train(params, d_train, 10, evals = [(d_test, "test")], verbose_eval=100, early_stopping_rounds=20)
    return model
```

다음으로 Streamlit 앱의 제목을 표시합니다.

```python
st.title("`streamlit-shap` for displaying SHAP plots in a Streamlit app")
```

앱에 대한 자세한 정보를 제공하는 소개용 펼침 상자를 만듭니다.

```python
with st.expander('About the app'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit component that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/). 
                    The library is developed by our in-house staff [Snehan Kekre](https://github.com/snehankekre) who also maintains the [Streamlit Documentation](https://docs.streamlit.io/) website.
                ''')
```

여기서는 입력 데이터의 제목과 함께 `X`, `y` 변수를 보여 주는 펼침 상자를 표시합니다.

```python
st.header('Input data')
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

with st.expander('About the data'):
    st.write('Adult census data is used as the example dataset.')
with st.expander('X'):
    st.dataframe(X)
with st.expander('y'):
    st.dataframe(y)
```

이어서 표시할 SHAP 출력의 제목을 작성합니다.

```python
st.header('SHAP output')
```

앞서 구현한 `load_model` 함수로 XGBoost 모델을 만듭니다.

```python
# train XGBoost model
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

model = load_model(X, y)
```

여기서는 SHAP 값을 계산한 다음, 그 값으로 Waterfall 그래프와 Beeswarm 그래프를 만듭니다.

```python
# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Waterfall plot'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Beeswarm plot'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)
```

마지막으로 `shap.TreeExplainer` 명령의 Tree SHAP 알고리즘으로 트리 앙상블 모델의 출력을 설명하고, `shap.force_plot` 명령으로 시각화합니다.

```python
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## 더 알아보기
- [`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)
- [SHAP](https://github.com/slundberg/shap)
