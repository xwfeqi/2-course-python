from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import json
import os

app = Flask(__name__)
NOTES_FILE = 'notes.json'
KEYS_FILE = 'secret.key'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    return {}

def load_keys():
    if os.path.exists(KEYS_FILE):
        with open(KEYS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file)

def save_keys(keys):
    with open(KEYS_FILE, 'w') as file:
        json.dump(keys, file)

@app.route('/add_note', methods=['POST'])
def add_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400
    
    key = Fernet.generate_key()
    cipher = Fernet(key)
    
    encrypted_content = cipher.encrypt(content.encode()).decode()
    
    notes = load_notes()
    keys = load_keys()

    notes[title] = encrypted_content
    keys[title] = key.decode()

    save_notes(notes)
    save_keys(keys)

    return jsonify({'message': 'Note added successfully'}), 201

@app.route('/get_note/<title>', methods=['GET'])
def get_note(title):
    notes = load_notes()
    keys = load_keys()

    if title not in notes:
        return jsonify({'error': 'Note not found'}), 404

    key = keys.get(title)
    if not key:
        return jsonify({'error': 'Encryption key not found'}), 404

    decrypt_code = request.args.get('code')
    if not decrypt_code:
        return jsonify({'error': 'Encryption code is required'}), 400
    
    if decrypt_code != key:
        return jsonify({'error': 'Invalid encryption code'}), 403

    cipher = Fernet(decrypt_code.encode())
    decrypted_content = cipher.decrypt(notes[title].encode()).decode()

    return jsonify({'title': title, 'content': decrypted_content}), 200

if __name__ == '__main__':
    app.run(debug=True)
