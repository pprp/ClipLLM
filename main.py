import sys

from PyQt5.QtWidgets import QApplication
from clipllm.interface import ContextMenu

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = ContextMenu()
    menu.run()

# Transformer based large language models have achieved tremendous success. However, the significant memory and
# computational costs incurred during the inference process make it challenging to deploy large models on resource-constrained
# devices. In this paper, we investigate compression and efficient inference methods for large language models from an algorithmic
# perspective. Regarding taxonomy, similar to smaller models, compression and acceleration algorithms for large language models can
# still be categorized into quantization, pruning, distillation, compact architecture design, dynamic networks. However, Large language
# models have two prominent characteristics compared to smaller models: (1) Most of compression algorithms require finetuning or even
# retraining the model after compression. The most notable aspect of large models is the very high cost associated with model finetuning
# or training. Therefore, many algorithms for large models, such as quantization and pruning, start to explore tuning-free algorithms. (2)
# Large models emphasize versatility and generalization rather than performance on a single task. Hence, many algorithms, such as
# knowledge distillation, focus on how to preserving their versatility and generalization after compression. Since these two characteristics
# were not very pronounced in early large models, we further distinguish large language models into medium models and “real” large
# models. Additionally, we also provide an introduction to some mature frameworks for efficient inference of large models, which can
# support basic compression or acceleration algorithms, greatly facilitating model deployment for users.
