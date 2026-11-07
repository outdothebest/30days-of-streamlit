# 30days of Streamlit

한국어 실습은 준비된 환경에서 코드 작성부터 시작합니다. [실습 환경 준비하기](content/ko/Day1.md)를 참고하세요.

## Run the course browser locally

With OrbStack (or another Docker engine) running, start the app from the repository root:

```sh
docker compose up --build -d
```

Open http://localhost:8502 to browse the daily challenges. Content and locale
directories are mounted read-only, so local edits are available without rebuilding
the image. Refresh the browser after editing a challenge.

If port 8502 is already in use, run `STREAMLIT_PORT=8503 docker compose up --build -d`
and open http://localhost:8503 instead.

View logs with `docker compose logs -f streamlit` and stop the app with
`docker compose down`.

The image uses Python 3.11 and the bundled Streamlit wheel required by this
repository's multilingual features.

* [English](readmes/en/README.md)
* [বাংলা](readmes/bn/README.md)
* [Deutsch](readmes/de/README.md)
* [français](readmes/fr/README.md)
* [हिन्दी](readmes/hi/README.md)
* [日本語](readmes/ja/README.md)
* [한국어](readmes/ko/README.md)
* [русский](readmes/ru/README.md)
* [português](readmes/pt/README.md)
* [中文](readmes/zh/README.md)
* [polski](readmes/pl/README.md)
* [español](readmes/es/README.md)


