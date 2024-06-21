import json
import random
import tkinter as tk
from tkinter import scrolledtext

# Load JSON data
with open('mental_health.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


categories = data['categories']

# Function to get a random greeting
def get_greeting():
    greetings = [
        "Hello! How can I help you today?",
        "Hi there! What can I assist you with?",
        "Welcome! How can I support you right now?"
    ]
    return random.choice(greetings)


def generate_response(user_input):
    user_input = user_input.lower()
    
    if 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
        return get_greeting()
    else:
        for category in categories:
            for question in category['questions']:
                if user_input in question['question'].lower():
                    return question['answer']
        

        return "I'm sorry, I don't quite understand. Could you please rephrase or ask something else?"


def send_message(event=None):
    user_input = user_input_field.get()
    if user_input.strip() != "":
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        response = generate_response(user_input)
        chat_window.insert(tk.END, "Bot: " + response + "\n\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        user_input_field.delete(0, tk.END)


root = tk.Tk()
root.title("Mental Health Companion")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_input_field = tk.Entry(root, width=100)
user_input_field.pack(padx=10, pady=10, fill=tk.X)
user_input_field.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, get_greeting() + "\n\n")
chat_window.config(state=tk.DISABLED)

root.mainloop()
