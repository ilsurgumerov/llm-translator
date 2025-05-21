'''
Шаг 1: Установка необходимых библиотек
Убедитесь, что у вас установлены необходимые библиотеки:
pip install fastapi uvicorn pydantic scikit-learn pandas

Шаг 2: Создание app_api.py
Шаг 3: Запустите ваше приложение: python app_api.py
Шаг 4: Тестирование API

Проверка работы API (/health)
curl -X GET http://127.0.0.1:5000/health
curl -X GET http://127.0.0.1:5000/stats
'''

from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

# Счетчик запросов
request_count = 0

# Определение доступных языков через Enum
class Language(str, Enum):
    english = "английский"
    french = "французский"
    german = "немецкий"

# Модель для входных данных
class TranslationRequest(BaseModel):
    text: str
    language: Language


@app.get("/stats")
def stats():
    return {"request_count": request_count}

@app.get("/health")
def health():
    return {"status": "OK"}


@app.post("/translate")
def translate(request: TranslationRequest):
    global request_count
    request_count += 1
    
    text = request.text.lower()
    lang = request.language.value
    
    return {
        "original_text": text,
        "translation": request.text,
        "language": lang,
        "found": True
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
    # uvicorn.run(app, host="127.0.0.1", port=5000)