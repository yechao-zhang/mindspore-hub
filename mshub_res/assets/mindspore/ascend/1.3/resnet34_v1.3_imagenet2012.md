# resnet

---

model-name: resnet34

backbone-name: resnet34

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: imagenet2012

accuracy: 73.83

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/resnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/resnet34_ascend_v130_imagenet2012_official_cv_bs256_top1acc73.83__top5acc91.61/resnet34_ascend_v130_imagenet2012_official_cv_bs256_top1acc73.83__top5acc91.61.ckpt>
    asset-sha256: b8303354c68c55560d1f1bb04dce4dfd62dd1f02a417c05bfa6b0a920396522c

license: Apache2.0

summary: resnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet.

resnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/resnet/README.md).

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

model = "mindspore/ascend/1.3/resnet34_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, dataset = "imagenet2012")
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. "Deep Residual Learning for Image Recognition"