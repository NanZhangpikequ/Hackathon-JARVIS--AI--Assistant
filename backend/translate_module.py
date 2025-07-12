import requests

# Hardcoded DeepL API Key
DEEPL_API_KEY = ""  # TODO: Replace with your actual DeepL key

def detect_language(text):
    # Uses DeepL to detect source language
    url = "https://api.deepl.com/v2/translate"
    params = {
        'auth_key': DEEPL_API_KEY,
        'text': text,
        'target_lang': 'EN'
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        return response.json()['translations'][0]['detected_source_language']
    else:
        raise Exception("Language detection failed")

def translate_text(text, target_lang, source_lang):
    # Uses DeepL to translate text from source_lang to target_lang
    url = "https://api.deepl.com/v2/translate"
    params = {
        'auth_key': DEEPL_API_KEY,
        'text': text,
        'target_lang': target_lang,
        'source_lang': source_lang
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        return response.json()['translations'][0]['text']
    else:
        raise Exception("Translation failed")
