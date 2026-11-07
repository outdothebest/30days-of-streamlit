# Cree un tablero que se pueda arrastrar y cambiar de tamaño con Streamlit Elements

Streamlit Elements es un componente de terceros creado por [okld](https://github.com/okld) que le brinda las herramientas para crear hermosas aplicaciones y tableros con componentes de Material UI, Monaco editor (Visual Studio Code), Nivo charts , y más.

## Como usarlo?

### Instalación

El primer paso es instalar Streamlit Elements en su entorno:

```bash
pip install "streamlit-elements==0.1.*"
```

Se recomienda fijar la versión a `0.1.*`, ya que las versiones futuras pueden introducir cambios importantes en la API.

### Uso

Puede consultar [Streamlit Elements README](https://github.com/okld/streamlit-elements#getting-started) para obtener una instrucciones detalladas.

## Qué estamos construyendo?

El objetivo del desafío de hoy es crear un tablero compuesto por tres tarjetas de IU de material:

- Una primera tarjeta con Monaco editor para completar algunos datos;
- Una segunda tarjeta para mostrar esos datos en un gráfico Nivo Bump;
- Una tercera tarjeta para mostrar una URL de video de YouTube definida con `st.text_input`.

Puede usar los datos generados a partir de la demostración de Nivo Bump, en la pestaña 'datos': https://nivo.rocks/bump/.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-elements-demo/main)

## Código con explicación línea por línea

```python
# Primero, necesitaremos las siguientes librerias para nuestra aplicación.

import json
import streamlit as st
from pathlib import Path

# En cuanto a Streamlit Elements, necesitaremos todos estos objetos.
# Todos los objetos disponibles y su uso se enumeran aquí: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# Cambie el diseño de la página para que el tablero ocupe toda la página.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # Define URL for media player.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# Inicialice los datos predeterminados para el editor de código y el gráfico.
#
# Para este tutorial, necesitaremos datos para un gráfico Nivo Bump.
# Puede obtener datos aleatorios aquí, en la pestaña 'datos': https://nivo.rocks/bump/
#
# Como verá a continuación, este elemento de estado de sesión se actualizará cuando nuestro
# editor de código cambie, y el gráfico Nivo Bump lo leerá para dibujar los datos.

if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

# Defina un diseño de tablero predeterminado.
# La grilla tiene 12 columnas por defecto.
#
# Para obtener más información sobre los parámetros disponibles:
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    # El elemento del editor se coloca en las coordenadas x=0 e y=0, ocupa 6/12 columnas y tiene una altura de 3.
    dashboard.Item("editor", 0, 0, 6, 3),
    # El elemento del gráfico se coloca en las coordenadas x=6 e y=0, ocupa 6/12 columnas y tiene una altura de 3.
    dashboard.Item("chart", 6, 0, 6, 3),
    # El elemento multimedia se coloca en las coordenadas x=0 e y=3, ocupa 6/12 columnas y tiene una altura de 4.
    dashboard.Item("media", 0, 2, 12, 4),
]

# Crea un marco para mostrar elementos.

with elements("demo"):

    # Cree un nuevo panel con el diseño especificado anteriormente.
    #
    # draggableHandle es un selector de CSS que define la parte que se puede arrastrar de cada elemento del tablero.
    # Aquí, los elementos con un nombre de clase 'draggable' serán arrastrables.
    #
    # Para obtener más información sobre los parámetros disponibles:
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # Primera tarjeta, el editor de código.
        #
        # Utilizamos el parámetro `key` para identificar el elemento correcto
        #
        # Para hacer que el contenido de la tarjeta llene automáticamente la altura disponible, usaremos CSS flexbox.
        # sx es un parámetro disponible con cada componente de Material UI para definir atributos CSS.
        #
        # Para más información sobre Card, flexbox y sx:
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # Para hacer que este encabezado se pueda arrastrar, solo necesitamos establecer su nombre de clase en 'draggable',
            # como se definió anteriormente en dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Editor", className="draggable")

            # Queremos hacer que el contenido de la tarjeta tome toda la altura disponible configurando el valor de CSS flex en 1.
            # También queremos que el contenido de la tarjeta se reduzca cuando la tarjeta se encoja al establecer minHeight en 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Aquí está nuestro editor de código de Monaco.
                #
                # Primero, establecemos el valor predeterminado en st.session_state.data que inicializamos anteriormente.
                # Segundo, definimos el lenguaje a usar, JSON.
                #
                # Luego, queremos recuperar los cambios realizados en el contenido del editor.
                # Al verificar la documentación de Monaco, hay una propiedad onChange que toma una función.
                # Esta función se llama cada vez que se realiza un cambio, y el valor del contenido actualizado se pasa en
                # el primer parámetro (onChange: https://github.com/suren-atoyan/monaco-react#props)
                #
                # Streamlit Elements proveé una función especial sync(). Esta función crea un Callback y
                # automáticamente redirecciona sus parámetros al estado de sesión de Streamlit.
                #
                # Ejemplos
                # --------
                # Cree un Callback que reenvíe su primer parámetro a un elemento del estado de sesión llamado "data":
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # Cree un Callback que reenvíe su segundo parámetro a un elemento del estado de sesión llamado "ev":
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # Cree un Callback que reenvíe sus dos parámetros al estado:
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # Ahora, hay un problema: se llama a onChange cada vez que se realiza un cambio, lo que significa que cada vez
                # que escribe un solo carácter, toda su aplicación Streamlit se volverá a ejecutar.
                #
                # Para evitar este problema, puede decirle a Streamlit Elements que espere a que ocurra otro evento
                # (como un clic de botón) para enviar los datos actualizados, envolviendo su devolución de llamada con lazy().
                #
                # Para obtener más información sobre Monaco:
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # Monaco editor tiene un Lazy Callback atado al onChange, lo que significa que incluso si cambias
                # el contenido de Monaco, Streamlit no va a ser notificado directamente, lo que previene que se recargue todo el tiempo.
                # Entonces necesitamos otro evento para iniciar la actualización.
                #
                # La solución es crear un botón que dispare un Callback al hacer click.
                # 
                # Nuestro callback no necesita hacer nada en particular. Tu puedes incluso crear una
                # función vacía de Python, o utilizar sync() sin ningún argumento.
                #
                # Ahora, cada vez que hagas click en ese botón, el callback de onClick va a ser iniciado, pero
                # cualquier otro lazy callback que cambió va a ser también llamado. 

                mui.Button("Apply changes", onClick=sync())

        # Segunda tarjeta, el gráfico Nivo Bump.
        # Usaremos la misma configuración de flexbox que la primera tarjeta para ajustar automáticamente la altura del contenido.

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            # Para hacer que este encabezado se pueda arrastrar, solo necesitamos establecer su nombre de clase en 'draggable',
            # como se definió anteriormente en dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Chart", className="draggable")

            # Como arriba, queremos que nuestro contenido crezca y se reduzca a medida que el usuario cambia el tamaño de la tarjeta,
            # configurando flex en 1 y minHeight en 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Aquí es donde dibujaremos nuestro gráfico Bump.
                #
                # Para este ejercicio, podemos simplemente adaptar el ejemplo de Nivo y hacer que funcione con Streamlit Elements.
                # El ejemplo de Nivo está disponible en la pestaña 'code': https://nivo.rocks/bump/
                #
                # Los datos toman un diccionario como parámetro, por lo que necesitamos convertir nuestros datos JSON de una cadena a
                # un diccionario Python, con `json.loads()`.
                #
                # Para obtener más información sobre Nivo:
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

        # Tercer elemento del tablero, el reproductor multimedia.

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Este elemento funciona con ReactPlayer, es compatible con muchos otros reproductores
                # además de YouTube. Puedes verificarlo aquí: https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)

```

## Alguna pregunta?

No dude en hacer cualquier pregunta sobre Streamlit Elements o este desafío aquí: [Streamlit Elements Topic](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616)