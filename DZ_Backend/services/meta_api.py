import requests
import os

ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")

def get_instagram_insights(business_account_id):
    url = f"https://graph.facebook.com/v18.0/{business_account_id}/media"
    params = {
        "access_token": ACCESS_TOKEN,
        "fields": "caption,media_url,timestamp"
    }

    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
