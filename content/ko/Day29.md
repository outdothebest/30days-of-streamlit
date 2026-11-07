# Hugging Face와 Streamlit으로 제로샷 텍스트 분류기 만들기

오늘은 문장과 분류 레이블을 입력하고 Hugging Face API의 예측 결과를 표와 차트로 표시합니다. 별도로 모델을 학습시키지 않고 레이블을 바꾸어 분류하는 방식을 제로샷 분류라고 합니다.

## 실습 준비

1일차의 실습 환경을 그대로 사용합니다. 아래 코드를 실습 폴더의 `app.py`에 저장하세요. 필요한 라이브러리는 이미 준비되어 있습니다.

실제 분류를 실행하려면 [Hugging Face 토큰 설정](https://huggingface.co/settings/tokens)에서 **Inference Providers 호출 권한**이 있는 토큰을 준비하여 앱의 토큰 입력란에 넣습니다. 토큰을 코드에 저장하거나 공유하지 마세요. 토큰이 없어도 앱 화면과 입력 검증을 확인할 수 있습니다.

## 코드

```python
import pandas as pd
import requests
import streamlit as st

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"

st.title("🤗 Zero-shot text classifier")
st.caption("분류를 누르면 입력 문장이 Hugging Face로 전송됩니다.")

with st.form("classifier"):
    token = st.text_input("Hugging Face token", type="password")
    text = st.text_area(
        "Text to classify",
        "I would like a refund for my order.",
        max_chars=2000,
    )
    label_text = st.text_input("Labels (comma-separated)", "refund, delivery, product")
    submitted = st.form_submit_button("Classify")

if submitted:
    labels = list(dict.fromkeys(label.strip() for label in label_text.split(",") if label.strip()))
    if not token.strip():
        st.warning("Hugging Face 토큰을 입력하세요.")
    elif not text.strip() or not 2 <= len(labels) <= 10:
        st.warning("문장과 서로 다른 레이블 2~10개를 입력하세요.")
    else:
        try:
            with st.spinner("Classifying..."):
                response = requests.post(
                    API_URL,
                    headers={"Authorization": f"Bearer {token.strip()}"},
                    json={"inputs": text.strip(), "parameters": {"candidate_labels": labels}},
                    timeout=30,
                )
                response.raise_for_status()
                result = response.json()
                if not isinstance(result, list) or not result or not all(isinstance(row, dict) for row in result):
                    raise ValueError("Unexpected response")
                scores = pd.DataFrame(result)[["label", "score"]]
                if len(scores) != len(labels) or set(scores["label"]) != set(labels):
                    raise ValueError("Unexpected labels")
                scores["score"] = pd.to_numeric(scores["score"], errors="raise")
                if not scores["score"].between(0, 1).all():
                    raise ValueError("Unexpected scores")
        except requests.Timeout:
            st.error("응답 시간이 초과되었습니다. 잠시 후 다시 시도하세요.")
        except requests.RequestException:
            st.error("API 호출에 실패했습니다. 토큰 권한과 서비스 이용 가능 상태를 확인하세요.")
        except (ValueError, KeyError, TypeError):
            st.error("예상한 분류 결과를 받지 못했습니다. 잠시 후 다시 시도하세요.")
        else:
            st.dataframe(scores, hide_index=True)
            st.bar_chart(scores, x="label", y="score")
```

## 실행하고 바꾸어 보기

앱에서 토큰을 입력하고 **Classify**를 누릅니다. 레이블별 점수가 표와 막대 차트에 표시되는지 확인하세요. 문장이나 레이블을 바꾼 뒤 다시 분류해 보세요. 예를 들어 `positive, negative, neutral`로 감정을 분류할 수 있습니다.

API는 토큰 권한, 계정의 사용 한도 및 모델 제공 상태에 따라 호출이 제한될 수 있습니다. 호출이 실패하면 토큰 권한과 [서비스 상태](https://status.huggingface.co/)를 확인하세요.

## 코드 살펴보기

- `st.form`은 문장과 레이블을 작성하는 동안 API를 호출하지 않고, 제출할 때 한 번만 호출하도록 묶습니다.
- `st.text_input`과 `st.text_area`로 입력받고, 쉼표로 나눈 레이블에서 빈 항목과 중복을 제거합니다.
- `requests.post`로 문장과 후보 레이블을 보냅니다. 응답의 `label`은 레이블, `score`는 예측 점수입니다.
- `st.dataframe`과 `st.bar_chart`로 같은 결과를 두 가지 방식으로 살펴봅니다.

## 더 알아보기

- [Hugging Face 제로샷 분류 API](https://huggingface.co/docs/inference-providers/tasks/zero-shot-classification): 이 예제는 현재 공식 안내의 BART 모델과 호출 주소를 사용합니다.
- [Charly Wargnier의 원본 튜토리얼](https://www.charlywargnier.com/post/how-to-create-a-zero-shot-learning-text-classifier-using-hugging-face-and-streamlit): Distilbart와 추가 UI 컴포넌트를 사용하는 확장 예제입니다. 기본 실습은 위 코드만으로 끝나므로 원문의 conda·패키지 설치 단계나 보조 파일을 준비할 필요가 없습니다.
