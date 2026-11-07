# Crie um painel com itens que suportam Drag and Drop (arrastar e soltar) e redimensionáveis com o Streamlit Elements

O Streamlit Elements é um componente de terceiros feito por [okld](https://github.com/okld) que fornece as ferramentas para compor aplicações e painéis bonitos, com Material UI widgets, Monaco editor (Visual Studio Code), Nivo charts, e mais.

## Como usar?

### Instalação

O primeiro passo é instalar o Streamlit Elements em seu ambiente:

```bash
pip install "streamlit-elements==0.1.*"
```

É recomendado (para este tutorial) fixar a versão em `0.1.*`, pois versões futuras podem apresentar alterações de API importantes.

### Uso

Você pode acessar [Streamlit Elements README](https://github.com/okld/streamlit-elements#getting-started) para um guia de uso detalhado.

## O que vamos construir?

O objetivo do desafio de hoje é criar um painel composto por três cartões Material UI:

- Um primeiro card com um editor de código Monaco para inserir dados;
- Um segundo card para exibir esses dados em um gráfico Nivo Bump;
- Um terceiro card para mostrar uma URL de vídeo do YouTube com um `st.text_input`.

Você pode usar os dados gerados pela demonstração do Nivo Bump, na guia 'data': https://nivo.rocks/bump/.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-elements-demo/main)

## Código e Explicação linha por linha

```python
# Primeiro,vamos importar as bilbiotecas necessárias.

import json
import streamlit as st

# Para o Streamlit Elements, Vamos precisar dos seguintes objetos
# Todos os objetos e como usá-los estão disponíveis em: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# Altere o layout da página para que o painel ocupe a página inteira.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Dia 27 - Streamlit Elements")
    st.write("Crie um painel com itens que suportam Drag and Drop (arrastar e soltar) e redimensionáveis com o Streamlit Elements.")
    st.write("---")

    # Defina a URL para media player.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# Inicialize os dados padrões para o editor de código e gráfico.
#
# Para este tutorial, vamos precisar de dados para um gráfico Nivo Bump.
# Você pode obter dados aleatórios, na aba 'dados': https://nivo.rocks/bump/
#
# Como você pode ver abaixo, este item de estado de sessão será atualizado sempre que o nosso
# editor de código mudar, e será lido pelo gráfico do Nivo Bump para exibir os dados.

if "data" not in st.session_state:
    st.session_state.data = json.dumps([
        {"id": "Series 1", "data": [{"x": 2020, "y": 1}, {"x": 2021, "y": 2}, {"x": 2022, "y": 1}]},
        {"id": "Series 2", "data": [{"x": 2020, "y": 2}, {"x": 2021, "y": 1}, {"x": 2022, "y": 2}]},
    ], indent=2)

# Define o layout do painel padrão.
# O grid do painel tem 12 colunas por padrão.
#
# Para mais informações sobre os parâmetros:
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    # O Editor está posicionado com as coordenadas x=0 and y=0, e usa 6/12 colunas e tem uma altura de 3.
    dashboard.Item("editor", 0, 0, 6, 3),
    # O Gráfico está posicionado com as coordenadas x=6 and y=0, e usa 6/12 colunas e tem uma altura de 3.
    dashboard.Item("chart", 6, 0, 6, 3),
    # A Media está posicionado com as coordenadas x=0 and y=3, e usa 6/12 colunas e tem uma altura de 4.
    dashboard.Item("media", 0, 2, 12, 4),
]

# Cria um frame para exibir os elementos.

with elements("demo"):

    # Cria um novo painel com o layout especificado acima
    #
    # draggableHandle é um query selector do CSS para definir a parte arrastável de cada item do painel.
    # Elements com a classe 'draggable' serão arrastáveis.
    #
    # Para mais informações sobre os parâmetro do grid:
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # Primeiro card
        #
        # Utilizaremos o parâmetro 'key' para identificar o item no painel.
        #
        # para fazer os conteúdos do card, preencherem toda a altura disponível, vamos usar o CSS flexbox.
        # sx é um parãmetro disponível com todo widget do Material UI para definir atributos do CSS.
        #
        # Para mais informações sobre card, flexbox e sx:
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # Para fazer o cabeçalho arrastável, temos que definir a classname como 'draggable',
            # da mesma maneira que definimos acima no dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Editor", className="draggable")

            # Vamos fazer o conteúdo do card preencher toda a altura disponível, definindo o valor de flex para 1.
            # Mas também, queremos que o conteúdo possa encolher, então vamos definir o minHeight para 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Aqui está o nosso editor de código Monaco.
                #
                # Primeiro, vamos configurar o defaultValue para ser o st.session_state.data que foi inicializado acima
                # Segundo, vamos definir a language para ser JSON
                #
                # Então, vamos recuperar as mudanças feitas no conteúdo do editor
                # Verificando a documentação da Monaco UI, existe uma propriedade chamada onChange que serve para isso
                # Esta função é chamada toda vez que uma mudança é feita e o conteúdo atualizado é passado 
                # no primeiro parâmetro (onChange: https://github.com/suren-atoyan/monaco-react#props)
                #
                # Streamlit Elements possui uma função especial chamada sync(). Esta função cria uma chamada de retorno que vai
                # encaminhar automaticamente os parâmetros para os items do Streamlit session state.
                #
                # Exemplos
                # --------
                # Cria uma chamada de retorno que encaminha o primeiro parâmetro para um item do session state chamado "data":
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # Cria uma chamada de retorno que encaminha o segundo parâmetro para um item do session state chamado "ev":
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # Cria uma chamada de retorno que encaminha ambos os parâmetros para o session state:
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # Agora temos um problema: onChange é chamado toda vez que uma mudança é feita. Isso significa que toda vez
                # que você digita um caracter, toda sua aplicação Streamlit vai rodar novamente.
                #
                # Para evitar esse problema, você pode definir no Streamlit Element para que ele espere que outro evento aconteça
                # (por exemplo, um clique) para enviar os dados atualizados. Isso pode ser feito usando a função lazy().
                #
                # Para mais informações sobre os parâmetros do Monaco:
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # O editor Monaco tem a função lazy na chamada de retorno onChange, isto significa que mesmo que você altere
                # o conteúdo, o Streamlit não será notificado, logo não vai rodar novamente
                # Então, precisamos de uma evento sem a chamada lazy, para chamar a atualização
                #
                # A solução é criar um botão que faz a chamada de retorno quando clicado
                # A chamada de retorno não precisa fazer nada em especial. Você pode criar uma função vazia
                # ou usar sync() sem argumentos.
                #
                # Agora, toda vez que você clicar no botão a chamada onClick vai ser chamada, mas também
                # todas as chamadas lazy que tiveram alterações.

                mui.Button("Apply changes", onClick=sync())

        # Segundo card, o gráfico Nivo Bump chart.
        # Nós vamos usar o mesmo CSS flexbox, para ajustar a altura automaticamente

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            # Para fazer o cabeçalho arrastável, temos que definir a classname como 'draggable',
            # da mesma maneira que definimos acima no dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Chart", className="draggable")

            # Da mesma maneira que fizemos acima, vamos fazer o conteúdo do card preencher toda a altura disponível, definindo o valor de flex para 1.
            # Mas também, queremos que o conteúdo possa encolher, então vamos definir o minHeight para 0.
            
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Aqui vamos exibir o nosso gráfico Bump.
                #
                # Para este exercício, nós podemos adapatar o exemplo do Nivo e fazê-lo funcionar com Streamlit Elements.
                # O exemplo está disponível na aba 'code': https://nivo.rocks/bump/
                #
                # Data recebe um dicionário como parâmetro, então primeiro temos que converter o nosso JSON de string para 
                # um dicionário Python, com `json.loads()`.
                #
                # Para mais informações sobre outros gráficos Nivo disponíveis:
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

        # Terceiro elemento do Painel, o Media Player

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Este elemento utilizar o ReactPlayer, ele suporta outros player além do YouTube
                # Para mais informações: https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)

```

## Dúvidas?

Sinta-se à vontade para fazer qualquer pergunta sobre Streamlit Elements ou este desafio em: [Tópico do Streamlit Elements](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616)
