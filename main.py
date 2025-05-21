from llama_cpp import Llama
from config import MODEL_PATH
import tkinter as tk
from tkinter import scrolledtext

# Initialize the model
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,           # Context size (reduce to 1024 if low RAM)
    n_threads=4,          # CPU threads (adjust based on your CPU)
    n_gpu_layers=20       # Offload to GPU (set to 0 if no GPU)
)

# Simple GUI
def start_gui():
    root = tk.Tk()
    root.title("Varnx - Offline")
    
    chat_window = scrolledtext.ScrolledText(root, width=80, height=25)
    chat_window.pack(pady=10)
    
    entry = tk.Entry(root, width=70)
    entry.pack(pady=5)
    
    def send():
        user_input = entry.get()
        chat_window.insert(tk.END, f"You: {user_input}\n")
        entry.delete(0, tk.END)
        
        # Generate response
        output = llm.create_chat_completion(
            messages=[{"role": "user", "content": user_input}],
            max_tokens=512,
            temperature=0.7
        )
        response = output['choices'][0]['message']['content']
        chat_window.insert(tk.END, f"Varnx: {response}\n\n")
    
    tk.Button(root