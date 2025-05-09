import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_message(product, tone="친근하게"):
    prompt = f"{tone} 톤으로 '{product}' 제품을 홍보할 마케팅 문구를 작성해줘."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"문구 생성 중 오류 발생: {str(e)}"