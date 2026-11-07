# st.form

`st.form`은 여러 요소를 "Submit" 버튼과 함께 묶어 처리하는 폼을 만듭니다.

일반적으로 사용자가 위젯을 조작할 때마다 Streamlit 앱이 다시 실행됩니다.

폼은 여러 요소와 위젯을 시각적으로 묶어 주며 제출 버튼을 포함하는 컨테이너입니다. 폼 안에서는 사용자가 하나 이상의 위젯을 몇 번이든 조작해도 앱이 다시 실행되지 않습니다. 마지막에 폼의 제출 버튼을 누르면 폼 안에 있는 모든 위젯의 값이 한꺼번에 Streamlit으로 전송됩니다.

폼 객체에 요소를 추가할 때는 `with` 구문을 사용하는 방법을 권장합니다. 또는 폼을 변수에 할당한 뒤 그 변수에서 Streamlit 메서드를 직접 호출하는 객체 표기법을 사용할 수도 있습니다. 예제 앱에서 두 방법을 살펴보세요.

폼에는 몇 가지 제약이 있습니다.
- 모든 폼에는 `st.form_submit_button`이 있어야 합니다.
- 폼에는 `st.button`과 `st.download_button`을 추가할 수 없습니다.
- 폼은 앱의 어느 곳에나 배치할 수 있지만(사이드바, 열 등), 다른 폼 안에 넣을 수는 없습니다.

폼에 대한 자세한 내용은 [커뮤니티 소개 글](https://discuss.streamlit.io/t/introducing-submit-button-and-forms/12401)을 참고하세요.

## 데모 앱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## 코드
`st.form`은 다음과 같이 사용합니다.
```python
import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')
    
    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## 코드 한 줄씩 살펴보기
Streamlit 앱을 만들 때 가장 먼저 할 일은 다음과 같이 `streamlit` 라이브러리를 `st`라는 이름으로 가져오는 것입니다.
```python
import streamlit as st
```

이어서 앱의 제목을 만듭니다.
```python
st.title('st.form')
```

### 첫 번째 예제
첫 번째 예제에서는 `with` 구문으로 `st.form` 명령을 사용합니다. 폼 안에 먼저 `Order your coffee`라는 소제목을 작성한 뒤 커피 주문 정보를 받을 입력 위젯(`st.selectbox`, `st.select_slider`, `st.checkbox`)을 만듭니다. 마지막으로 `st.form_submit_button` 명령으로 제출 버튼을 만듭니다. 이 버튼을 클릭하면 모든 사용자 입력이 하나로 묶여 앱으로 전달되고 처리됩니다.
```python
# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
```

다음으로 제출 버튼을 클릭한 뒤 실행할 로직을 추가합니다. Streamlit 앱을 처음 불러오면 기본적으로 `else` 문이 실행되어 `☝️ Place your order!`라는 메시지가 표시됩니다. 제출 버튼을 클릭하면 여러 위젯으로 받은 입력이 각각의 변수(예: `coffee_bean_val`, `coffee_roast_val` 등)에 저장되고, f-string과 `st.markdown` 명령을 통해 출력됩니다.
```python
if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')
```


### 두 번째 예제
두 번째 예제에서는 `st.form`을 객체 표기법으로 사용합니다. `st.form` 명령의 결과를 `form` 변수에 할당한 뒤, `slider`나 `form_submit_button` 같은 여러 Streamlit 명령을 `form` 변수에서 호출합니다.
```python
# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## 더 알아보기
- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [제출 버튼과 폼 소개](https://discuss.streamlit.io/t/introducing-submit-button-and-forms/12401)
