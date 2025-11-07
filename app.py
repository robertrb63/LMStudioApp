import requests

url = "http://localhost:1234/v1/chat/completions"
headers = {"Content-Type": "application/json"}
data = {
    "model": "gpt-oss-safeguard-20b",  # Reemplaza con el nombre exacto del modelo cargado
    "messages": [{"role": "user", "content": "Hola, que modelo de IA tienes?"}],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])