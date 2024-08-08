import json
import requests
from openai import OpenAI


class InterfaceLocalLLM:
    """Interface for interacting with locally deployed language models.

    This class provides an interface to interact with locally deployed language models
    for various natural language processing tasks. It is designed to work with Ollama.

    Attributes:
        _client (OpenAI): The OpenAI client for Ollama interactions.

    Methods:
        get_response(content: str) -> str:
            Sends a request to the language model and returns the generated response.
        summarize(text: str) -> str:
            Summarizes the given text.
        translate_to_chinese(text: str) -> str:
            Translates the given English text to Chinese.
        polish(text: str) -> str:
            Polishes the given text to improve its quality.
        proofread(text: str) -> str:
            Proofreads the given text for errors.
    """

    def __init__(self, url, api_key):
        self._client = OpenAI(
            base_url=f"{url}/v1",
            api_key=api_key,  # required, but unused
        )

    def get_response(self, content: str) -> str:
        while True:
            try:
                response = self._do_ollama_request(content)
                return response
            except Exception as e:
                print(f"Error occurred: {e}. Retrying...")
                continue

    def _do_ollama_request(self, content: str) -> str:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": content,
            },
        ]

        # try:
        if True:
            response = self._client.chat.completions.create(
                model="gemma2:2b", messages=messages  # Adjust the model as needed
            )

            # Extract the summary from the response
            return response.choices[0].message.content.strip()
        # except Exception as e:
        #     print(f"An error occurred: {e}")
        #     return None

    def summarize(self, text: str) -> str:
        prompt = """
        Persona: You are a skilled summarizer with a talent for distilling complex information into concise, clear summaries.

        Steps:
        1. Read the given text carefully.
        2. Identify the main ideas and key points.
        3. Condense the information, removing unnecessary details.
        4. Create a coherent summary that captures the essence of the original text.
        5. Ensure the summary is clear, concise, and accurate.

        Example:
        Original: "The Industrial Revolution, which took place from the 18th to 19th centuries, was a period during which predominantly agrarian, rural societies in Europe and America became industrial and urban. Prior to the Industrial Revolution, which began in Britain in the late 1700s, manufacturing was often done in people's homes, using hand tools or basic machines. Industrialization marked a shift to powered, special-purpose machinery, factories and mass production."
        Summary: "The Industrial Revolution (18th-19th centuries) transformed agrarian societies in Europe and America into industrial ones. It shifted manufacturing from homes using hand tools to factories with powered machinery and mass production."

        Now, please summarize the following text:
        {text}
        """
        return self._do_ollama_request(prompt.format(text=text))

    def translate_to_chinese(self, text: str) -> str:
        prompt = """
        Persona: You are a bilingual expert in English and Chinese, skilled in translating between the two languages while preserving meaning and nuance.

        Steps:
        1. Read the English text carefully.
        2. Understand the context and meaning of the text.
        3. Translate the text into Chinese, ensuring accuracy and natural flow.
        4. Pay attention to idiomatic expressions and cultural nuances.
        5. Review the translation for clarity and correctness.

        Example:
        English: "The early bird catches the worm."
        Chinese: "早起的鸟儿有虫吃。" (Zǎo qǐ de niǎo er yǒu chóng chī.)

        Now, please translate the following English text to Chinese:
        {text}
        """
        return self._do_ollama_request(prompt.format(text=text))

    def polish(self, text: str) -> str:
        prompt = """
        Persona: You are a skilled editor with a keen eye for improving writing style, clarity, and impact.

        Steps:
        1. Read the given text thoroughly.
        2. Identify areas that can be improved in terms of clarity, conciseness, and style.
        3. Enhance the vocabulary and sentence structure where appropriate.
        4. Ensure consistency in tone and voice throughout the text.
        5. Refine the text to make it more engaging and impactful.

        Example:
        Original: "The meeting was long and boring. We talked about stuff."
        Polished: "The extensive meeting covered various topics, though it failed to maintain engagement throughout its duration."

        Now, please polish the following text:
        {text}
        """
        return self._do_ollama_request(prompt.format(text=text))

    def proofread(self, text: str) -> str:
        prompt = """
        Persona: You are a meticulous proofreader with an exceptional eye for detail and a deep understanding of grammar, punctuation, and spelling rules.

        Steps:
        1. Carefully read the given text.
        2. Check for and correct any spelling errors.
        3. Identify and fix grammatical mistakes.
        4. Ensure proper punctuation usage throughout the text.
        5. Verify consistency in formatting and style.
        6. Provide a clean, error-free version of the text along with a list of corrections made.

        Example:
        Original: "Their were alot of people at the party. Its was fun"
        Proofread: "There were a lot of people at the party. It was fun."
        Corrections: 
        - "Their" changed to "There"
        - "alot" changed to "a lot"
        - "Its" changed to "It"

        Now, please proofread the following text:
        {text}
        """
        return self._do_ollama_request(prompt.format(text=text))
