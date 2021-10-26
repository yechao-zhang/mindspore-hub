# vgg16

---

model-name: vgg16

backbone-name: vgg16

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: imagenet2012

accuracy: 73.49

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/vgg16>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/vgg16_ascend_v130_imagenet2012_official_cv_bs64_top1acc73.49__top5acc91.56/vgg16_ascend_v130_imagenet2012_official_cv_bs64_top1acc73.49__top5acc91.56.ckpt>
    asset-sha256: a400e47c89ce77ade7e45b7eb7c84dc04378152ed92a549e8b5f6e046ef36829

license: Apache2.0

summary: vgg16 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of vgg16 from the MindSpore model zoo on Gitee at model_zoo/official/cv/vgg16.

vgg16 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/vgg16](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/vgg16/README.md).

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

model = "mindspore/ascend/1.3/vgg16_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1000, dataset="imagenet2012")
network.set_train(False)

# ...
```

## Citation

1. Simonyan K, zisserman A. Very Deep Convolutional Networks for Large-Scale Image Recognition[J]. arXiv preprint arXiv:1409.1556, 2014.