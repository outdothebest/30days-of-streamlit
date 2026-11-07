# Streamlit Elements के साथ ड्रैग करने योग्य और आकार बदलने योग्य डैशबोर्ड बनाएं
Streamlit Elements [okld](https://github.com/okld) द्वारा बनाया गया एक थर्ड-पार्टी कंपोनेंट है जो आपको Material UI विजेट्स, Monaco संपादक (विजुअल स्टूडियो कोड), Nivo चार्ट और अन्य के साथ सुंदर ऐप्लिकेशन और डैशबोर्ड बनाने के लिए टूल देता है|

## कैसे इस्तेमाल करे?

### इंस्टालेशन

पहला कदम आपके इन्वायरमेंट में Streamlit Elements को इंस्टॉल करना है:

```bash
pip install "streamlit-elements==0.1.*"
```

वर्शन को `0.1.*` पर पिन करने की अनुशंसा की जाती है, क्योंकि भविष्य के वर्ज़न में ब्रेकिंग API परिवर्तन हो सकते हैं|


### उपयोग

इन-डेप्थ उपयोग गाइड के लिए आप [Streamlit Elements README](https://github.com/okld/streamlit-elements#getting-started) का संदर्भ ले सकते हैं|


## हम क्या बना रहे हैं?

आज के चैलेंज का लक्ष्य तीन Material UI कार्ड से बना एक डैशबोर्ड बनाना है:

- कुछ डेटा इनपुट करने के लिए Monaco कोड एडिटर वाला पहला कार्ड;
- Nivo Bump चार्ट में उस डेटा को प्रदर्शित करने के लिए दूसरा कार्ड;
- YouTube वीडियो URL दिखाने के लिए एक तीसरा कार्ड एक `st.text_input` के साथ परिभाषित किया गया है|

आप Nivo Bump डेमो से जेनरेट किए गए डेटा का उपयोग 'डेटा' टैब में कर सकते हैं: https://nivo.rocks/bump/.

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-elements-demo/main)

## लाइन-बाय-लाइन स्पष्टीकरण के साथ कोड

```python
# सबसे पहले, हमें अपने ऐप्लिकेशन के लिए निम्नलिखित इम्पोर्ट की आवश्यकता होगी.

import json
import streamlit as st
from pathlib import Path

# Streamlit एलिमेंट्स के लिए, हमें इन सभी ऑब्जेक्ट्स की आवश्यकता होगी.
# सभी उपलब्ध ऑब्जेक्ट्स और उनका उपयोग वहां सूचीबद्ध है: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# डैशबोर्ड को पूरे पेज पर ले जाने के लिए पेज लेआउट बदलें.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # मीडिया प्लेयर के लिए URL परिभाषित करें.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# कोड एडिटर और चार्ट के लिए डिफ़ॉल्ट डेटा को इनिशियलाइज़ करें.
#
# इस ट्यूटोरियल के लिए, हमें Nivo Bump चार्ट के लिए डेटा की आवश्यकता होगी.
# आप वहां रैंडम डेटा प्राप्त कर सकते हैं, टैब 'डेटा' में: https://nivo.rocks/bump/
#
# जैसा कि आप नीचे देखेंगे, हमारे कोड एडिटर में परिवर्तन होने पर यह सेशन स्टेट आइटम अपडेट हो जाएगा, 
# और इसे डेटा निकालने के लिए Nivo Bump चार्ट द्वारा पढ़ा जाएगा.

if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

# एक डिफ़ॉल्ट डैशबोर्ड लेआउट परिभाषित करें.
# Dashboard grid has 12 columns by default.
#
# उपलब्ध मापदंडों के बारे में अधिक जानकारी के लिए:
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props.

layout = [
    # एडिटर आइटम निर्देशांक x=0 और y=0 में स्थित है, और 6/12 कॉलम लेता है और इसकी ऊंचाई 3 है.
    dashboard.Item("editor", 0, 0, 6, 3),
    # चार्ट आइटम निर्देशांक x=6 और y=0 में स्थित है, और 6/12 कॉलम लेता है और इसकी ऊंचाई 3 है.
    dashboard.Item("chart", 6, 0, 6, 3),
    # मीडिया आइटम निर्देशांक x=0 और y=3 में स्थित है, और 6/12 कॉलम लेता है और इसकी ऊंचाई 4 है.
    dashboard.Item("media", 0, 2, 12, 4),
]

# एलिमेंट्स को प्रदर्शित करने के लिए एक फ़्रेम बनाएं.

with elements("demo"):

    # ऊपर बताए गए लेआउट के साथ नया डैशबोर्ड बनाएं.
    #
    # 
    # यहां, 'ड्रैगेबल' क्लास नाम वाले एलिमेंट्स ड्रैगेबल होंगे.
    # draggableHandle प्रत्येक डैशबोर्ड आइटम के ड्रैग करने योग्य हिस्से को परिभाषित करने के लिए एक CSS क्वेरी चयनकर्ता है.
    # डैशबोर्ड ग्रिड के लिए उपलब्ध पैरामीटर पर अधिक जानकारी के लिए:
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # पहला कार्ड, कोड एडिटर.
        #
        # हम सही डैशबोर्ड आइटम की पहचान करने के लिए 'की' पैरामीटर का उपयोग करते हैं.
        #
        # उपलब्ध ऊंचाई में कार्ड की सामग्री को स्वचालित रूप से भरने के लिए, हम CSS flexbox का उपयोग करेंगे.
        # CSS विशेषताओं को परिभाषित करने के लिए sx प्रत्येक सामग्री UI विजेट के साथ उपलब्ध एक पैरामीटर है.
        #
        # कार्ड, flexbox और sx के बारे में अधिक जानकारी के लिए:
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # इस हेडर को ड्रैगेबल बनाने के लिए, हमें इसके क्लास नाम को 'ड्रैगेबल' पर सेट करने की आवश्यकता है, जैसा कि
            # डैशबोर्ड में ऊपर परिभाषित किया गया है. Grid का draggableHandle.

            mui.CardHeader(title="Editor", className="draggable")

            # हम flex CSS मान को 1 पर सेट करके कार्ड की सामग्री को उपलब्ध सभी ऊंचाई तक ले जाना चाहते हैं.
            # हम यह भी चाहते हैं कि minHeight को 0 पर सेट करके कार्ड के सिकुड़ने पर कार्ड की सामग्री भी सिकुड़ जाए.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # यह रहा हमारा Monaco कोड एडिटर.
                #
                # सबसे पहले, हम डिफ़ॉल्ट मान को st.session_state.data पर सेट करते हैं जिसे हमने ऊपर इनिशियलाइज़ किया था.
                # दूसरा, हम उपयोग करने के लिए भाषा परिभाषित करते हैं, यहां JSON.
                #
                # फिर, हम एडिटर की सामग्री में किए गए परिवर्तनों को पुनः प्राप्त करना चाहते हैं.
                # Monaco दस्तावेज़ों की जांच करके, एक onChange प्रॉपर्टी है जो काम करती है.
                # हर बार बदलाव किए जाने पर इस फ़ंक्शन को कॉल किया जाता है, और अपडेट किए गए सामग्री मान को पहले
                # पैरामीटर में पास किया जाता है (cf. onChange: https://github.com/suren-atoyan/monaco-react#props)
                #
                # Streamlit एलिमेंट्स एक विशेष सिंक () फ़ंक्शन प्रदान करते हैं. 
                # यह फ़ंक्शन एक कॉलबैक बनाता है जो स्वचालित रूप से इसके पैरामीटर को Streamlit के सेशन स्टेट आइटम में फॉरवर्ड करेगा.
                #
                # उदाहरण
                # --------
                # एक कॉलबैक बनाएं जो "डेटा" नामक सेशन स्टेट आइटम के लिए अपना पहला पैरामीटर फॉरवर्ड करता है:
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # एक कॉलबैक बनाएं जो इसके दूसरे पैरामीटर को "ev" नामक सेशन स्टेट आइटम पर फॉरवर्ड करता है:
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # एक कॉलबैक बनाएँ जो इसके दोनों मापदंडों को सेशन स्टेट में फॉरवर्ड करता है:
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # अब, एक समस्या है: परिवर्तन किए जाने पर हर बार onChange कॉल किया जाता है, जिसका अर्थ है कि हर बार जब आप
                # एक ही वर्ण टाइप करते हैं, तो आपका संपूर्ण Streamlit ऐप फिर से चालू हो जाएगा.
                #
                # इस समस्या से बचने के लिए, आप अपने कॉलबैक को लेज़ी() के साथ रैपिंग करके अपडेट किए गए डेटा को भेजने के लिए
                # Streamlit एलिमेंट्स को किसी अन्य ईवेंट के होने की प्रतीक्षा करने के लिए कह सकते हैं (जैसे एक बटन क्लिक).
                #
                # Monaco के लिए उपलब्ध मापदंडों के बारे में अधिक जानकारी के लिए:
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # Monaco एडिटर के पास onChange के लिए एक लेज़ी कॉलबैक है, जिसका अर्थ है कि भले ही आप Monaco की
                # सामग्री को बदलते हैं, Streamlit को सीधे अधिसूचित नहीं किया जाएगा, इस प्रकार हर बार पुनः लोड नहीं होगा.
                # इसलिए हमें अपडेट को ट्रिगर करने के लिए एक और नॉन-लेज़ी इवेंटकी ज़रूरत है.
                #
                # समाधान एक ऐसा बटन बनाना है जो क्लिक करने पर कॉलबैक को सक्रिय करता है.
                # हमारे कॉलबैक को विशेष रूप से कुछ भी करने की ज़रूरत नहीं है.
                # आप या तो एक खाली Python फ़ंक्शन बना सकते हैं या बिना किसी तर्क के सिंक () का उपयोग कर सकते हैं.
                #
                # अब, जब भी आप उस बटन पर क्लिक करेंगे, onClick कॉलबैक सक्रिय कर दिया जाएगा, 
                # लेकिन इस दौरान बदले गए हर दूसरे लेज़ी कॉलबैक को भी कॉल किया जाएगा.

                mui.Button("Apply changes", onClick=sync())

        # दूसरा कार्ड, Nivo Bump चार्ट.
        # हम सामग्री की ऊंचाई को स्वतः समायोजित करने के लिए पहले कार्ड के समान flexbox कॉन्फ़िगरेशन का उपयोग करेंगे.

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            # इस हेडर को ड्रैगेबल बनाने के लिए, हमें इसके क्लास नाम को 'ड्रैगेबल' पर सेट करने की आवश्यकता है,
            # जैसा कि डैशबोर्ड में ऊपर परिभाषित किया गया है. Grid का draggableHandle.

            mui.CardHeader(title="Chart", className="draggable")

            # ऊपर की तरह, हम flex को 1 और minHeight को 0 पर सेट करके उपयोगकर्ता द्वारा कार्ड का आकार बदलने
            # पर अपनी सामग्री को बढ़ाना और सिकोड़ना चाहते हैं.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # यहीं पर हम अपना Bump चार्ट बनाएंगे.
                #
                # इस अभ्यास के लिए, हम बस Nivo के उदाहरण को अनुकूलित कर सकते हैं और इसे Streamlit एलिमेंट्स के साथ काम करने योग्य बना सकते हैं.
                # Nivo का उदाहरण वहां 'कोड' टैब में उपलब्ध है: https://nivo.rocks/bump/
                #
                # डेटा एक डिक्शनरी को पैरामीटर के रूप में लेता है, इसलिए हमें अपने JSON डेटा को पहले एक स्ट्रिंग से
                # Python डिक्शनरी में `json.loads()` के साथ बदलने की आवश्यकता है.
                #
                # अन्य उपलब्ध Nivo चार्ट्स के बारे में अधिक जानकारी के लिए:
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

        # डैशबोर्ड का तीसरा एलिमेंट, मीडिया प्लेयर.

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # यह एलिमेंट ReactPlayer द्वारा संचालित है, यह YouTube के अलावा और भी कई प्लेयर को सपोर्ट करता है.
                # आप इसे वहां देख सकते हैं: https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)

```

## कोई प्रश्न है?

Streamlit Elements या इस चैलेंज के बारे में कोई भी प्रश्न बेझिझक पूछें: [Streamlit Elements टॉपिक](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616)
