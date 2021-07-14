# FaceQualityAssessment

---

model-name: FaceQualityAssessment

backbone-name: FaceQualityAssessment

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: humanface

accuracy: 18

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/FaceQualityAssessment>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/facequalityassessment_ascend_v120_humanface_research_cv_bs32_IPNacc18_MAEacc18/facequalityassessment_ascend_v120_humanface_research_cv_bs32_IPNacc18_MAEacc18.ckpt>
    asset-sha256: 7b9a72f5fea043c510d18161b1609f702b252691a20ddc5adb6b008cc43f35c8

license: Apache2.0

summary: FaceQualityAssessment is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FaceQualityAssessment from the MindSpore model zoo on Gitee at model_zoo/research/cv/FaceQualityAssessment.

FaceQualityAssessment is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/FaceQualityAssessment](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/FaceQualityAssessment/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/facequalityassessment_v1.2_humanface"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. "Deep Residual Learning for Image Recognition"