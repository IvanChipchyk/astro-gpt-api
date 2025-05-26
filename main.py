from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Horoscope(BaseModel):
    sign: str
    text: str

@app.post("/upload-horoscope")
def upload_horoscope(horoscope: Horoscope):
    return {"message": f"Гороскоп для {horoscope.sign} успешно добавлен."}

@app.post("/generate-daily")
def generate_daily():
    return {"message": "Сгенерированы гороскопы на день."}

@app.post("/generate-weekly")
def generate_weekly():
    return {"message": "Сгенерированы недельные Shorts."}

@app.post("/generate-monthly")
def generate_monthly():
    return {"message": "Сгенерированы месячные Shorts."}

@app.post("/generate-monthly-video")
def generate_monthly_video():
    return {"message": "Сгенерирован длинный текст для видео."}
