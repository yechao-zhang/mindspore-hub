# EfficientNet

---

model-name: efficientnet

backbone-name: EfficientNet-B0

module-type: cv

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.1

train-dataset: imagenet

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/efficientnet>

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/efficientnet_GPU_v111_imagenet_offical_cv_bs128_loss3/efficientnet_GPU_v111_imagenet_offical_cv_bs128_loss3.ckpt>
    asset-sha256: c9d495f142cf630c5e4493ce2f0d60a6c83374969594a888b159cb20287b307c

license: Apache2.0

summary: bert_base used to do classification, sequence labeling or squad tasks on various dataset.

---

## Introduction

This MindSpore Hub model uses the implementation of efficientnet from the MindSpore model zoo on Gitee at model_zoo/official/cv/efficientnet.

efficientnet is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/efficientnet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/efficientnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/efficientnet_v1.1_imagenet"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Mingxing Tan, Quoc V. Le. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. 2019.