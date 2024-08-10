import sys
import tkinter as tk
from tkinter import scrolledtext
from clipllm.llm.interface_LLM import InterfaceLLM


class ChatInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat with LLM")

        self.chat_area = scrolledtext.ScrolledText(
            master, state="disabled", wrap=tk.WORD
        )
        self.chat_area.pack(padx=10, pady=10)

        self.prompt_entry = tk.Entry(master, width=50)
        self.prompt_entry.pack(padx=10, pady=10)
        self.prompt_entry.bind("<Return>", self.send_prompt)

        self.send_button = tk.Button(master, text="Send", command=self.send_prompt)
        self.send_button.pack(padx=10, pady=10)

        self.llm = InterfaceLLM(
            api_endpoint="http://localhost:11434/v1",
            api_key="gemma2:2b",
            model_LLM="gemma2:2b",
            llm_use_local=True,
            llm_local_url="http://localhost:11434",
            debug_mode=True,
        )

    def send_prompt(self, event=None):
        user_input = self.prompt_entry.get()
        if user_input:
            self.chat_area.config(state="normal")
            self.chat_area.insert(tk.END, f"You: {user_input}\n")
            self.chat_area.config(state="disabled")
            self.prompt_entry.delete(0, tk.END)

            response = self.llm.get_response(user_input)
            self.chat_area.config(state="normal")
            self.chat_area.insert(tk.END, f"LLM: {response}\n")
            self.chat_area.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    chat_interface = ChatInterface(root)
    root.mainloop()
