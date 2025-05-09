from flask import Blueprint, request, jsonify
from services.openai_api import generate_ai_message

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/recommend', methods=['POST'])
def recommend_message():
    data = request.get_json()
    product = data.get('product')
    tone = data.get('tone', '친근하게')

    if not product:
        return jsonify({"success": False, "error": "product 필드가 필요합니다."}), 400

    result = generate_ai_message(product, tone)
    return jsonify({"success": True, "recommended_message": result})