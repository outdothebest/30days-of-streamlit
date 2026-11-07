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

강의 뷰어 이미지는 Python 3.11과 저장소에 포함된 다국어 Streamlit wheel을 사용합니다. 위의 Python 3.12 코드 실습 환경과는 별도로 실행됩니다.

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
