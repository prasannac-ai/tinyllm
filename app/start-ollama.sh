#!/bin/sh

echo "Pulling model: tinyllama"
ollama pull tinyllama

echo "Starting Ollama API server"
exec ollama serve