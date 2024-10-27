from flask import Flask, jsonify
from utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route('/score', methods=['GET'])
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()
        return jsonify({"score": score}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
