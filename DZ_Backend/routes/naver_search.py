from flask import Blueprint, request, jsonify
from services.naver_api import search_naver_shopping

naver_bp = Blueprint('naver', __name__)

@naver_bp.route('/naver_search', methods=['GET'])
def naver_search():
    query = request.args.get('query')

    if not query:
        return jsonify({"error": "검색어(query)가 필요합니다."}), 400

    result = search_naver_shopping(query)
    return jsonify(result)
