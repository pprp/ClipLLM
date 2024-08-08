import unittest
from clipllm.llm.interface_LLM import InterfaceLLM

KEY = "sk-fd09809450c84054b541a06af631da0f"
MODEL = "deepseek-chat"
BASE_URL = "https://api.deepseek.com"
ENDPOINT = "https://api.deepseek.com/v1"


class TestInterfaceLLM(unittest.TestCase):

    def test_initialization_remote(self):
        # Initialize with remote settings
        llm = InterfaceLLM(
            api_endpoint=BASE_URL,
            api_key=KEY,
            model_LLM=MODEL,
            llm_use_local=False,
            llm_local_url=BASE_URL,
            debug_mode=True,
        )

        # Test the API call
        response = llm.get_response("1+4=?")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

    def test_initialization_local(self):
        # Initialize with local settings
        llm = InterfaceLLM(
            api_endpoint="http://localhost:11434/v1",
            api_key="gemma2:2b",  # required, but unused
            model_LLM="gemma2:2b",
            llm_use_local=True,
            llm_local_url="http://localhost:11434",
            debug_mode=True,
        )

        # Test the local LLM call
        response = llm.get_response("1+1=?")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)


if __name__ == "__main__":
    unittest.main()
