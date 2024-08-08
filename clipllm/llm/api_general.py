from openai import OpenAI
import json


class InterfaceAPI:
    """
    A class to interface with a general API for language model interactions.

    This class handles the communication with an API endpoint to send prompts
    and receive responses from a language model. Currently, only the DeepSeek API
    has been tested and verified to work with this interface.

    Attributes:
        api_endpoint (str): The endpoint URL for the API.
        api_key (str): The authentication key for the API.
        model_LLM (str): The name or identifier of the language model to use.
        debug_mode (bool): Flag to enable or disable debug mode.
        n_trial (int): The maximum number of retry attempts for API calls.

    Note:
        While designed to be general, this interface has only been tested with
        the DeepSeek API. Use with other APIs may require additional testing or modifications.
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
        self.client = OpenAI(base_url=self.api_endpoint, api_key=self.api_key)

    def get_response(self, prompt_content):
        """
        Send a prompt to the API and get the response from the language model.

        This method handles the API communication, including retries on failure.

        Args:
            prompt_content (str): The prompt to send to the language model.

        Returns:
            str: The response from the language model, or None if all retries fail.
        """
        response = None
        for _ in range(self.n_trial):
            try:
                chat_completion = self.client.chat.completions.create(
                    model=self.model_LLM,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt_content},
                    ],
                )
                response = chat_completion.choices[0].message.content.strip()
                break
            except Exception as e:
                if self.debug_mode:
                    print(f"Error in API: {e}. Retrying...")
                continue

        return response
