# This file includes classe to get response from deployed local LLM
import json
from typing import Collection
import requests


class InterfaceLocalLLM:
    """Language model that predicts continuation of provided source code.

    This class provides an interface to interact with a locally deployed language model
    for code completion tasks. It sends requests to a specified URL and processes the responses.

    Attributes:
        _url (str): The URL of the locally deployed language model API.

    Methods:
        get_response(content: str) -> str:
            Sends a request to the language model and returns the generated response.

        _do_request(content: str) -> str:
            Performs the actual HTTP request to the language model API.
    """

    def __init__(self, url):
        self._url = url  # 'http://127.0.0.1:11045/completions'

    def get_response(self, content: str) -> str:
        while True:
            try:
                response = self._do_request(content)
                return response
            except:
                continue

    def _do_request(self, content: str) -> str:
        content = content.strip("\n").strip()
        # repeat the prompt for batch inference (inorder to decease the sample delay)
        data = {
            "prompt": content,
            "repeat_prompt": 1,
            "params": {
                "do_sample": True,
                "temperature": None,
                "top_k": None,
                "top_p": None,
                "add_special_tokens": False,
                "skip_special_tokens": True,
            },
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(self._url, data=json.dumps(data), headers=headers)
        print(response)
        if response.status_code == 200:
            response = response.json()["content"][0]
            return response
