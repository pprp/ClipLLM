import unittest
from unittest.mock import patch, MagicMock
from eoh.llm.interface_LLM import InterfaceLLM


class TestInterfaceLLM(unittest.TestCase):

    @patch("eoh.llm.interface_LLM.InterfaceAPI")
    @patch("eoh.llm.interface_LLM.InterfaceLocalLLM")
    def test_initialization_remote(self, MockInterfaceLocalLLM, MockInterfaceAPI):
        # Mock the response of the InterfaceAPI
        mock_api_instance = MockInterfaceAPI.return_value
        mock_api_instance.get_response.return_value = "2"

        # Initialize with remote settings
        llm = InterfaceLLM(
            api_endpoint="valid_endpoint",
            api_key="valid_key",
            model_LLM="gpt-3",
            llm_use_local=False,
            llm_local_url=None,
            debug_mode=True,
        )

        # Check if InterfaceAPI was called with correct parameters
        MockInterfaceAPI.assert_called_with(
            "valid_endpoint", "valid_key", "gpt-3", True
        )
        self.assertEqual(llm.get_response("1+1=?"), "2")

    @patch("eoh.llm.interface_LLM.InterfaceAPI")
    @patch("eoh.llm.interface_LLM.InterfaceLocalLLM")
    def test_initialization_local(self, MockInterfaceLocalLLM, MockInterfaceAPI):
        # Mock the response of the InterfaceLocalLLM
        mock_local_instance = MockInterfaceLocalLLM.return_value
        mock_local_instance.get_response.return_value = "2"

        # Initialize with local settings
        llm = InterfaceLLM(
            api_endpoint=None,
            api_key=None,
            model_LLM=None,
            llm_use_local=True,
            llm_local_url="valid_local_url",
            debug_mode=True,
        )

        # Check if InterfaceLocalLLM was called with correct parameters
        MockInterfaceLocalLLM.assert_called_with("valid_local_url")
        self.assertEqual(llm.get_response("1+1=?"), "2")

    @patch("eoh.llm.interface_LLM.InterfaceAPI")
    @patch("eoh.llm.interface_LLM.InterfaceLocalLLM")
    def test_initialization_invalid_local_url(
        self, MockInterfaceLocalLLM, MockInterfaceAPI
    ):
        with self.assertRaises(SystemExit):
            InterfaceLLM(
                api_endpoint=None,
                api_key=None,
                model_LLM=None,
                llm_use_local=True,
                llm_local_url="xxx",
                debug_mode=True,
            )

    @patch("eoh.llm.interface_LLM.InterfaceAPI")
    @patch("eoh.llm.interface_LLM.InterfaceLocalLLM")
    def test_initialization_invalid_api_settings(
        self, MockInterfaceLocalLLM, MockInterfaceAPI
    ):
        with self.assertRaises(SystemExit):
            InterfaceLLM(
                api_endpoint="xxx",
                api_key="xxx",
                model_LLM=None,
                llm_use_local=False,
                llm_local_url=None,
                debug_mode=True,
            )


if __name__ == "__main__":
    unittest.main()
