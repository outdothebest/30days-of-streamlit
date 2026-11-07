# День 27

# **Создайте перетаскиваемую панель инструментов с изменяемым размером с помощью Streamlit Elements**

Streamlit Elements—это сторонний компонент который создал [okld](https://github.com/okld) чтобы вы могли делать красивые приложения и информационные панели с виджетами Material UI, редактором Monaco (Visual Studio Code), диаграммами Nivo, и так далее.

## **Как использовать?**

### **Монтаж**

Первым шагом является установка Streamlit Elements в вашей среде:

```bash
pip install "streamlit-elements==0.1.*"
```

Рекомендуется закрепить версию `0.1.*`, так как в будущих версиях могут быть внесены критические изменения API.

### **Применение**

Подробное руководство по использованию можно найти в [README Streamlit Elements](https://github.com/okld/streamlit-elements#getting-started).

## **Что мы строим?**

Цель сегодняшнего задания—создать панель управления, состоящую из трех карт пользовательского интерфейса материалов:

- Первая карта с редактором кода Monaco для ввода некоторых данных;
- Вторая карта для отображения этих данных в диаграмме Nivo Bump;
- Третья карта для отображения URL-адреса видео YouTube, определенного с помощью `st.text_input`.

Вы можете использовать данные, сгенерированные из демонстрации Nivo Bump, на вкладке «данные»: [https://nivo.rocks/bump/](https://nivo.rocks/bump/).

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-elements-demo/main)

## **Код с построчными пояснениями**

```python
# Сначала нам понадобятся следующие импорты для нашего приложения.

import json
import streamlit as st

# Что касается элементов Streamlit, то нам понадобятся все эти объекты.
# Здесь перечислены все доступные объекты и их использование: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# Измените макет страницы, чтобы панель инструментов занимала всю страницу.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # Определите URL для медиаплеера.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# Инициализируйте данные по умолчанию для редактора кода и диаграммы.
#
# Для этого урока нам понадобятся данные для диаграммы Nivo Bump.
# Вы можете получить случайные данные во вкладке «данные»: https://nivo.rocks/bump/
#
# Как вы увидите ниже, этот элемент session state будет обновляться, когда наш
# редактор кода изменится, и он будет прочитан диаграммой Nivo Bump для извлечения данных.

if "data" not in st.session_state:
    st.session_state.data = json.dumps([
        {"id": "Series 1", "data": [{"x": 2020, "y": 1}, {"x": 2021, "y": 2}, {"x": 2022, "y": 1}]},
        {"id": "Series 2", "data": [{"x": 2020, "y": 2}, {"x": 2021, "y": 1}, {"x": 2022, "y": 2}]},
    ], indent=2)

# Определите макет панели инструментов по умолчанию.
# Сетка панели инструментов по умолчанию имеет 12 столбцов.
#
# Для дополнительной информации о доступных параметрах:
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
		# Элемент редактора расположен в координатах x=0 и y=0, занимает 6/12 столбцов и имеет высоту 3.
    dashboard.Item("editor", 0, 0, 6, 3),
		# Элемент диаграммы расположен в координатах x=6 и y=0, занимает 6/12 столбцов и имеет высоту 3.
    dashboard.Item("chart", 6, 0, 6, 3),
    # Элемент мультимедиа расположен в координатах x=0 и y=3, занимает 6/12 столбцов и имеет высоту 4.
    dashboard.Item("media", 0, 2, 12, 4),
]

# Создайте рамку для изображения элементов.

with elements("demo"):

     # Создайте новую панель мониторинга с указанным выше макетом.
     #
     # draggableHandle — это селектор запросов CSS для определения перетаскиваемой части каждого элемента панели.
     # Здесь элементы с именем класса "перетаскиваемый" будут перетаскиваемыми.
     #
     # Для получения дополнительной информации о доступных параметрах сетки панели инструментов:
     # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
     # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

	 # Первая карта, редактор кода.
         #
         # Мы используем параметр 'key' для определения правильного элемента панели.
         #
         # Чтобы содержимое карты автоматически заполняло доступную высоту, мы будем использовать CSS flexbox.
         # sx — это параметр, доступный в каждом виджете Material UI для определения атрибутов CSS.
         #
         # Для получения дополнительной информации о Card, flexbox и sx:
         # https://mui.com/components/cards/
         # https://mui.com/system/flexbox/
         # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

	    # Чтобы сделать этот заголовок перетаскиваемым, нам просто нужно установить для его имени класса значение «перетаскиваемый»,
	    # как определено выше в draggableHandle панели инструментов.

            mui.CardHeader(title="Editor", className="draggable")

	    # Мы хотим, чтобы содержимое карточки занимало всю доступную высоту, установив для flex CSS значение 1.
            # Мы также хотим, чтобы содержимое карты сжималось, когда карта сжимается, установив для minHeight значение 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

		# Вот наш редактор кода Monaco.
                #
                # Во-первых, мы устанавливаем значение по умолчанию st.session_state.data, которое мы инициализировали выше.
                # Во-вторых, мы определяем используемый язык, здесь JSON.
                #
                # Затем мы хотим получить изменения, внесенные в содержимое редактора.
                # Проверяя документацию Monaco, мы обнаруживаем свойство onChange, которое принимает функцию.
                # Эта функция вызывается каждый раз при внесении изменений, и обновленное значение содержимого передается в
                # первый параметр (см. onChange: https://github.com/suren-atoyan/monaco-react#props)
                #
                # Элементы Streamlit предоставляют специальную функцию sync(). Эта функция создает обратный вызов, который
                # автоматически пересылает свои параметры элементам session state Streamlit.
                #
                # Примеры
                # --------
                # Создайте обратный вызов, который перенаправляет свой первый параметр в элемент session state с именем «data»:
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # Создайте обратный вызов, который перенаправляет свой второй параметр элементу session state с именем «ev»:
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # Создайте обратный вызов, который перенаправляет оба своих параметра в session state:
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # Теперь есть проблема: onChange вызывается каждый раз, когда вносятся изменения, что означает, что каждый раз когда
                # вы вводите один символ, все ваше приложение Streamlit запускается повторно.
                #
                # Чтобы избежать этой проблемы, вы можете указать Streamlit Elements ждать другого события
                # (как например, нажатие кнопки), чтобы отправить обновленные данные, обернув ваш обратный вызов с помощью lazy().
                #
                # Для получения дополнительной информации о доступных параметрах для Монако:
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.ISandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

		 # В редакторе Monaco есть ленивый обратный вызов функции, связанный с onChange, что означает, что даже если вы измените
                 # Контент Монако, Streamlit не будет получать уведомления напрямую, поэтому не будет перезагружаться каждый раз.
                 # Итак, нам нужно еще одно неленивое событие для запуска обновления.
                 #
                 # Наше решение будет в создании кнопки, которая запускает обратный вызов при нажатии.
                 # Наш обратный вызов не требует особых действий. Вы можете либо создать пустой
                 # Функция Python или использовать sync() без аргументов.
                 #
                 # Теперь каждый раз, когда вы будете нажимать эту кнопку, будет запускаться обратный вызов onClick, но и все остальные
                 # ленивые обратные вызовы, которые за это время изменились, также будут вызваны.

                mui.Button("Apply changes", onClick=sync())

	# Вторая карта, диаграмма Nivo Bump.
        # Мы будем использовать ту же конфигурацию flexbox, которую мы использовали на первая карте, для автоматической настройки высоты контента.

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

	    # Чтобы сделать этот заголовок перетаскиваемым, нам просто нужно установить для его имени класса значение «перетаскиваемый»,
            # как определено выше в draggableHandle панели инструментов.

            mui.CardHeader(title="Chart", className="draggable")

	    # Как мы обсуждали раньше, нам нужно чтобы наш контент увеличивался и уменьшался по мере того, как пользователь менял размер карты,
            # установливая значение flex к 1 и minHeight к 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

		# Здесь мы будем рисовать нашу диаграмму Bump.
                #
                # Для этого упражнения мы можем просто адаптировать пример Nivo чтобы оно работалои с Streamlit Elements.
                # Пример Nivo доступен на вкладке «код» здесь: https://nivo.rocks/bump/
                #
                # Данные принимают словарь в качестве параметра, поэтому нам нужно преобразовать наши данные JSON из строки в
                # словарь Python с `json.loads()`.
                #
                # Для получения дополнительной информации о других доступных графиках Nivo:
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

	# Третий элемент панели управления, медиаплеер.

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

		# Этот элемент получает энергию от ReactPlayer и поддерживает гораздо больше других плееров
                # чем YouTube. Вы можете проверить это здесь: https://github.com/cookpete/react-player#props.

                media.Player(url=media_url, width="100%", height="100%", controls=True)
```
## Есть вопросы?

Не стесняйтесь задавать любые вопросы, касающиеся Streamlit Elements или этой задачи.: [Тема об элементах Streamlit](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616)
