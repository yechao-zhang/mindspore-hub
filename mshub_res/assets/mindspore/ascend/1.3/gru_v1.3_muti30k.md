# gru

---

model-name: gru

backbone-name: gru

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: muti30k

accuracy: 30

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/nlp/gru>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/gru_ascend_v130_muti30k_official_nlp_bs16_acc30/gru_ascend_v130_muti30k_official_nlp_bs16_acc30.ckpt>
    asset-sha256: 4d0e2582626ed286b9753b8e2b79dcd1c54dc87170f3ddae050796edb5ce8eeb

license: Apache2.0

summary: gru is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of gru from the MindSpore model zoo on Gitee at model_zoo/official/nlp/gru.

gru is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/gru](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/nlp/gru/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.3/gru_v1.3_muti30k"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation, 2014, Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio