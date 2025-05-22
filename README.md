# LLM Translator API & Web App

Этот проект предоставляет REST API и инструменты для перевода текстов с использованием крупных языковых моделей (LLM). Поддерживаются различные модели (OpenAI и другие) с настройкой параметров перевода.

---

## Содержание

- [Функционал](#функционал)
- [Установка](#установка)
- [Запуск](#запуск)
  - [FastAPI (Backend)](#fastapi-backend)
  - [Streamlit (Frontend)](#streamlit-frontend)
  - [Docker](#docker)
- [Формат запроса](#формат-запроса)
- [Поддерживаемые модели](#поддерживаемые-модели)
- [Конфигурация](#конфигурация)
- [Обратная связь](#обратная-связь)

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
    pip install -r requirements.txt
    ```
3. Создайте файл конфигурации
    ```bash
    cp config.example.yaml config.yaml
    ```

---

## Запуск

### FastAPI (Backend)

Запуск сервера:
```bash
python app_api.py
```

Сервер будет доступен по адресу: http://127.0.0.1:8000

Доступные эндпоинты:
- `GET /health`
- `GET /models`
- `POST /translate`

Пример запроса:
```bash
curl -X POST http://127.0.0.1:8000/translate \
     -H "Content-Type: application/json" \
     -d '{"text": "Привет, мир", "source_lang": "ru", "target_lang": "en", "model": "gpt-3.5-turbo"}'
```

### Streamlit (Frontend)

Запуск веб-приложения:
```bash
streamlit run web_app.py
```

Веб-интерфейс подключается к API по адресу `http://localhost:8501`.

---

### Docker

Для запуска через Docker:

Соберите образ:

```bash
docker build -t llm-translator .
```

Запустите контейнер:

```bash
docker run -p 8000:8000 -p 8501:8501 llm-translator
```

API будет доступно на порту 8000, веб-интерфейс на порту 8501.

---

## Формат запроса

Пример JSON для предсказания:
```json
{
  "text": "Текст для перевода",
  "source_lang": "ru",
  "target_lang": "en",
  "model": "gpt-3.5-turbo",
  "temperature": 0.7,
  "max_tokens": 1000
}
```

---

## Поддерживаемые модели
OpenAI: gpt-3.5-turbo, gpt-4

Другие модели (см. список через /models)

---

## Конфигурация

Создайте config.yaml в корне проекта:

```yaml
openai:
  api_key: "your_openai_key"
anthropic:
  api_key: "your_anthropic_key"
default_model: "gpt-3.5-turbo"
translation_params:
  temperature: 0.7
  max_tokens: 2000
```

---

## Обратная связь

Если вы нашли ошибку или у вас есть предложения по улучшению, создайте issue или pull request!
Вы также можете связаться с командой напрямую: **xxxxx@yandex.ru**