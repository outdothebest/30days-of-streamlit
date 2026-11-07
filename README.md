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

뷰어를 켠 상태에서 다른 터미널의 `examples/docker`에서 `docker compose up -d`를 실행하면, 강의는 8502번 탭에서 읽고 실습은 8501번 탭에서 확인할 수 있습니다. 강의의 코드는 자동 실행되지 않으므로 `examples/docker/app.py`에 옮겨 저장하세요. 두 명령 모두 `STREAMLIT_PORT`를 사용하므로 전역 환경 변수로 같은 포트를 지정하지 마세요. 각각 종료하려면 해당 폴더에서 `docker compose down`을 실행합니다.

호스트에서는 실습 파일을 편집할 수 있지만 컨테이너의 `/app` 마운트는 읽기 전용입니다. 예제가 파일을 생성해야 한다면 `/tmp` 등의 쓰기 가능한 경로를 사용하세요. `/tmp` 파일은 컨테이너를 삭제하면 사라집니다.

### 호환성 검증 범위

macOS ARM64의 OrbStack에서 Linux ARM64 컨테이너(Python 3.12.16, Streamlit 1.54.0)를 검증했습니다. 두 이미지 빌드와 `pip check`, 동시 실행, 뷰어의 12개 언어·직접 링크·일차 이동, 실습 파일 저장 후 반영을 확인했습니다. 한국어 예제의 위젯·폼·쿼리 파라미터·세션 상태·캐싱과 Day14 프로파일링, Day27 Elements 콜백, Day28 SHAP, Day29 회귀 테스트도 확인했습니다. Elements 버튼은 실제 브라우저에서, Monaco의 lazy/sync 데이터 전달은 컴포넌트 위젯 메시지를 통한 자동 테스트로 확인했습니다. 외부 서비스 전체, 모든 예제의 브라우저 조작, Linux AMD64 및 Windows 호스트는 검증하지 않았습니다.

뷰어 회귀 테스트는 뷰어 의존성이 설치된 저장소 루트에서 `python -m unittest discover -s tests -p test_viewer.py`로 실행합니다. 확장 패키지 회귀 테스트를 포함한 전체 테스트는 패치가 적용된 실습 이미지에서 저장소 루트를 `/app`에 마운트하고 `python -m unittest discover -s tests`로 실행합니다.

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
