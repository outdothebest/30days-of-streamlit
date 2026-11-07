# 첫 번째 Streamlit 앱 만들기

## 첫 코드 입력하기

[1일차](https://github.com/outdothebest/30days-of-streamlit/blob/main/content/ko/Day1.md)에서 준비한 실습 폴더의 `app.py`를 편집기로 엽니다. 파일 내용을 다음 코드로 바꾸세요.

```python
import streamlit as st

st.write('Hello world!')
```

파일을 저장한 뒤 [http://localhost:8501](http://localhost:8501)에서 `Hello world!`이 표시되는지 확인합니다. 앱을 종료해 둔 상태라면 실습 폴더에서 다음 명령으로 다시 시작하세요.

```bash
docker compose up -d
```

## 코드 바꾸어 보기

`Hello world!`를 원하는 문장으로 바꾸고 저장해 보세요. 실행 중인 화면에도 새 문장이 표시됩니다.

이후 챌린지에서도 같은 `app.py`의 내용을 당일 예제로 바꾸어 실습합니다. 이전 코드를 보관하려면 다른 이름의 파일로 복사해 두세요.

**축하합니다!** 첫 번째 Streamlit 앱을 만들었습니다!
