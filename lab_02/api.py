from flask import Flask, request, jsonify
from cipher.playfair import PlayfairCipher

app = Flask(__name__)
playfair_cipher = PlayfairCipher()

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.get_json(silent=True)
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'plain_text and key are required'}), 400

    plain_text = data['plain_text']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.get_json(silent=True)
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'cipher_text and key are required'}), 400

    cipher_text = data['cipher_text']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)