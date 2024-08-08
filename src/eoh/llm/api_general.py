import http.client
import json


class InterfaceAPI:
    """
    A class to interface with a general API for language model interactions.

    This class handles the communication with an API endpoint to send prompts
    and receive responses from a language model.

    Attributes:
        api_endpoint (str): The endpoint URL for the API.
        api_key (str): The authentication key for the API.
        model_LLM (str): The name or identifier of the language model to use.
        debug_mode (bool): Flag to enable or disable debug mode.
        n_trial (int): The maximum number of retry attempts for API calls.
    """

    def __init__(self, api_endpoint, api_key, model_LLM, debug_mode):
        """
        Initialize the InterfaceAPI instance.

        Args:
            api_endpoint (str): The endpoint URL for the API.
            api_key (str): The authentication key for the API.
            model_LLM (str): The name or identifier of the language model to use.
            debug_mode (bool): Flag to enable or disable debug mode.
        """
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.model_LLM = model_LLM
        self.debug_mode = debug_mode
        self.n_trial = 5

    def get_response(self, prompt_content):
        """
        Send a prompt to the API and get the response from the language model.

        This method handles the API communication, including retries on failure.

        Args:
            prompt_content (str): The prompt to send to the language model.

        Returns:
            str: The response from the language model, or None if all retries fail.
        """
        payload_explanation = json.dumps(
            {
                "model": self.model_LLM,
                "messages": [
                    # {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt_content}
                ],
            }
        )

        headers = {
            "Authorization": "Bearer " + self.api_key,
            "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
            "Content-Type": "application/json",
            "x-api2d-no-cache": 1,
        }

        response = None
        n_trial = 1
        while True:
            n_trial += 1
            if n_trial > self.n_trial:
                return response
            try:
                conn = http.client.HTTPSConnection(self.api_endpoint)
                conn.request(
                    "POST", "/v1/chat/completions", payload_explanation, headers
                )
                res = conn.getresponse()
                data = res.read()
                json_data = json.loads(data)
                response = json_data["choices"][0]["message"]["content"]
                break
            except:
                if self.debug_mode:
                    print("Error in API. Restarting the process...")
                continue

        return response
