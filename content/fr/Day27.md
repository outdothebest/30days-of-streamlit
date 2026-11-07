# Créez un dashboard redimensionable avec Streamlit Elements

Streamlit Elements est une extension pour Streamlit créée par [okld](https://github.com/okld). Elle vous permet de construire des applications allant de simples formulaires à des dashboard redimensionables, avec Material UI, l'éditeur de code Monaco, des graphiques Nivo, et bien plus encore !

## Guide d'installation et d'utilisation

### Installation

Commencez par installer Streamlit Elements dans votre environnement Python :

```python
pip install "streamlit-elements==0.1.*"
```

Il est recommandé de fixer la version à `0.1.*`. L'extension étant encore à ses débuts, les versions ultérieures pourront introduire des changements d'API incompatibles avec les versions précédentes. 

### Utilisation

Vous pouvez vous référer au README [sur la page GitHub de Streamlit Elements](https://github.com/okld/streamlit-elements#getting-started), toutes les fonctionnalités de l'extension y sont décrites.

## Qu'allons nous créer ?

L'objectif de l'application d'aujourd'hui est de créer un dashboard composé de trois fenêtres :

- Une fenêtre d'édition de code avec Monaco pour pouvoir y écrire des données ;
- Une deuxième fenêtre pour afficher ces données avec un graphique Nivo ;
- Un lecteur YouTube qui lira une URL définie avec un `st.text_input`.

Pour cette application, vous pouvez récupérer des données d'exemple depuis la documentation de Nivo, dans l'onglet `data`: https://nivo.rocks/bump/.

## Démo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-elements-demo/main)

## Code source commenté

```python
# Commençons par importer les bibliothèques que nous utiliserons (hors Streamlit Elements).

import json
import streamlit as st

# Voici les imports de Streamlit Elements dont nous aurons besoin.
# Vous pouvez retrouver une description détaillée de chaque élément ici:
# https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# Configuration de la page Streamlit pour que le dashboard prenne toute la largeur de l'écran.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # URL par défaut pour le lecteur YouTube.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# Initialisation des données par défaut à afficher dans l'éditeur de code.
#
# Pour ce tutoriel, nous allons utiliser un graphique Nivo de type 'Bump'.
# Vous pouvez trouver des exemples de données ici, onglet 'data': https://nivo.rocks/bump/
#
# Nous allons stocker ces données dans le session state de Streamlit.
# A chaque fois que nous éditerons ces données depuis l'éditeur de code, 
# le graphique les récupèrera et les affichera.

if "data" not in st.session_state:
    st.session_state.data = json.dumps([
        {"id": "Series 1", "data": [{"x": 2020, "y": 1}, {"x": 2021, "y": 2}, {"x": 2022, "y": 1}]},
        {"id": "Series 2", "data": [{"x": 2020, "y": 2}, {"x": 2021, "y": 1}, {"x": 2022, "y": 2}]},
    ], indent=2)

# Disposition des fenêtre du dashboard.
# Les éléments du dashboard sont disposés sur une grille de 12 colonnes par défaut.
#
# Pour plus d'information sur les paramètres disponibles:
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    # L'éditeur de code est positionnée aux coordonnées x=0 et y=0,
    # avec une largeur de 6 colonnes sur 12, et a une hauteur de 3 unités.
    dashboard.Item("editor", 0, 0, 6, 3),
    # Le graphique est positionnée aux coordonnées x=6 et y=0,
    # avec une largeur de 6 colonnes sur 12, et a une hauteur de 3 unités.
    dashboard.Item("chart", 6, 0, 6, 3),
    # Le lecteur vidéo est positionnée aux coordonnées x=0 et y=2,
    # prend toute la largeur de l'écran, et a une hauteur de 4 unités.
    dashboard.Item("media", 0, 2, 12, 4),
]

# Zone d'affichage pour Streamlit Elements.

with elements("demo"):

    # Création du dashboard avec la disposition des éléments spécifiée ci-dessus.
    #
    # draggableHandle est une propriété du dashboard qui prend un query selector CSS.
    # Ce sélécteur CSS définit les éléments qui permettront à l'utilisateur de déplacer
    # les fenêtres. Pour cette démo, ce seront les barres de titre de chaque fenêtre.
    #
    # Pour plus d'information sur les paramètres du dashboard:
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # Première fenêtre, l'éditeur de code.
        #
        # Le paramètre 'key' permet d'associer un élément à une des 3 dispositions
        # définies plus haut dans 'layout'.
        #
        # Pour nous assurer que l'éditeur prenne toute la hauteur de la fenêtre, nous allons
        # utiliser des flexbox CSS. Le paramètre 'sx' disponible sur tous les éléments de
        # de Material UI permet de définir des attributs CSS.
        #
        # Pour plus d'information sur les flexbox CSS, le paramètre sx et les Card de Material UI:
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # Pour pouvoir déplacer la fenêtre, nous allons ajouter à l'en-tête de cette Card
            # (la barre de titre) la classe CSS "draggable", qui est définie dans le draggableHandle
            # du dashboard.Grid plus haut.

            mui.CardHeader(title="Editor", className="draggable")

            # Nous allons indiquer que le contenu de la fenêtre prenne toute la hauteur possible
            # avec l'attribut CSS "flex" à 1. "minHeight" est nécessaire pour que le contenu
            # puisse se réduire. Sans ça, agrandir puis réduire la fenêtre ne réduira pas le
            # contenu.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # L'éditeur de code Monaco. Voici les paramètres que nous passons:
                #
                # 1. La valeur par défaut de l'éditeur correspond aux données d'entrée
                #    sauvegardées dans le session state 'data'.
                # 
                # 2. Les données d'entrée sont au format JSON. Nous définissons la langue
                #    de l'éditeur en conséquence.
                #
                # 3. Lorsque l'utilisateur change les données dans l'éditeur, nous voulons
                #    mettre à jour les graphiques Nivo en conséquence. Pour ce faire, nous
                #    allons passer une fonction au paramètre 'onChange', qui sera appelée à
                #    chaque fois que le contenu de l'éditeur changera.
                #
                #    Le contenu mis à jour correspond au 1e argument de la fonction, comme
                #    l'indique la documentation: https://github.com/suren-atoyan/monaco-react#props
                #    
                #    > Signature: function(value: string | undefined, ev: ...) => void
                #                          ^^^^^^^^^^^^^^^^^^^^^^^^^
                #    La fonction que nous allons passer à 'onChange' recevra donc le nouveau
                #    contenu de l'éditeur en 1e paramètre.
                #    
                # Streamlit Elements met à disposition une fonction spéciale: sync()
                # Elle va retourner une fonction qui va automatiquement mettre à jour
                # le session state de Streamlit.
                #    
                # Exemple
                # -------
                # Création d'une fonction qui va assigner le 1e paramètre de 'onChange' à
                # l'entrée 'data' du session state:
                #
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # Création d'une fonction qui va assigner le 2e paramètre de 'onChange' à
                # l'entrée 'ev' du session state:
                #
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # Création d'une fonction qui va assigner le 1e et le 2e paramètre de 'onChange'
                # respectivement à 'data' et 'ev': 
                #
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # Un autre problème se pose désormais: à chaque changement d'un seul caractère,
                # onChange est appelé, ce qui déclenche une ré-exécution de toute l'application
                # Streamlit.
                #
                # Pour éviter ces ré-exécutions intempestives, nous allons utiliser la fonction
                # lazy() qui indique à Streamlit Elements que cette fonction ne doit pas être
                # appelée à chaque changement.
                # Ainsi, Streamlit Elements attendra un autre événement qui n'utilise pas lazy()
                # pour appeler toutes les autres fonctions lazy.
                #
                # Un exemple d'événement non-lazy: un clic bouton sur un élément mui.Button auquel
                # on aurait défini le paramètre 'onClick'. Ce sera implémenté ci-dessous.
                #
                # Pour plus d'information sur les paramètres de Monaco:
                # - https://github.com/suren-atoyan/monaco-react
                # - https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # Nous avons passé à Monaco une fonction lazy à onChange. Notre application
                # Streamlit n'est donc pas notifiée par défaut lorsque le contenu change.
                # 
                # Nous avons donc besoin d'un autre événement non-lazy pour déclencher une
                # mise à jour de Streamlit, par exemple, un clic de bouton.
                #
                # Nous allons utiliser sync() sans argument car nous ne sommes pas intéressé
                # par les paramètres de la fonction onClick. Nous cherchons juste à déclencher
                # une mise à jour de Streamlit.
                #
                # Ainsi, lorsque nous cliquerons sur ce bouton, toutes les fonctions lazy se 
                # déclencherons également.

                mui.Button("Apply changes", onClick=sync())

        # Deuxième fenêtre, notre graphique Nivo.
        #
        # Nous allons utiliser le même principe de flexbox qu'avec la 1e fenêtre pour que le
        # contenu puisse s'ajuster sur la hauteur.

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            # Comme la 1e fenêtre, nous attribuons le nom de classe CSS 'draggable' à la barre
            # de titre pour que l'utilisateur puisse la saisir avec la souris et déplacer
            # la fenêtre sur le dashboard.

            mui.CardHeader(title="Chart", className="draggable")

            # Même chose que la 1e fenêtre, flex à 1 et minHeight à 0 pour que le contenu
            # puisse prendre toute la hauteur à sa disposition, et puisse réduire sa hauteur.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Le graphique Nivo.
                #
                # Pour cette application, nous pouvons tout simplement aller sur le site de Nivo
                # et adapter un exemple Javascript en Python. La documentation se trouve ici, 
                # onglet 'code' : https://nivo.rocks/bump/
                #
                # Le 1e paramètre 'data' prend les données en format JSON. Nous devons donc
                # convertir nos données avec 'json.loads()'.
                #
                # Pour plus d'information sur les graphiques Nivo:
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

        # Troisième fenêtre, le lecteur de vidéo YouTube.

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Cet élément utilise React-player, qui supporte de nombreux lecteurs autre que
                # YouTube. Pour plus d'informations: https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)

```

## Des questions?

N'hésitez pas à poser vos questions en rapport avec ce challenge ou Steamlit Elements sur le forum : [Topic Streamlit Elements](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616)
