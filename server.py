from flask import Flask, request, jsonify
import os

UPLOAD_FOLDER = '/workspace/yama_brain/data/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'Aucun fichier reçu'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'Fichier sans nom'}), 400

    save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(save_path)

    return jsonify({'status': f'Fichier enregistré : {file.filename}'}), 200

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')

    # TODO : appeler ici Yama localement avec le message
    response = f"(Réponse simulée) Tu as dit : {message}"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
