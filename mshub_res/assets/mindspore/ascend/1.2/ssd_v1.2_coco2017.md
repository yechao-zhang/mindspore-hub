# ssd

---

model-name: ssd

backbone-name: ssd

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: coco2017

accuracy: 23

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/ssd>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/ssd_ascend_v120_coco2017_official_cv_bs32_acc23/ssd_ascend_v120_coco2017_official_cv_bs32_acc23.ckpt>
    asset-sha256: d0b0449bab807e03528c88498425921a7a43a8d97fdd92bed6cf25d5b3379b07

license: Apache2.0

summary: ssd is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssd from the MindSpore model zoo on Gitee at model_zoo/official/cv/ssd.

ssd is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/ssd](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/ssd/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/ssd_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).