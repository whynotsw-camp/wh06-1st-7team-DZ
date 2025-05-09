import requests
import os

KAKAO_API_TOKEN = os.getenv("KAKAO_API_TOKEN")
KAKAO_TEMPLATE_ID = os.getenv("KAKAO_TEMPLATE_ID")

def send_kakao_message(phone_number, message_text):
    url = "https://kakaoapi.alimtalk.io/v1/send"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {KAKAO_API_TOKEN}"
    }

    payload = {
        "template_id": KAKAO_TEMPLATE_ID,
        "receiver": phone_number,
        "message": message_text
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}
