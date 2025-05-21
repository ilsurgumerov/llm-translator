import streamlit as st
import requests
from requests.exceptions import ConnectionError

# ip_api = "127.0.0.1"
ip_api = "cross-celling-api" # compose
port_api = "5000"


# Обновленные стили для тёмной темы
st.markdown("""
    <style>
    :root {
        --background: #000000; /* чёрный фон */
        --text: #f1f1f1;        /* светлый текст */
        --input-bg: #1a1a1a;    /* тёмный фон полей */
        --placeholder: #888888; /* светло-серый плейсхолдер */
    }

    /* Цвет текста и плейсхолдера внутри textarea */
    [data-baseweb="base-input"] textarea {
        color: var(--text) !important;
        font-size: 16px !important;
        background-color: var(--input-bg) !important;
    }

    [data-baseweb="base-input"] textarea::placeholder {
        color: var(--placeholder) !important;
        font-style: normal !important;
    }

    /* Оформление текстовых полей */
    .stTextArea [data-baseweb="base-input"] {
        background-color: var(--input-bg) !important;
        border: 1px solid #444 !important;
    }

    /* Disabled/readonly поля — яркий текст */
    .stTextArea [data-baseweb="base-input"][disabled],
    .stTextArea [data-baseweb="base-input"][aria-disabled="true"] {
        background-color: var(--input-bg) !important;
        color: var(--text) !important;
        opacity: 1 !important;
    }

    /* Делаем текст в disabled textarea таким же светлым */
    [data-baseweb="base-input"][disabled] textarea {
        color: var(--text) !important;
    }

    /* Стили для заголовков полей */
    label, .stTextArea label {
        color: var(--text) !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }

    body {
        color: var(--text);
        background-color: var(--background);
    }

    .block-container {
        padding: 2rem 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Инициализация состояния для вывода
if 'translation_result' not in st.session_state:
    st.session_state.translation_result = ""

st.title("🗺️ Многоязычный переводчик")

languages = [
    "английский",
    "французский",
    "немецкий",
    "испанский",
    "португальский",
    "китайский",
    "японский",
    "казахский",
    "башкирский"
]

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("### Язык")
    lang = st.selectbox(
        label="Выберите язык",
        options=languages,
        index=0,
        key="lang_select",
        label_visibility="collapsed"
    )

with col2:
    # Поле ввода
    input_text = st.text_area(
        label="Исходный текст",
        height=200,
        placeholder="Введите текст для перевода...",
        key="input_text"
    )
    
    # Кнопка перевода
    if st.button("Перевести", use_container_width=True):
        if not input_text:
            st.warning("Пожалуйста, введите текст для перевода")
        else:
            try:
                response = requests.post(
                    f"http://{ip_api}:{port_api}/translate",
                    json={"text": str(input_text), "language": str(lang)}
                )
                
                if response.status_code == 200:
                    result = response.json()
                    st.session_state.translation_result = result['original_text'].lower()
                else:
                    st.session_state.translation_result = f"Ошибка ({response.status_code})"
                
            except ConnectionError:
                st.error("Ошибка подключения к серверу")
    
    # Результат
    output_text = st.session_state.get("translation_result", "")

    st.text_area(
        label="Результат перевода",
        value=output_text,
        height=200,
        disabled=True,
        key="output_text"
    )
