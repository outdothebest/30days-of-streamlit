# Streamlit Elements로 드래그와 크기 조절이 가능한 대시보드 만들기

Streamlit Elements는 [okld](https://github.com/okld)가 만든 서드파티 컴포넌트로, Material UI 위젯, Monaco 편집기(Visual Studio Code), Nivo 차트 등을 사용해 멋진 애플리케이션과 대시보드를 구성할 수 있는 도구를 제공합니다.

## 사용 방법

### 실습 준비

Streamlit Elements는 실습 환경에 준비되어 있습니다. 아래 전체 코드를 `app.py`에 저장하세요. 초기 데이터도 코드에 포함되어 있어 별도 파일을 준비할 필요가 없습니다.

### 사용법

자세한 사용법은 [Streamlit Elements README](https://github.com/okld/streamlit-elements#getting-started)를 참고하세요.

## 무엇을 만들까요?

오늘의 챌린지 목표는 세 개의 Material UI 카드로 구성된 대시보드를 만드는 것입니다.

- 첫 번째 카드에는 데이터를 입력할 Monaco 코드 편집기를 넣습니다.
- 두 번째 카드에는 그 데이터를 Nivo Bump 차트로 표시합니다.
- 세 번째 카드에는 `st.text_input`으로 지정한 URL의 YouTube 동영상을 표시합니다.

Nivo Bump 데모의 'data' 탭에서 생성한 데이터를 사용할 수 있습니다: https://nivo.rocks/bump/.

## 데모 앱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-elements-demo/main)

## 코드와 한 줄씩 살펴보는 설명

```python
# First, we will need the following imports for our application.

import json
import streamlit as st

# As for Streamlit Elements, we will need all these objects.
# All available objects and there usage are listed there: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# Change page layout to make the dashboard take the whole page.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # Define URL for media player.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# Initialize default data for code editor and chart.
#
# For this tutorial, we will need data for a Nivo Bump chart.
# You can get random data there, in tab 'data': https://nivo.rocks/bump/
#
# As you will see below, this session state item will be updated when our
# code editor change, and it will be read by Nivo Bump chart to draw the data.

if "data" not in st.session_state:
    st.session_state.data = json.dumps([
        {"id": "Series 1", "data": [{"x": 2020, "y": 1}, {"x": 2021, "y": 2}, {"x": 2022, "y": 1}]},
        {"id": "Series 2", "data": [{"x": 2020, "y": 2}, {"x": 2021, "y": 1}, {"x": 2022, "y": 2}]},
    ], indent=2)

# Define a default dashboard layout.
# Dashboard grid has 12 columns by default.
#
# For more information on available parameters:
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    # Editor item is positioned in coordinates x=0 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("editor", 0, 0, 6, 3),
    # Chart item is positioned in coordinates x=6 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("chart", 6, 0, 6, 3),
    # Media item is positioned in coordinates x=0 and y=3, and takes 6/12 columns and has a height of 4.
    dashboard.Item("media", 0, 2, 12, 4),
]

# Create a frame to display elements.

with elements("demo"):

    # Create a new dashboard with the layout specified above.
    #
    # draggableHandle is a CSS query selector to define the draggable part of each dashboard item.
    # Here, elements with a 'draggable' class name will be draggable.
    #
    # For more information on available parameters for dashboard grid:
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # First card, the code editor.
        #
        # We use the 'key' parameter to identify the correct dashboard item.
        #
        # To make card's content automatically fill the height available, we will use CSS flexbox.
        # sx is a parameter available with every Material UI widget to define CSS attributes.
        #
        # For more information regarding Card, flexbox and sx:
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # To make this header draggable, we just need to set its classname to 'draggable',
            # as defined above in dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Editor", className="draggable")

            # We want to make card's content take all the height available by setting flex CSS value to 1.
            # We also want card's content to shrink when the card is shrinked by setting minHeight to 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Here is our Monaco code editor.
                #
                # First, we set the default value to st.session_state.data that we initialized above.
                # Second, we define the language to use, JSON here.
                #
                # Then, we want to retrieve changes made to editor's content.
                # By checking Monaco documentation, there is an onChange property that takes a function.
                # This function is called everytime a change is made, and the updated content value is passed in
                # the first parameter (cf. onChange: https://github.com/suren-atoyan/monaco-react#props)
                #
                # Streamlit Elements provide a special sync() function. This function creates a callback that will
                # automatically forward its parameters to Streamlit's session state items.
                #
                # Examples
                # --------
                # Create a callback that forwards its first parameter to a session state item called "data":
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # Create a callback that forwards its second parameter to a session state item called "ev":
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # Create a callback that forwards both of its parameters to session state:
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # Now, there is an issue: onChange is called everytime a change is made, which means everytime
                # you type a single character, your entire Streamlit app will rerun.
                #
                # To avoid this issue, you can tell Streamlit Elements to wait for another event to occur
                # (like a button click) to send the updated data, by wrapping your callback with lazy().
                #
                # For more information on available parameters for Monaco:
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # Monaco editor has a lazy callback bound to onChange, which means that even if you change
                # Monaco's content, Streamlit won't be notified directly, thus won't reload everytime.
                # So we need another non-lazy event to trigger an update.
                #
                # The solution is to create a button that fires a callback on click.
                # Our callback doesn't need to do anything in particular. You can either create an empty
                # Python function, or use sync() with no argument.
                #
                # Now, everytime you will click that button, onClick callback will be fired, but every other
                # lazy callbacks that changed in the meantime will also be called.

                mui.Button("Apply changes", onClick=sync())

        # Second card, the Nivo Bump chart.
        # We will use the same flexbox configuration as the first card to auto adjust the content height.

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            # To make this header draggable, we just need to set its classname to 'draggable',
            # as defined above in dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Chart", className="draggable")

            # Like above, we want to make our content grow and shrink as the user resizes the card,
            # by setting flex to 1 and minHeight to 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # This is where we will draw our Bump chart.
                #
                # For this exercise, we can just adapt Nivo's example and make it work with Streamlit Elements.
                # Nivo's example is available in the 'code' tab there: https://nivo.rocks/bump/
                #
                # Data takes a dictionary as parameter, so we need to convert our JSON data from a string to
                # a Python dictionary first, with `json.loads()`.
                #
                # For more information regarding other available Nivo charts:
                # https://nivo.rocks/

                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={ "scheme": "spectral" },
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={ "theme": "background" },
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={ "from": "serie.color" },
                    axisTop={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": -36
                    },
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
                    axisRight=None,
                )

        # Third element of the dashboard, the Media player.

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # This element is powered by ReactPlayer, it supports many more players other
                # than YouTube. You can check it out there: https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)

```

## 질문이 있으신가요?

Streamlit Elements나 이번 챌린지에 관한 질문은 [Streamlit Elements 토론 주제](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616)에 편하게 남겨 주세요.
