import pyperclip
from pynput import keyboard
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="gemma2:2b",  # required, but unused
)


def get_clipboard_content():
    return pyperclip.paste()


def set_clipboard_content(text):
    pyperclip.copy(text)


def summarize_text(text):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that summarizes text.",
        },
        {
            "role": "user",
            "content": f"Please summarize the following text concisely:\n\n{text}",
        },
    ]

    # try:
    if True:
        response = client.chat.completions.create(model="gemma2:2b", messages=messages)

        # Extract the summary from the response
        summary = response.choices[0].message.content
        return summary
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     return None


def on_press(key):
    try:
        if key == keyboard.Key.alt_l and keyboard.KeyCode.from_char("1"):
            # Get clipboard content
            clipboard_content = get_clipboard_content()
            print("Original clipboard content:", clipboard_content)

            # Summarize the content
            summary = summarize_text(clipboard_content)

            if summary:
                print("Summary:", summary)

                # Set the summary as the new clipboard content
                set_clipboard_content(summary)
                print("Summary has been copied to clipboard.")
            else:
                print("Failed to generate summary.")
    except AttributeError:
        pass


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
