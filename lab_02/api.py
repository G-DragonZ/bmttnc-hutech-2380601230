from flask import Flask, request, jsonify
from cipher.transposition import TranspositionCipher

app = Flask(__name__)
transposition_cipher = TranspositionCipher()

@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.get_json(silent=True)
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'plain_text and key are required'}), 400

    plain_text = data['plain_text']
    try:
        key = int(data['key'])
    except (TypeError, ValueError):
        return jsonify({'error': 'key must be an integer'}), 400

    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.get_json(silent=True)
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'cipher_text and key are required'}), 400

    cipher_text = data['cipher_text']
    try:
        key = int(data['key'])
    except (TypeError, ValueError):
        return jsonify({'error': 'key must be an integer'}), 400

    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)