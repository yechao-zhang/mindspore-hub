# openpose

---

model-name: openpose

backbone-name: openpose

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: coco2017

accuracy: 33

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/openpose>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/openpose_ascend_v120_coco2017_official_cv_bs10_acc33/openpose_ascend_v120_coco2017_official_cv_bs10_acc33.ckpt>
    asset-sha256: 2f565f0ddb905e9b6079c5442612db2c08b44a8b97521924bd299b09517db549

license: Apache2.0

summary: openpose is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of openpose from the MindSpore model zoo on Gitee at model_zoo/official/cv/openpose.

openpose is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/openpose](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/openpose/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/openpose_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Zhe Cao,Tomas Simon,Shih-En Wei,Yaser Sheikh,"Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields",The IEEE Conference on Computer Vision and Pattern Recongnition(CVPR),2017