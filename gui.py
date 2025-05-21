import tkinter as tk
from tkinter import scrolledtext

def start_gui(llm):
    def send_input():
        user_input = user_entry.get()
        chat_window.insert(tk.END, f"You: {user_input}\n")
        user_entry.delete(0, tk.END)
        output = llm(user_input, max_tokens=512)
        response = output["choices"][0]["text"]
        chat_window.insert(tk.END, f"Varnx: {response}\n\n")

    root = tk.Tk()
    root.title("Varnx - Your Offline Coding Assistant")

    chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    chat_window.pack(padx=10, pady=10)

    user_entry = tk.Entry(root, width=70)
    user_entry.pack(padx=10, pady=(0, 10))

    send_button = tk.Button(root, text="Send", command=send_input)
    send_button.pack()

    root.mainloop()
