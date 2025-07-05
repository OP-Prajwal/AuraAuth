from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from moviepy import VideoFileClip
import os
import librosa
import numpy as np
from werkzeug.utils import secure_filename
import tensorflow as tf

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


model = tf.keras.models.load_model('audio_classifier.h5')


os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_features(file_path):
    audio, sr = librosa.load(file_path)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    mfcc = np.mean(mfcc.T, axis=0)
    return np.expand_dims(mfcc, axis=0)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file found"}), 400

    file = request.files['file']

    if file.filename == "":
        return jsonify({"message": "No file selected"}), 400

    if file:
   
        filename = secure_filename(file.filename)
        video_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(video_path)

      
        audio_path = os.path.join(UPLOAD_FOLDER, filename.split('.')[0] + ".mp3")
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)

        return jsonify({
            "message": "File uploaded successfully",
            "audio_path": audio_path
        }), 200
    else:
        return jsonify({"message": "File upload failed"}), 400

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    audio_path = data.get('audio_path')

    if not audio_path:
        return jsonify({'error': 'Audio path not provided'}), 400

   
    features = extract_features(audio_path)

    
    prediction = model.predict(features)
    
  
    print(prediction)
    human_prob = float(prediction[0][0])  
    ai_prob = float(prediction[0][1])     
    
   
    print(f"Debug - Raw prediction: {prediction}")
    print(f"Debug - Human probability: {human_prob:.4f}")
    print(f"Debug - AI probability: {ai_prob:.4f}")

  
    if human_prob > ai_prob:
        result = 'Human'
        confidence = round(human_prob * 100, 2)
    else:
        result = 'AI-Generated'
        confidence = round(ai_prob * 100, 2)

   
    return jsonify({
        'prediction': result,
        'confidence': f'{confidence}%',
        'probabilities': {
            'human': f'{human_prob:.2%}',
            'ai': f'{ai_prob:.2%}'
        },
        'audio_url': f'http://localhost:5000/audio/{audio_path.split("/")[-1]}'
    })

@app.route('/audio/<filename>')
def get_audio(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
