# deeplabv3

---

model-name: deeplab_v3_s8

backbone-name: deeplabv3

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: voc2012

accuracy: 78.51

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/deeplabv3>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/deeplabv3s8r2_ascend_v130_voc2012_official_cv_bs16_s8acc78.51_ns8mul79.26_ns8mulflip79.37/deeplabv3s8r2_ascend_v130_voc2012_official_cv_bs16_s8acc78.51_ns8mul79.26_ns8mulflip79.37.ckpt>
    asset-sha256: bb00c4455d1b1eaf91ed8c8f1e755b68cfdf8b2c0d5f8a32a611caaa5ae91b0d

license: Apache2.0

summary: deeplabv3 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of deeplabv3 from the MindSpore model zoo on Gitee at model_zoo/official/cv/deeplabv3.

deeplabv3 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/deeplabv3](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/deeplabv3/README.md).

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

model = "mindspore/ascend/1.3/deeplabv3s8r2_v1.3_voc2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=21)
network.set_train(False)

# ...
```

## Citation

1. Chen L C, Papandreou G, Schroff F, et al. Rethinking atrous convolution for semantic image segmentation[J]. arXiv preprint arXiv:1706.05587, 2017.