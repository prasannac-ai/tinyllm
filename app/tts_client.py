import requests

def synthesize_voice(text: str):
    url = "http://tts:5002/api/tts"
    payload = {
        "text": text,
        "speaker_id": "p225",
        "model_name": "tts_models/en/vctk/vits",
        "language": "en"
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.content
        else:
            return b""
    except Exception as e:
        return b""
