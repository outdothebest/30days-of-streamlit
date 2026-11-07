# 30 Days of Streamlit 🎈

30일간의 실습으로 Python 데이터 앱을 만들고 공유하는 방법을 배우는 학습 자료입니다. 기본 위젯부터 레이아웃, 세션 상태, 캐싱까지 Streamlit의 주요 기능을 예제로 익힙니다.

이 저장소는 [streamlit/30days-i18n](https://github.com/streamlit/30days-i18n)을 바탕으로 한국어 학습 자료와 실습 환경을 보완한 포크입니다. 원본 챌린지는 [streamlit/30days](https://github.com/streamlit/30days)에서 확인할 수 있습니다.

## 학습 시작하기

Python의 변수, 함수, 패키지 사용법을 알고 있다면 시작할 수 있습니다. 한국어 과정은 Mac, 코드 편집기(예: VS Code), [OrbStack](https://orbstack.dev/download)을 기준으로 안내합니다. Python이나 conda를 호스트에 따로 설치할 필요는 없습니다.

1. [실습 환경 준비하기](content/ko/Day1.md)를 따라 자료를 내려받고 OrbStack을 실행합니다.
2. 편집기로 `examples/docker` 폴더를 열고, 해당 폴더의 터미널에서 앱을 시작합니다.

   ```bash
   docker compose up -d
   ```

3. 처음 빌드가 끝나면 [http://localhost:8501](http://localhost:8501)을 엽니다.
4. [한국어 과정 안내](readmes/ko/README.md)와 일차별 자료를 보며 `examples/docker/app.py`에 예제 코드를 작성하고 저장합니다. 저장한 코드는 실행 중인 앱에 반영됩니다.

실습 환경은 Python 3.12와 고정된 패키지 버전을 사용합니다. 필요한 패키지는 [실습용 requirements.txt](examples/docker/requirements.txt)에 정의되어 있으며, 첫 실행에는 이미지와 패키지를 내려받을 인터넷 연결이 필요합니다.

실습을 마치면 같은 폴더에서 다음 명령을 실행합니다. 다음 실습 때는 시작 명령을 다시 실행하면 됩니다.

```bash
docker compose stop
```

실행이 잘되지 않으면 OrbStack이 실행 중인지와 현재 폴더를 확인하고, `docker compose logs streamlit`으로 로그를 살펴보세요. 기본 포트가 사용 중이면 `STREAMLIT_PORT=8503 docker compose up -d`로 실행한 뒤 [http://localhost:8503](http://localhost:8503)을 엽니다.

## 30일 학습 구성

| 단계 | 일차 | 학습 내용 |
| --- | --- | --- |
| 초급 | 1–7일차 | 실습 환경 준비, 첫 앱, 기본 출력과 입력 위젯 |
| 중급 | 8–23일차 | 다양한 위젯, 차트, 레이아웃과 외부 서비스 연동 |
| 고급 | 24–30일차 | 캐싱, 세션 상태, 데이터 처리와 앱 구성 |

[1일차](content/ko/Day1.md)부터 순서대로 진행하며 하루에 하나씩 예제를 실행하고 코드를 바꿔 보세요. 한국어 과정은 설치 부담을 줄이기 위해 원본과 다른 준비 절차를 사용합니다. 앱 공유와 클라우드 배포는 선택 과정이며, 일부 예제에는 외부 서비스 계정이나 별도 설정이 필요합니다. 자세한 조건은 각 일차의 안내를 확인하세요.

## 저장소 구성

| 경로 | 역할 |
| --- | --- |
| `content/<언어>/DayN.md` | 일차별 학습 자료와 예제 |
| `readmes/<언어>/README.md` | 언어별 과정 소개 |
| `locale/` | 강의 뷰어의 번역 리소스 |
| `streamlit_app.py` | 언어와 일차별 강의 내용을 표시하는 뷰어 진입점 |
| `examples/docker/` | 학습자가 `app.py`를 편집하는 Docker 실습 환경 |

위 시작 명령은 `examples/docker/app.py`를 실행합니다. 루트의 `streamlit_app.py`는 일차별 학습 자료를 읽는 강의 뷰어입니다.

## 강의 뷰어 실행하기

OrbStack 또는 다른 Docker 엔진을 실행한 뒤, 저장소 루트의 터미널에서 시작합니다.

```bash
docker compose up --build -d
```

[http://localhost:8502](http://localhost:8502)에서 일차별 강의를 볼 수 있습니다. `content/`와 `locale/`은 읽기 전용으로 마운트되므로 강의 파일을 수정한 뒤 이미지를 다시 빌드할 필요 없이 브라우저를 새로고침하면 됩니다.

기본 포트가 사용 중이면 `STREAMLIT_PORT=8503 docker compose up --build -d`로 실행하고 [http://localhost:8503](http://localhost:8503)을 엽니다. 로그는 `docker compose logs -f streamlit`으로 확인하고, 종료할 때는 저장소 루트에서 `docker compose down`을 실행합니다.

강의 뷰어와 코드 실습 이미지는 모두 Python 3.12와 표준 Streamlit 1.54.0을 사용합니다. 뷰어의 번역은 저장소의 `locale/` 카탈로그를 Python `gettext`로 읽습니다. Streamlit 자체 메뉴는 표준 배포판의 표시를 따릅니다.

사이드바의 **Language / 언어**에서 강의 언어를 선택합니다. 첫 접속 시 브라우저의 언어 설정을 참고하며, 지원하지 않는 언어는 영어로 표시합니다. `http://localhost:8502/?language=ko&challenge=Day27`처럼 언어와 일차를 지정한 링크로 바로 열 수도 있습니다. 언어나 일차를 선택하면 URL도 갱신됩니다.

## 강의를 보면서 실습하기

터미널 두 개를 열어 각각 다음 위치에서 시작합니다. 아래 명령의 `STREAMLIT_PORT`는 해당 명령에만 적용됩니다.

| 터미널 위치 | 시작 명령 | 브라우저 탭 |
| --- | --- | --- |
| 저장소 루트 | `STREAMLIT_PORT=8502 docker compose up --build -d` | [강의 뷰어](http://localhost:8502) |
| `examples/docker` | `STREAMLIT_PORT=8501 docker compose up --build -d` | [코드 실습 앱](http://localhost:8501) |

강의 탭에서 언어와 일차를 선택하고, 실습 탭을 나란히 열어 두세요. **강의 화면의 코드는 자동 실행되지 않습니다.** 호스트의 편집기로 `examples/docker/app.py`에 코드를 옮겨 작성하고 저장한 뒤 실습 탭에서 결과를 확인합니다. 실습 앱은 파일 변경을 감지해 다시 실행합니다. 강의 탭을 새로고침하는 것만으로 실습 코드는 바뀌지 않습니다.

두 Compose 설정은 모두 `STREAMLIT_PORT`를 호스트 포트로 사용합니다. 셸에서 `export STREAMLIT_PORT=8503`처럼 전역으로 지정하거나 각 폴더의 `.env`에 같은 값을 넣으면 두 앱이 같은 포트를 점유하려 해 충돌할 수 있습니다. 위처럼 명령별로 다른 값을 지정하세요. 기본 포트가 이미 사용 중이면 뷰어는 `STREAMLIT_PORT=18502`, 실습은 `STREAMLIT_PORT=18501`로 실행하고 각각의 포트로 접속합니다. 컨테이너 내부 포트는 두 앱 모두 8501이며 변경할 필요가 없습니다.

### 파일 편집과 저장 위치

읽기 전용 마운트는 **컨테이너에서 호스트 파일에 쓰는 것을 제한**합니다. 호스트 편집기에서는 파일을 수정하고 저장할 수 있습니다.

- 뷰어는 `content/`와 `locale/`을 읽기 전용으로 마운트합니다. 호스트에서 강의 자료를 수정한 뒤 강의 탭을 새로고침합니다.
- 실습은 `examples/docker/` 전체를 `/app`에 읽기 전용으로 마운트합니다. 호스트에서 `app.py`나 입력 데이터를 편집할 수 있지만, 앱이 `open("result.csv", "w")` 또는 `df.to_csv("result.csv")`처럼 `/app` 아래에 파일을 쓰면 실패합니다. 하위 디렉터리를 만드는 코드도 같은 제약을 받습니다.
- 중간 결과는 `tempfile.TemporaryDirectory()` 등으로 `/tmp`에 저장하세요. 컨테이너가 제거되면 사라질 수 있으므로 영구 보관용으로 사용하지 않습니다. 결과를 사용자 PC에 보관하려면 메모리에서 CSV 등을 만든 뒤 `st.download_button`으로 내려받을 수 있습니다. 비밀 키나 사용자 데이터를 저장소에 넣지 마세요.

### 각각 종료하기

| 터미널 위치 | 종료 명령 | 효과 |
| --- | --- | --- |
| 저장소 루트 | `docker compose down` | 강의 뷰어 컨테이너와 해당 Compose 네트워크 제거 |
| `examples/docker` | `docker compose stop` | 실습 컨테이너 정지; 다음에 `docker compose up -d`로 재시작 |

각 명령은 해당 폴더의 앱에 적용됩니다. 시작할 때 `-p`로 프로젝트 이름을 지정했다면 종료할 때도 같은 이름을 지정하세요. 포트 충돌로 시작하지 못한 앱도 해당 폴더에서 종료 명령으로 정리할 수 있습니다.

### 호환성 검증 범위

macOS ARM64의 OrbStack에서 Linux ARM64 컨테이너(Python 3.12.16, Streamlit 1.54.0)를 검증했습니다. 두 이미지 빌드와 `pip check`, 동시 실행, 뷰어의 12개 언어·직접 링크·일차 이동, 실습 파일 저장 후 반영을 확인했습니다. 한국어 예제의 위젯·폼·쿼리 파라미터·세션 상태·캐싱과 Day14 프로파일링, Day27 Elements 콜백, Day28 SHAP, Day29 회귀 테스트도 확인했습니다. Elements 버튼은 실제 브라우저에서, Monaco의 lazy/sync 데이터 전달은 컴포넌트 위젯 메시지를 통한 자동 테스트로 확인했습니다. 외부 서비스 전체, 모든 예제의 브라우저 조작, Linux AMD64 및 Windows 호스트는 검증하지 않았습니다.

뷰어 회귀 테스트는 뷰어 의존성이 설치된 저장소 루트에서 `python -m unittest discover -s tests -p test_viewer.py`로 실행합니다. 확장 패키지 회귀 테스트를 포함한 전체 테스트는 패치가 적용된 실습 이미지에서 저장소 루트를 `/app`에 마운트하고 `python -m unittest discover -s tests`로 실행합니다.

### 이전 구성의 동시 실행 검증

아래 기록은 버전 통일 전 구성의 검증 이력입니다. 현재 버전과 검증 범위는 위 절을 참고하세요.

2026-11-08, macOS ARM64 + OrbStack(Linux aarch64)에서 두 이미지를 빌드 캐시를 사용해 빌드하고, 기존 서비스와 겹치지 않는 포트 18537(뷰어)·18538(실습)에서 동시에 실행했습니다. 실제 설치 버전은 뷰어 Python 3.11.18 / Streamlit 1.21.0, 실습 Python 3.12.16 / Streamlit 1.54.0이었습니다. 브라우저 두 탭에서 한국어 강의 표시와 호스트의 `app.py` 저장 후 실습 화면 자동 반영을 확인했습니다. 동일한 호스트 포트 18537로 실습 앱을 추가 시작하면 `port is already allocated`로 실패하는 것을 재현했고, 서로 다른 포트에서는 두 앱이 healthy 상태였습니다. 뷰어의 `down`과 실습의 `stop`도 실행했습니다. 실습 컨테이너의 `/app` 쓰기 실패와 `tempfile.TemporaryDirectory()` 안의 파일 저장·읽기를 확인했습니다.

모든 일차 예제·확장 패키지, 다운로드 버튼의 실제 다운로드, 다른 운영체제·CPU, 캐시 없는 전체 빌드는 이번 문서 작업에서 검증하지 않았습니다. 버전 변경 후에는 해당 동작을 다시 확인해야 합니다.

## 언어별 안내

- [한국어](readmes/ko/README.md)
- [English](readmes/en/README.md)
- [বাংলা](readmes/bn/README.md)
- [Deutsch](readmes/de/README.md)
- [français](readmes/fr/README.md)
- [हिन्दी](readmes/hi/README.md)
- [日本語](readmes/ja/README.md)
- [русский](readmes/ru/README.md)
- [português](https://github.com/franciscoed/30days)
- [中文](readmes/zh/README.md)
- [polski](readmes/pl/README.md)
- [español](readmes/es/README.md)

## 참고 자료

- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [Streamlit API 레퍼런스](https://docs.streamlit.io/develop/api-reference)
- [원본 30 Days of Streamlit](https://github.com/streamlit/30days)
- [다국어 원본 저장소](https://github.com/streamlit/30days-i18n)
- [라이선스](LICENSE)
