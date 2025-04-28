from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
import io
from whisper_client import transcribe_audio
from llm_client import query_llm
from tts_client import synthesize_voice
from llm_client import query_with_text_rag

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/ask")
async def ask(file: UploadFile):
    audio_bytes = await file.read()
    question = transcribe_audio(audio_bytes)
    print(question)
    response = query_with_text_rag(question)
    print("...."+response)
    
    audio_output = synthesize_voice(response)
    return StreamingResponse(io.BytesIO(audio_output), media_type="audio/wav")
