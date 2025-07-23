import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt: str) -> str:
    try:
        print("GPT 요청 시작:", prompt)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "친절한 한국어 조수입니다."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        print("GPT 응답 도착")
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"GPT 호출 실패: {str(e)}"

