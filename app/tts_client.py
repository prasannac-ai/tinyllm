import requests


def synthesize_voice(text: str):
    url = "http://tts:5002/api/tts"  

    try:
     
        response = requests.post(url, data=text.encode('utf-8'), headers={'Content-Type': 'text/plain'})
        if response.status_code == 200:
            return response.content  
        else:
            print(f"Error: Received status code {response.status_code}")
            return b""
    except Exception as e:
        print(f"Exception occurred: {e}")
        return b""
