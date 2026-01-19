from flask import Flask, render_template, request, send_from_directory, jsonify, url_for
import os
import uuid
from ai_utils import analyze_image, generate_story, text_to_speech

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
AUDIO_FOLDER = os.path.join(APP_ROOT, 'audio')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Save the image
        filename = str(uuid.uuid4()) + "_" + file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Analyze Image
        mood = analyze_image(filepath)

        # Generate Story
        story = generate_story(mood)

        # Generate Audio
        audio_filename = str(uuid.uuid4()) + ".mp3"
        audio_path = os.path.join(app.config['AUDIO_FOLDER'], audio_filename)
        text_to_speech(story, audio_path)

        return jsonify({
            'mood': mood,
            'story': story,
            'image_url': url_for('uploaded_file', filename=filename),
            'audio_url': url_for('serve_audio', filename=audio_filename)
        })

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(app.config['AUDIO_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
