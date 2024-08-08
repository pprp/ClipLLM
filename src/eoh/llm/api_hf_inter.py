import http.client
import json
import requests
import torch


class InterfaceHF:
    """
    A class to interface with Hugging Face's API for model inference.

    Attributes:
        key (str): The API key for authentication.
        model_LLM (str): The name of the model to use for inference.
        debug_mode (bool): Flag to enable or disable debug mode.
    """

    def __init__(self, key, model_LLM, debug_mode):
        """
        Initialize the InterfaceHF instance.

        Args:
            key (str): The API key for authentication.
            model_LLM (str): The name of the model to use for inference.
            debug_mode (bool): Flag to enable or disable debug mode.
        """
        self.key = key
        self.model_LLM = model_LLM
        self.debug_mode = debug_mode

    def get_response(self, prompt_content):
        """
        Send a request to the Hugging Face API and get the response.

        Args:
            prompt_content (dict): The input prompt for the model.

        Returns:
            dict: The JSON response from the API.
        """
        API_URL = f"https://api-inference.huggingface.co/models/{self.model_LLM}"
        headers = {"Authorization": f"Bearer {self.key}"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        data = query(prompt_content)
        return data


if __name__ == "__main__":
    key = "XXX"
    model = "gpt2"
    hf = InterfaceHF(key, model, False)
    resp = hf.get_response({"inputs": "The answer to the universe is [MASK]."})
    print(resp)

    # from transformers import AutoTokenizer
    # import transformers
    # model = "meta-llama/Llama-2-7b-chat-hf"

    # tokenizer = AutoTokenizer.from_pretrained(model)
    # pipeline = transformers.pipeline(
    #     "text-generation",
    #     model=model,
    #     torch_dtype=torch.float16,
    #     device_map="auto",
    # )

    # sequences = pipeline(
    #     'Do you have any recommendations of other source to learn Evolving Algorithm or how to use HuggingFace I might like?\n',
    #     do_sample=True,
    #     top_k=10,
    #     num_return_sequences=1,
    #     eos_token_id=tokenizer.eos_token_id,
    #     max_length=200,
    # )
    # for seq in sequences:
    #     print(f"Result: {seq['generated_text']}")
