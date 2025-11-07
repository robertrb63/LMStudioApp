import tkinter as tk
from tkinter import ttk
import requests

# Configuración de la API local de LM Studio
API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_ID = "qwen3-4b-valiant-polaris"

# Función para enviar la pregunta y mostrar la respuesta
def enviar_pregunta():
    pregunta = entrada_usuario.get()
    if not pregunta.strip():
        return

    data = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": pregunta}],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers={"Content-Type": "application/json"}, json=data)
        respuesta = response.json()["choices"][0]["message"]["content"]
        salida_texto.config(state="normal")
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, respuesta)
        salida_texto.config(state="disabled")
    except Exception as e:
        salida_texto.config(state="normal")
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, f"Error: {e}")
        salida_texto.config(state="disabled")

# Crear ventana 

style = ttk.Style()
style.theme_use("clam")  # Tema moderno

style.configure("TLabel", font=("Segoe UI", 14, "bold"), background="#e6f2ff", foreground="#003366")
style.configure("TEntry", font=("Segoe UI", 14))
style.configure("TButton", font=("Segoe UI", 14), padding=8)
ventana = tk.Tk()
ventana.title("🤖 LM Studio Chat")
ventana.geometry("600x400")
ventana.configure(bg="#f0f4f8")

ventana.configure(bg="#e6f2ff")  # Fondo azul claro


# Estilo moderno
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 12), padding=6)
style.configure("TLabel", font=("Segoe UI", 12), background="#f0f4f8")
style.configure("TEntry", font=("Segoe UI", 12))

# Etiqueta
ttk.Label(ventana, text="Escribe tu pregunta para el modelo:").pack(pady=10)

# Entrada de texto

ttk.Label(
    ventana,
    text="💬 ¿Qué quieres preguntarle a la inteligencia artificial?",
    style="TLabel",
    anchor="center",
    justify="center"
).pack(pady=15)


entrada_usuario = ttk.Entry(ventana, width=80)
entrada_usuario.pack(pady=5)

# Botón
ttk.Button(ventana, text="Enviar", command=enviar_pregunta).pack(pady=10)

# Área de salida
salida_texto = tk.Text(ventana, wrap="word", font=("Segoe UI", 11), bg="#ffffff", fg="#333333", height=10)
salida_texto.pack(padx=20, pady=10, fill="both", expand=True)
salida_texto.config(state="disabled")

# Ejecutar la app
ventana.mainloop()