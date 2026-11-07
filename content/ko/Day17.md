# st.secrets

`st.secrets`를 사용하면 API 키, 데이터베이스 비밀번호 또는 기타 인증 정보와 같은 기밀 정보를 저장할 수 있습니다.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## 실습 준비

실습 폴더의 `.streamlit/secrets.toml.example`을 복사하여 같은 폴더에 `secrets.toml`이라는 이름으로 저장합니다. 내용은 다음과 같습니다. `message`는 별도의 섹션 없이 최상위 키로 작성합니다.

```toml
message = "Hello, Streamlit!"
```

제공된 `.gitignore`는 `.streamlit/secrets.toml`을 Git에서 제외합니다. 실제 비밀 정보가 담긴 파일은 GitHub에 직접 업로드하거나 다른 사람에게 공유하지 마세요. 여기서는 비밀이 아닌 인사말로 동작을 확인합니다.

## 코드

다음 코드를 실습 폴더의 `app.py`에 저장합니다.

```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

처음 secrets 파일을 만들었다면 실습 폴더에서 다음 명령으로 앱을 다시 시작합니다.

```bash
docker compose restart streamlit
```

앱에 `Hello, Streamlit!`이 표시되면 설정이 완료된 것입니다.

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

선택 과정으로 Community Cloud에 배포할 때는 서비스의 secrets 설정에 값을 별도로 입력합니다.

## 더 읽어 보기
- [로컬 비밀 정보 설정](https://docs.streamlit.io/develop/concepts/connections/secrets-management)
- [Streamlit 앱에 비밀 정보 추가하기](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [비밀 정보 관리](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
