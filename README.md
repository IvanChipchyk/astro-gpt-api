# AstroPublisher GPT API

🚀 FastAPI-сервер для генерации и записи гороскопов, готов к подключению с GPT.

## Возможности:
- Принимает POST-запросы с полями `sign` и `text`.
- Планируется интеграция с Google Sheets, ElevenLabs и YouTube API.

## Как использовать

1. Деплой на Render через GitHub.
2. Точка входа: `/upload-horoscope` (POST)
3. Формат запроса:
```json
{
  "sign": "Овен",
  "text": "Овен. 26 мая 2025 года..."
}
```

✅ Ответ:
```json
{ "message": "Гороскоп для Овен успешно добавлен." }
```
...
