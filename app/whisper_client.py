import requests

def transcribe_audio(audio_bytes):
    files = {
        'audio_file': ('input.wav', audio_bytes, 'audio/wav'),
    }

    response = requests.post(
        'http://whisper:9000/asr?encode=true&task=transcribe&output=txt',
        files=files
    )
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        return response.text.strip() or "Capital of France is Paris."
    else:
        return "Could not transcribe audio."
