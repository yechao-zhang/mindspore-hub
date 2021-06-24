# Transformer

---

model-name: transformer

backbone-name: TransformerModel

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128], [1, 128]]

model-version: 1.1

train-dataset: wmtende

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/nlp/transformer>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/transformer_ascend_v111_wmtende_offical_nlp_bs96_belu28/transformer_ascend_v111_wmtende_offical_nlp_bs96_belu28.ckpt>
    asset-sha256: 6a3e672a8f4c49b9ff903f6dd1b6944a34ec91836adf919a5c24ce1f9a3a044c

license: Apache2.0

summary: transformer_large used to do machine translation.

---

## Introduction

This MindSpore Hub model uses the implementation of transformer from the MindSpore model zoo on Gitee at model_zoo/official/nlp/transformer.

transformer is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/transformer](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/nlp/transformer/README.md).

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

model = "mindspore/ascend/1.1/transformer_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

Paper: Ashish Vaswani, Noam Shazeer, Niki Parmar, JakobUszkoreit, Llion Jones, Aidan N Gomez, Ł ukaszKaiser, and Illia Polosukhin. 2017. Attention is all you need. In NIPS 2017, pages 5998–6008.