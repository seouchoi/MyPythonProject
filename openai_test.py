import os
import openai
openai.api_key = "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"

INSTRUCTIONS = ["1. summarize the sentences", "2. give me core word"]
system_instruction = "\n".join(["""You will be provided with many sentences, and your task is to summarize these sentences as follows.
                                Also, if the input sentence is in Korean, provide a summary sentence and its keywords in Korean as well.""", *INSTRUCTIONS])

msg = """12월 12일 경기도에서 화재가 발생했다. 화재의 발생원인은 담배꽁초의 무단투기로 인해 발생했고 주변에 마른 낙엽이 수북히 쌓여있어 불길이 낙엽 더미에 옮겨붙어서 화재의 크기가 더욱 커졌다. 
         화재 발생 12시간이 지난 뒤에서야 모든 불길이 진압되었고 진압 과정에서 소방 헬기 2대와 소방차 20대가 모여서 마지막 남은 불씨까지 끌 수 있었다."""
response = openai.ChatCompletion.create(
  model="gpt-4", #모델 지정
  messages = [{"role":"system", "content": f"{system_instruction}"},
      {"role": "user", "content": f"{msg}"}],
  temperature=0,
)

print(response.choices[0].message.content)