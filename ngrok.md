# How to local ollama in cursor

<https://www.youtube.com/shorts/zH-SmoD3_NQ>

Ollama settings:

```bash
launchctl setenv OLLAMA_HOST "0.0.0.0:11434"
```

```bash
ngrok http 11434 --host-header="localhost:11434"
```

in cursor:

```
url: https://a836-109-171-193-1.ngrok-free.app/v1

apikey: ollama
```
