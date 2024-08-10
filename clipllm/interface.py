import sys
import logging
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QMainWindow,
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt5.QtGui import QCursor
import pyperclip
from pynput import keyboard
import signal
from clipllm.llm.interface_LLM import InterfaceLLM

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


class KeyboardHandler(QObject):
    show_menu_signal = pyqtSignal()

    def on_key_event(self, key, pressed):
        if pressed:
            if key == keyboard.Key.alt_l and keyboard.KeyCode.from_char("c"):
                logging.info("Alt+C detected")
                self.show_menu_signal.emit()
        else:
            if key == keyboard.Key.esc:
                logging.info("Escape key detected")
                # break currently
                exit()


class ContextMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_llm()
        self.setup_ui()
        self.setup_signals()
        self.keyboard_handler = KeyboardHandler()
        self.keyboard_handler.show_menu_signal.connect(self.show_menu)
        self.keyboard_listener = None
        logging.info("ContextMenu initialized")

    def setup_window(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.hide()
        self.hide_timer = QTimer(self)
        self.hide_timer.timeout.connect(self.hide)
        logging.info("Window setup complete")

    def setup_llm(self):
        self.llm = InterfaceLLM(
            api_endpoint="http://localhost:11434/v1",
            api_key="gemma2:2b",
            model_LLM="gemma2:2b",
            llm_use_local=True,
            llm_local_url="http://localhost:11434",
            debug_mode=True,
        )
        logging.info("LLM setup complete")

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        button_layout = QHBoxLayout()
        buttons = [
            ("Polish", "polish"),
            ("Proofread", "proofread"),
            ("Summarize", "summarize"),
            ("Copy", "copy"),
        ]
        for text, action in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, a=action: self.process_text(a))
            button_layout.addWidget(btn)

        close_button = QPushButton("●")
        close_button.setStyleSheet("color: #FF605C; font-size: 14px; border: none;")
        close_button.clicked.connect(self.hide)
        button_layout.addWidget(close_button)

        layout.addLayout(button_layout)
        self.text_field = QTextEdit()
        layout.addWidget(self.text_field)
        logging.info("UI setup complete")

    def setup_signals(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        logging.info("Signals setup complete")

    def show_menu(self):
        self.move(QCursor.pos())
        self.show()
        self.activateWindow()  # This brings the window to the front
        self.hide_timer.start(30000)
        logging.info("Menu shown")

    def process_text(self, action):
        selected_text = pyperclip.paste()
        logging.info(f"Processing text with action: {action}")
        try:
            if action == "polish":
                result = self.llm.polish(selected_text)
            elif action == "proofread":
                result = self.llm.proofread(selected_text)
            elif action == "summarize":
                result = self.llm.summarize(selected_text)
            elif action == "copy":
                result = self.text_field.toPlainText()
                pyperclip.copy(result)
                self.text_field.setText("Text copied to clipboard!")
                return
            else:
                raise ValueError(f"Unknown action: {action}")

            self.text_field.setText(result)
        except AttributeError as e:
            logging.error(f"Method not found: {str(e)}")
            self.text_field.setText(f"Error: Action '{action}' not available")
        except Exception as e:
            logging.error(f"Error processing text: {str(e)}")
            self.text_field.setText(f"Error: {str(e)}")
        self.hide_timer.start(30000)
        logging.info("Text processing complete")

    def run(self):
        self.keyboard_listener = keyboard.Listener(
            on_press=lambda key: self.keyboard_handler.on_key_event(key, True),
            on_release=lambda key: self.keyboard_handler.on_key_event(key, False),
        )
        self.keyboard_listener.start()
        logging.info("Keyboard listener started")

        try:
            QApplication.instance().exec_()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            self.cleanup()

    def cleanup(self):
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        QApplication.instance().quit()
        logging.info("Cleanup complete")

    def signal_handler(self, signum, frame):
        logging.info("Received signal to terminate. Cleaning up...")
        self.cleanup()
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = ContextMenu()
    logging.info("ContextMenu created, starting run")
    menu.run()
