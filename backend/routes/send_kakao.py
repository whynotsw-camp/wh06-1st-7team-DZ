from flask import Blueprint, request, jsonify
from services.kakao_api import send_kakao_message

kakao_bp = Blueprint('kakao', __name__)

@kakao_bp.route('/send_kakao', methods=['POST'])
def send_kakao():
    data = request.get_json()
    phone = data.get('phone')
    message = data.get('message')

    if not phone or not message:
        return jsonify({"success": False, "error": "phone 및 message 필수"}), 400

    result = send_kakao_message(phone, message)
    return jsonify(result)
