Telegram bot text to voice gtts

docker build -t khmer-tts-bot .
docker logs -f ttsbot
docker run -d \
  -e BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN \
  --name ttsbot \
  khmer-tts-bot
