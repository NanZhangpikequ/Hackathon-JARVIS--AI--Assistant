from flask import Flask, request, jsonify
from gpt_module import chat_with_gpt
from translate_module import detect_language, translate_text
from speech_module import recognize_audio
import os

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # Accepts JSON with user text and returns GPT reply (translated back)
    data = request.get_json()
    user_input = data.get("text", "")
    if not user_input:
        return jsonify({"error": "No input"}), 400

    try:
        source_lang = detect_language(user_input)
        translated = translate_text(user_input, "EN", source_lang)
        gpt_reply = chat_with_gpt(translated)
        reply_translated = translate_text(gpt_reply, source_lang, "EN")
        return jsonify({"reply": reply_translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/voice', methods=['POST'])
def voice():
    # Accepts an uploaded audio file and returns transcribed text
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    audio_file = request.files['file']
    filepath = "temp_audio.wav"
    audio_file.save(filepath)
    try:
        text = recognize_audio(filepath)
        os.remove(filepath)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)