from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Horoscope(BaseModel):
    sign: str
    text: str

@app.post("/upload-horoscope")
def upload_horoscope(horoscope: Horoscope):
    # Здесь будет логика записи в Google Sheet (заглушка)
    return {"message": f"Гороскоп для {horoscope.sign} успешно добавлен."}