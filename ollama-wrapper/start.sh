#!/bin/sh
ollama serve &
sleep 5
ollama pull llama3.2:3b
wait
