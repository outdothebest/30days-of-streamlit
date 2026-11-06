# Streamlit 앱 만들기의 기술

오늘은 *#30DaysOfStreamlit* 챌린지의 30일차입니다. 여기까지 함께하신 것을 축하합니다.

이번 튜토리얼에서는 이 학습 챌린지에서 새로 익힌 지식을 활용해 실제 문제를 해결하는 Streamlit 앱을 만들어 보겠습니다.

## 실제 문제

콘텐츠 제작자에게 YouTube 동영상의 썸네일 이미지는 소셜 미디어 홍보와 콘텐츠 제작에 유용한 자료입니다.

이 문제를 어떻게 해결할지 생각하고 Streamlit 앱을 만들어 봅시다.

## 해결 방법

오늘은 YouTube 동영상의 썸네일 이미지를 추출할 수 있는 Streamlit 앱인 `yt-img-app`을 만들겠습니다.

앱이 수행할 작업은 다음 세 단계로 정리할 수 있습니다.

1. 사용자에게 YouTube URL을 입력받습니다.
2. URL을 텍스트 처리해 YouTube 동영상의 고유 ID를 추출합니다.
3. YouTube 동영상 ID를 함수에 전달해 동영상의 썸네일 이미지를 가져와 표시합니다.

## 사용 안내

Streamlit 앱을 사용하려면 YouTube URL을 복사해 텍스트 입력 상자에 붙여 넣으세요.

## 데모 앱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## 코드
`yt-img-app` Streamlit 앱은 다음과 같이 만듭니다.
```python
import streamlit as st

st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
  
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
    
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

다음으로 앱의 제목과 그 아래에 놓일 머리글을 표시합니다.
```python
st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
```
앱 소개를 위한 펼침 상자도 추가해 봅시다.
```python
with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
```
 
여기서는 사용할 이미지 품질을 사용자에게 입력받는 선택 상자를 만듭니다.
```python
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
```

이미지를 추출할 YouTube 동영상의 URL을 사용자에게 입력받는 텍스트 입력 상자를 표시합니다.
```python
yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')
```

입력한 URL을 텍스트 처리하는 함수를 정의합니다.
```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```

마지막으로 제어문을 사용해 URL 입력 안내를 표시할지(`else` 문), YouTube 썸네일 이미지를 표시할지(`if` 문) 결정합니다.
```python
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## 정리

Streamlit 앱을 만들 때는 보통 먼저 문제를 파악하고 정의하는 것부터 시작한다는 점을 살펴봤습니다. 다음으로 문제를 해결할 방법을 세부 단계로 나누어 설계하고, 이를 Streamlit 앱으로 구현합니다.

이 과정에서 사용자에게 어떤 데이터나 정보를 입력받아야 할지, 원하는 최종 출력을 얻으려면 입력을 어떤 방식과 방법으로 처리해야 할지도 결정해야 합니다.

이번 튜토리얼이 즐거우셨기를 바랍니다. Streamlit으로 즐겁게 개발하세요!
