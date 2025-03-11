from flask import Blueprint, request, jsonify
from app.services.openai_service import generate_image

bp = Blueprint('openai_api', __name__, url_prefix='/generate-image')

@bp.route('/', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', 'Un paisaje hermoso')
    image_url = generate_image(prompt)
    return jsonify({'image_url': image_url})