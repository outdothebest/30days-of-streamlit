# 실습 환경 준비하기

Streamlit 코드를 작성하고 바로 화면에서 확인할 수 있는 실습 환경을 준비합니다. Python이나 conda를 따로 설치할 필요가 없습니다.

## 처음 한 번 준비하기

1. 편집기(예: VS Code)와 [Docker Desktop](https://www.docker.com/products/docker-desktop/)을 설치하고 실행합니다. 이미 Docker와 Compose를 사용하고 있다면 그대로 사용하세요.
2. [실습 자료 ZIP](https://github.com/outdothebest/30days-of-streamlit/archive/refs/heads/main.zip)을 내려받아 압축을 풉니다.
3. 압축을 푼 자료의 `examples/docker` 폴더를 편집기로 열고, 그 폴더에서 터미널을 엽니다.

## 앱 시작하기

```bash
docker compose up -d
```

처음에는 필요한 파일을 내려받고 환경을 준비하므로 시간이 걸릴 수 있습니다. 준비가 끝나면 [http://localhost:8501](http://localhost:8501)을 열어 시작 화면을 확인하세요.

이후 챌린지에서는 이 폴더의 `app.py`에 예제 코드를 작성하고 저장합니다. 필요한 라이브러리는 준비되어 있으며, 코드를 저장하면 실행 중인 앱에 변경이 반영됩니다.

## 실습 마치기

```bash
docker compose stop
```

다음 실습 때 같은 폴더에서 시작 명령을 다시 실행하면 됩니다.

## 실행이 잘되지 않을 때

- Docker가 실행 중인지, 터미널이 `examples/docker` 폴더에 열려 있는지 확인하세요.
- 첫 실행 중에는 파일 다운로드가 끝날 때까지 기다렸다가 브라우저를 새로고침하세요.
- 이미 다른 앱이 `8501`을 사용하고 있다면 그 앱을 종료한 뒤 시작하세요.
- 오류가 계속되면 `docker compose logs streamlit`으로 메시지를 확인하세요.
