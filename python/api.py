from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import tensorflow as tf

app = Flask(__name__)

# Carregar o modelo previamente treinado
model = tf.keras.models.load_model('trabalho-cop-30\python\model_trained.keras')
# Função para preparar a imagem
def prepare_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = np.array(image) / 255.0  # Normaliza a imagem
    image = np.expand_dims(image, axis=0)  # Adiciona uma dimensão para batch
    return image

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    try:
        image = Image.open(file.stream)
        prepared_image = prepare_image(image, target_size=(224, 224))  # Use o tamanho apropriado

        # Fazer a previsão
        predictions = model.predict(prepared_image)
        predicted_class = np.argmax(predictions, axis=1)

        return jsonify({'class_id': int(predicted_class[0]), 'confidence': float(np.max(predictions))})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
