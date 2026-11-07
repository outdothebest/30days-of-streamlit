# Zbuduj pulpit z możliwością przeciągania i zmiany rozmiaru za pomocą Streamlit Elements

Streamlit Elements jest zewnętrznym komponentem stworzonym przez [okld](https://github.com/okld), który dostarcza narzędzi do budowania pięknych aplikacji i pulpitów z wykorzystaniem widżetów Material UI, edytora Monaco (Visual Studio Code), wykresów Nivo i więcej.

## Sposób użycia

### Instalacja

Pierwszym krokiem będzie zainstalowanie biblioteki Streamlit Elements w Twoim środowisku:

```bash
pip install "streamlit-elements==0.1.*"
```

Zalecamy przypiąć wersję do `0.1.*` ponieważ nowe wersje biblioteki mogą wprowadzić zmiany niekompatybilne z tym przykładem.

### Użycie

Może zajrzeć do pliku [Streamlit Elements README](https://github.com/okld/streamlit-elements#getting-started), aby uzyskać szczegółowe informacje na temat biblioteki.

## Co będziemy budować?

Celem dzisiejszej lekcji będzie stworzenie pulpitu złożonego z trzech komponentów Material UI:

- Pierwszy komponent będzie zawierał edytor kodu Monaco, aby móc wprowadzać dane;
- Drugi komponent będzie wyświetlał dane w postaci wykresu Nivo Bump;
- Trzeci komponent wyświetli wideo z portalu YouTube na podstawie adresu przekazanego poprzez `st.text_input`.

Możesz użyć danych wygenerowanych z demo Nivo Bump, w zakładce „dane”: https://nivo.rocks/bump/.

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-elements-demo/main)

## Wyjaśnienie działania, linijka po linijce

```python
# Na początku musimy zaimportować kilka bibliotek.

import json
import streamlit as st
from pathlib import Path

# Jeśli chodzi o Streamlit Elements, to będziemy potrzebowali wszystkich elementów zaimportowanych poniżej.
# Wszystkie dostępne elementy wraz z opisem użycia są udokumentowane tutaj: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# Zmieńmy układ strony tak, aby nasz pulpit wypełniał całą jej szerokość.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Dzień 27 - Streamlit Elements")
    st.write("Zbuduj pulpit z możliwością przeciągania i zmiany rozmiaru za pomocą Streamlit Elements.")
    st.write("---")

    # Zdefiniujmy adres URL dla odtwarzacza wideo.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# Zainicjalizujmy edytor kodu i wykres domyślnymi wartościami.
#
# Na potrzeby tej lekcji, będziemy używali danych z przykładowej aplikacji dla wykresu Nivo Bump.
# Możesz pobrać dane z zakładki 'data': https://nivo.rocks/bump/
#
# Jak zobaczymy poniżej, klucz 'data' w stanie sesji zostanie zaktualizowany, kiedy zmieni się kod w edytorze.
# Nowe dane zostaną odczytane przez wykres Nivo Bum, który się odświeży. 

if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

# Zdefiniujmy domyślne rozmieszczenie elementów na stronie.
# Domyślnie siatka pulpitu będzie się składać z 12 kolumn.
#
# Więcej informacji na temat dostępnych parametrów konfiguracji znajdziesz pod adresem:
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    
    # Komponent edytora jest umieszczony na współrzędnych x=0 i y=0, zajmuje 6/12 kolumn i ma wysokość 3 jednostek.
    dashboard.Item("edytor", 0, 0, 6, 3),
    # Komponent wykresu jest umieszczony na współrzędnych x=6 i y=0, zajmuje 6/12 kolumn i ma wysokość 3 jednostek.
    dashboard.Item("wykres", 6, 0, 6, 3),
    # Komponent wideo jest umieszczony na współrzędnych x=0 i y=3, zajmuje 6/12 kolumn i ma wysokość 4 jednostek.
    dashboard.Item("wideo", 0, 2, 12, 4),
]

# Tworzenie ramki do wyświetlania elementów

with elements("przykład"):

    # Stwórzmy nowy pulpit z elementami rozmieszczonymi według układu zdefiniowanego powyżej.
    #
    # draggableHandle jest zmienną definiującą które części aplikacji mogą być przeciągane.
    # W naszym przypadku wszystkie elementy posiadające klasę CSS o nawie 'draggable' będą mogły zmieniać pozycję.
    #
    # Po więcej informacji na temat dostępnych parametrów siatki pulpitu zajrzyj pod następujące adresy:
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # Pierwszy komponent, edytor kodu
        #
        # Używamy parametru 'key' aby móc odwołać się do właściwego elementu pulpitu.
        #
        # Aby treść komponentu automatycznie dostosowywała swoją wysokość, użyjemy modelu flexbox.
        # sx jest parametrem dostępnym dla każdego widżetu Material UI i służy do dodania atrybutów CSS.
        #
        # Po więcej informacji na temat komponentów flexbox oraz parametru sx zajrzyj tutaj:
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # Aby sprawić, że nagłówek również jest przeciągalny, należy dodać do niego klasę 'draggable',
            # podobnie jak to robiliśmy dla innych komponentów przy pomocy zmiennej draggableHandle.

            mui.CardHeader(title="Editor", className="draggable")

            # Chcemy, aby zawartość komponentu zajmowała całą dostępną wysokość, dlatego ustawiamy parametr flex na 1.
            # Ponadto chcemy, aby zawartość komponentu minimalizowała się, kiedy komponent jest zmniejszany ustawiając parametr minHeight to 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Tutaj definiujemy nasz edytor kodu Monaco.
                #
                # Po pierwsze, ustawiamy domyślną treść edytora na to, co aktualnie znajduje się w st.session_state.data
                # Po drugie, ustawiamy język edytora na JSON.
                #
                # Następnie chcemy pobrać zmiany dokonane w treści za pomocą edytora.
                # Po sprawdzeniu dokumentacji Monaco dowiadujemy się, że istnieje właściwość o nazwie onChange, która przyjmuje funkcję.
                #
                # Ta funkcja jest wywoływana, ilekroć dokonywana jest zmiana, a zaktualizowana treść jest przekazywana jako pierwszy parametr 
                # do naszej funkcji (zobacz: onChange: https://github.com/suren-atoyan/monaco-react#props)
                #
                # Biblioteka Streamlit Elements dostarcza specjalną funkcję sync(). Funkcja ta tworzy callback, który automatycznie przekazuje jej 
                # parametry do stanu sesji.
                #
                # Przykłady
                # --------
                # Stwórzmy callback, który przekazuje swój pierwszy parametr do stanu sesji, pod klucz o nazwie "data":
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # Stwórzmy callback, który przekazuje drugi parametr do stanu sesji, pod klucz o nazwie "ev"
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # Stwórzmy callback, który przekazuje oba swoje parametry do stanu sesji:
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # Teraz pojawia się problem: onChange jest wywoływany za każdym razem, kiedy zmienia się treść w edytorze.
                # To znaczy, że za każdym razem, kiedy w edytorze zostanie wpisany jakikolwiek znak, cała aplikacja zostaje uruchomiona w całości.
                #
                # Aby ominąć ten problem, musimy powiedzieć bibliotece Streamlit Elements, aby czekała na inne zdarzenie
                # (jak na przykład kliknięcie przycisku), zanim wyśle nowe dane. Można to zrobić poprzez opakowanie naszego callbacku w funkcję lazy()
                #
                # Po więcej informacji na temat parametrów dostępnych w Monaco, zajrzy tutaj:
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # Teraz kiedy nasz edytor ma "leniwy" callback przypisany do atrybutu onChange, to oznacza, że
                # nawet jeśli zmieni się treść w edytorze, Streamlit nie zostanie o tym powiadomiony od razu
                # i nie nastąpi ponowne uruchomienie pythonowego skryptu na serwerze.
                # W związku z tym potrzebujemy kolejnego zdarzenia, które zainicjuje aktualizację.
                #
                # Rozwiązaniem jest stworzenie przycisku, który będzie uruchamiał callback po kliknięciu.
                # Nasz nowy callback nie musi robić nic szczególnego. Możesz stworzyć pustą funkcję w Pythonie
                # albo użyć funkcji sync() bez żadnych argumentów.
                #
                # Po dodaniu przycisku, za każdym razem, kiedy go klikniemy, wywoła się jego callback
                # i wszystkie inne "leniwe" callbacki również zostaną wywołane.

                mui.Button("Zapisz zmiany", onClick=sync())

        # Drugi komponent, wykres Nivo Bump.
        # Użyjemy tej samej konfiguracji flexboxa co przy pierwszym komponencie, aby dostosować wysokość zawartości.

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            # Aby sprawić, że nagłówek również jest przeciągalny, należy dodać do niego klasę 'draggable',
            # podobnie jak to robiliśmy dla innych komponentów przy pomocy zmiennej draggableHandle.

            mui.CardHeader(title="Chart", className="draggable")

            # Tak jak powyżej, chemy sprawić, aby nasz komponent rozszerzał się i minimalizował, kiedy użytkownik zmienia rozmiar komponentu
            # Robimy to, ustwiając parametr flex na 1 oraz parametr minHeight na 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # To jest miejsce, w którym będziemy rysować nasz wykres.
                #
                # Na potrzeby tego ćwiczenia, możemy po prostu zaadoptować przykład wzięty ze strony Novo i sprawić,
                # że zadziała dobrze z biblioteką Streamlit Elements. Przykład, z którego korzystamy jest dostępny
                # w zakładce 'code' tutaj: https://nivo.rocks/bump/
                #
                # Parametr 'data' przyjmuje słownik, więc musimy przekształcić nasze dane ze stringa zawierającego dokument w formacie JSON
                # do słownika w Pythonie. Służy do tego funkcja `json.loads()`.
                #
                # Po więcej informacji na temat dostępnych wykresów Nivo, zajrzyj na:
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

        # Trzeci element naszego pulpitu, odtwarzacz wideo.

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Ten element jest stworzony przy użyciu komponentu ReactPlayer, wspiera on również wiele innych odtwarzaczy, nie tylko YouTube.
                # Możesz przeczytać o nim tutaj: https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)

```

## Zobacz też

Zachęcamy do zadawania pytań dotyczących biblioteki Streamlit Elements lub tej lekcji tutaj: [Streamlit Elements](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616)
