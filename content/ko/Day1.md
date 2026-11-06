# 로컬 개발 환경 설정하기

Streamlit 앱을 본격적으로 만들기 전에 먼저 개발 환경을 설정해야 합니다.

conda를 설치하고 환경을 설정하는 것부터 시작하겠습니다.

## **conda 설치하기**
- https://docs.conda.io/en/latest/miniconda.html 에서 운영 체제(Windows, Mac 또는 Linux)를 선택하여 `conda`를 설치합니다.
- 설치 프로그램을 다운로드한 다음 실행하여 `conda`를 설치합니다.

## **새 conda 환경 만들기**
conda를 설치했으니 이제 Python 라이브러리의 모든 의존성을 관리할 conda 환경을 만들어 보겠습니다.

Python 3.9를 사용하는 새 환경을 만들려면 다음을 입력합니다.
```bash
conda create -n stenv python=3.9
```

여기서 `create -n stenv`는 `stenv`라는 이름의 conda 환경을 만들고, `python=3.9`는 Python 3.9 버전을 사용하도록 conda 환경을 설정합니다.

## **conda 환경 활성화하기**

방금 만든 `stenv`라는 conda 환경을 사용하려면 명령줄에 다음을 입력합니다.

```bash
conda activate stenv
```

## **Streamlit 라이브러리 설치하기**

이제 `streamlit` 라이브러리를 설치할 차례입니다.
```bash
pip install streamlit
```

## **Streamlit 데모 앱 실행하기**
Streamlit 데모 앱(그림 1)을 실행하려면 다음을 입력합니다.
```bash
streamlit hello
```
