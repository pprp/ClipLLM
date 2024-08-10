from ..llm.api_general import InterfaceAPI
from ..llm.api_local_llm import InterfaceLocalLLM


class InterfaceLLM:
    """
    A class that provides an interface for interacting with different Language Learning Models (LLMs).

    This class can handle both local and remote LLM deployments. It initializes the appropriate
    interface based on the provided configuration and offers a unified method to get responses
    from the LLM.

    Attributes:
        api_endpoint (str): The endpoint for the remote LLM API.
        api_key (str): The API key for authentication with the remote LLM.
        model_LLM (str): The specific LLM model to use.
        debug_mode (bool): Flag to enable or disable debug mode.
        llm_use_local (bool): Flag to determine whether to use a local LLM deployment.
        llm_local_url (str): The URL for the local LLM deployment.

    Methods:
        __init__: Initializes the InterfaceLLM with the provided configuration.
        get_response: Sends a prompt to the LLM and returns the response.
        polish: Polishes the provided text using the LLM.
        proofread: Proofreads the provided text using the LLM.
        summarize: Summarizes the provided text using the LLM.
    """

    def __init__(
        self, api_endpoint, api_key, model_LLM, llm_use_local, llm_local_url, debug_mode
    ):
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.model_LLM = model_LLM
        self.debug_mode = debug_mode
        self.llm_use_local = llm_use_local
        self.llm_local_url = llm_local_url

        print("- check LLM API")

        if self.llm_use_local:
            print("local llm delopyment is used ...")

            if self.llm_local_url == None or self.llm_local_url == "xxx":
                print(">> Stop with empty url for local llm !")
                exit()

            self.interface_llm = InterfaceLocalLLM(self.llm_local_url, self.api_key)

        else:
            print("remote llm api is used ...")

            if (
                self.api_key == None
                or self.api_endpoint == None
                or self.api_key == "xxx"
                or self.api_endpoint == "xxx"
            ):
                print(
                    ">> Stop with wrong API setting: Set api_endpoint (e.g., api.chat...) and api_key (e.g., kx-...) !"
                )
                exit()

            self.interface_llm = InterfaceAPI(
                self.api_endpoint,
                self.api_key,
                self.model_LLM,
                self.debug_mode,
            )

        print("interface_llm: ", self.interface_llm)

        res = self.interface_llm.get_response("1+1=?")

        if res == None:
            print(
                ">> Error in LLM API, wrong endpoint, key, model or local deployment!"
            )
            exit()

        # choose LLMs
        # if self.type == "API2D-GPT":
        #     self.interface_llm = InterfaceAPI2D(self.key,self.model_LLM,self.debug_mode)
        # else:
        #     print(">>> Wrong LLM type, only API2D-GPT is available! \n")

    def get_response(self, prompt_content):
        """
        Sends a prompt to the LLM and returns the response.

        Args:
            prompt_content (str): The prompt to send to the LLM.

        Returns:
            str: The response from the LLM.
        """
        response = self.interface_llm.get_response(prompt_content)

        return response

    def polish(self, text):
        prompt = f"""Polish the following text to improve its clarity, flow, and overall quality. Follow these steps:
        1. Correct any grammatical errors or typos.
        2. Improve sentence structure for better readability.
        3. Enhance vocabulary by replacing weak or repetitive words with more precise alternatives.
        4. Ensure consistency in tone and style throughout the text.
        5. Adjust paragraph structure if necessary for better organization of ideas.
        6. Provide the polished version of the text.

        Original text: {text}"""
        return self.generate_response(prompt)

    def proofread(self, text):
        prompt = f"""Proofread the following text for errors and suggest improvements. Follow these steps:
        1. Identify and correct any spelling mistakes.
        2. Fix grammatical errors, including issues with punctuation, verb tense, and subject-verb agreement.
        3. Check for proper capitalization and formatting.
        4. Highlight any awkward phrasings or unclear sentences.
        5. Suggest improvements for clarity and conciseness where appropriate.
        6. Provide the corrected version of the text, along with a brief summary of the changes made.

        Text to proofread: {text}"""
        return self.generate_response(prompt)

    def summarize(self, text):
        prompt = f"""Summarize the following text concisely while retaining its key points. Follow these steps:
        1. Identify the main topic or theme of the text.
        2. Extract the most important ideas, facts, or arguments presented.
        3. Condense the information into a brief summary, typically 1/4 to 1/3 the length of the original text.
        4. Ensure the summary is coherent and flows logically.
        5. Use your own words as much as possible, avoiding direct quotes unless absolutely necessary.
        6. Provide the summarized version of the text.

        Text to summarize: {text}"""
        return self.generate_response(prompt)

    def generate_response(self, prompt):
        # This method should contain the logic to interact with your LLM
        # and return the generated response
        # For example:
        response = self.interface_llm.get_response(
            prompt
        )  # Assuming self.llm is your LLM instance
        return response
