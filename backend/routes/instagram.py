from flask import Blueprint, request, jsonify
from services.meta_api import get_instagram_insights

insta_bp = Blueprint('insta', __name__)

@insta_bp.route('/instagram_feed', methods=['GET'])
def instagram_feed():
    account_id = request.args.get('account_id')

    if not account_id:
        return jsonify({"error": "account_id가 필요합니다."}), 400

    result = get_instagram_insights(account_id)
    return jsonify(result)