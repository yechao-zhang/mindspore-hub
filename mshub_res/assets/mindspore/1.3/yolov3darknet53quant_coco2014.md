# yolov3_darknet53_quant

---

model-name: yolov3_darknet53_quant

backbone-name: yolov3_darknet53_quant

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: coco2014

evaluation: mAP31

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/cv/yolov3_darknet53_quant>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/yolov3darknet53quant_ascend_v130_coco2014_official_cv_mAP31.ckpt>
    asset-sha256: d41609bc771288a2424a7b6bd6fa688abc345fbdc152ead669eda8ed3d783c9c

license: Apache2.0

summary: yolov3_darknet53_quant is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_darknet53_quant from the MindSpore model zoo on Gitee at official/cv/yolov3_darknet53_quant.

yolov3_darknet53_quant is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/yolov3_darknet53_quant](https://gitee.com/mindspore/models/blob/r1.3/official/cv/yolov3_darknet53_quant/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/yolov3darknet53quant_coco2014"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

YOLOv3: An Incremental Improvement.Joseph Redmon, Ali Farhadi, University of Washington

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.