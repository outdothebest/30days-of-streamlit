# st.secrets

`st.secrets`를 사용하면 API 키, 데이터베이스 비밀번호 또는 기타 인증 정보와 같은 기밀 정보를 저장할 수 있습니다.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## 코드
`st.secrets`를 사용하는 방법은 다음과 같습니다.
```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

이어서 앱의 제목 텍스트를 만듭니다.
```python
st.title('st.secrets')
```

마지막으로 저장된 비밀 정보를 표시합니다.
```python
st.write(st.secrets['message'])
```

아래 스크린샷에서 볼 수 있듯이 비밀 정보는 Streamlit Community Cloud에 저장할 수 있습니다.

로컬에서 작업하는 경우 `.streamlit/secrets.toml`에 저장할 수 있지만, 앱을 배포할 때 이 파일을 GitHub 저장소에 업로드하지 않도록 주의하세요.

## 더 읽어 보기
- [Streamlit 앱에 비밀 정보 추가하기](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [비밀 정보 관리](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
