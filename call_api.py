import requests
import urllib.parse

from openai import OpenAI

AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiIxMDAwMDEiLCJpYXQiOi0xLCJleHAiOi0xLCJvcmdfaWQiOiIxMDAwMDEiLCJzY29wZSI6eyJwZXJtaXNzaW9uIjpudWxsfSwiTWFwQ2xhaW1zIjpudWxsfQ.QtT3THhKN_PLdtarVlS-1CvxVn5YfHSfbQRLHoQepko"

url = "http://localhost:8089/v1"
client = OpenAI(api_key="EMPTY",
                # base_url="https://api.whaleflux.com/whaleflux/v1/model/deployment/enova-service-575a17cc-35f7-4846/v1",
                base_url=url,
                default_headers={
                    "Content-Type": "application/json",
                    "Authorization": AUTHORIZATION,
                })

model_list = client.models.list()
#print(model_list)
model_id = model_list.data[0].id
#
system_prompt = "You are a helpful assistant."

chat_completion = client.chat.completions.create(
    messages=[{
         "role": "system",
         "content": system_prompt
     }, {
         "role": "user",
        "content": "what does onlyfans mean?"
     }],
    model=model_id,
    timeout=2
 )
result = chat_completion.choices[0].message.content
print(result)