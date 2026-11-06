# st.secrets

`st.secrets`를 사용하면 API 키, 데이터베이스 비밀번호 또는 기타 인증 정보와 같은 기밀 정보를 저장할 수 있습니다.

## 데모 앱

[![Streamlit 앱](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## 로컬 실행 준비

아래 예제를 실행하기 전에 `day17.py`를 저장할 폴더에서 터미널을 열고 `.streamlit` 폴더를 만듭니다.

```bash
mkdir -p .streamlit
```

그 안에 `secrets.toml` 파일을 만들고 다음 내용을 저장합니다. 파일 경로는 `.streamlit/secrets.toml`이며, `message`는 별도의 섹션 없이 최상위 키로 작성합니다.

```toml
message = "Hello, Streamlit!"
```

비밀 정보가 담긴 `.streamlit/secrets.toml`은 GitHub 저장소에 업로드하지 마세요. Git을 사용하는 경우 `.gitignore`에 `.streamlit/secrets.toml`을 추가하여 커밋에서 제외하세요.

## 코드
다음 코드를 같은 폴더의 `day17.py` 파일로 저장합니다.
```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

`day17.py`와 `.streamlit` 폴더가 있는 디렉터리에서 다음 명령을 실행합니다. Streamlit은 실행한 디렉터리의 `.streamlit/secrets.toml`에서 `message` 값을 읽습니다.

```bash
streamlit run day17.py
```

앱에 `Hello, Streamlit!`이 표시되면 설정이 완료된 것입니다. 앱 실행 후 `secrets.toml`을 새로 만들었다면 터미널에서 `Ctrl+C`로 서버를 종료한 뒤 위 명령으로 다시 실행하세요.

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

## 더 읽어 보기
- [로컬 비밀 정보 설정](https://docs.streamlit.io/develop/concepts/connections/secrets-management)
- [Streamlit 앱에 비밀 정보 추가하기](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [비밀 정보 관리](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
