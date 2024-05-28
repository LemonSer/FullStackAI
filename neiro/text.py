import requests
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '7138631637:AAEnYvqdaFaAFz7ehzjnzEyo6RqK978pCAE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def get_response(message_text):
  prompt = {
    "modelUri": "gpt://b1go1t8vie998tqjdjhu/yandexgpt-lite",
    "completionOptions": {
      "stream": False,
      "temperature": 0.3,
      "maxTokens": "2000"
    },
    "messages": [
      {
        "role": "system",
        "text": "Ты - нейронная сеть которая помогает улучшать промт. Ты получаешь сообщение от пользователя и улучшаешь промт придумав ему одно крутое название"
  },
      {
        "role": "user",
        "text": message_text
      }
    ]
  }

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
    "Content-Type": "application/json",
    "Authorization": "API-Key AQVN0pDgU51dizMQvGEQnOj4ce4BPJyMBxzdRm9P"
  }

  response = requests.post(url, headers=headers, json=prompt)
  result = response.json()
  magic =  result['result']['alternatives'][0]['message']['text']
  return magic

