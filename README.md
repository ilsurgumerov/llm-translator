# LLM Translator API & Web App

Этот проект предоставляет REST API и инструменты для перевода текстов с использованием крупных языковых моделей (LLM)..

---

## Содержание

- [Пример перевода](#пример-перевода)
- [Функционал](#функционал)
- [Установка](#установка)
- [Запуск](#запуск)
  - [FastAPI (Backend)](#fastapi-backend)
  - [Streamlit (Frontend)](#streamlit-frontend)
  - [Docker](#docker)
- [Формат запроса](#формат-запроса)
- [Поддерживаемые модели](#поддерживаемые-модели)
- [Обратная связь](#обратная-связь)

---

## Пример перевода

![5d59923b-24de-486c-90a3-8042d734c0de](https://github.com/user-attachments/assets/1b71940e-c652-4131-a4e6-ea702eb817d3)

---

## Функционал

- `/translate` — перевод текста с настраиваемыми параметрами
- `/models` — список доступных моделей
- `/health` — проверка работоспособности API
- Веб-интерфейс для интерактивного перевода

---

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ilsurgumerov/llm-translator.git
   cd llm-translator
   ```
2. Установите зависимости:
    ```bash
    # Установка зависимостей
    pip install -r backend/requirements.txt
    pip install -r frontend/requirements.txt

    # Запуск backend
    python backend/app_api.py

    # Запуск frontend
    streamlit run frontend/streamlit_app.py
    ```

---

## Запуск

### FastAPI (Backend)

Запуск сервера:
```bash
python backend/app_api.py
```

Сервер будет доступен по адресу: `http://127.0.0.1:5000`.

Доступные эндпоинты:
- `GET /health`
- `GET /models`
- `POST /translate`

### Streamlit (Frontend)

Запуск веб-приложения:
```bash
streamlit run frontend/streamlit_app.py
```

Веб-интерфейс подключается к API по адресу `http://localhost:8501`.

---

### Docker

Для запуска через Docker небходимо поменять хост в коде

Сборка образов:

```bash
docker compose build
```

Запустите контейнер:

```bash
docker compose up -d
```

API будет доступно на порту 5000, веб-интерфейс на порту 8501.

---

## Формат запроса

Пример JSON для предсказания:
```json
{
  "text": "Текст для перевода",
  "lang_orig": "ru",
  "lang_target": "en"
}
```

---

## Поддерживаемые модели
- google/gemini-2.0-flash-exp:free
- deepseek/deepseek-chat-v3-0324:free    
- qwen/qwen3-235b-a22b:free
- meta-llama/llama-4-maverick:free

Можно смотреть через /models

---

## Обратная связь

Если вы нашли ошибку или у вас есть предложения по улучшению, создайте issue или pull request!
Вы также можете связаться с командой напрямую: **gumerovilsur1@gmail.com**
