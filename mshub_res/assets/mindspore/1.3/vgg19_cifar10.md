# vgg19

---

model-name: vgg19

backbone-name: vgg19

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: cifar10

evaluation: acc93.78

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/vgg19>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/vgg19_ascend_v130_cifar10_research_cv_acc93.78.ckpt>
    asset-sha256: be9a7860d521b6036cb8fde0183eb5c577817987d3ca8fde5e459af3d77e941c

license: Apache2.0

summary: vgg19 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of vgg19 from the MindSpore model zoo on Gitee at research/cv/vgg19.

vgg19 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/vgg19](https://gitee.com/mindspore/models/blob/r1.3/research/cv/vgg19/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/vgg19_cifar10"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Simonyan K, zisserman A. Very Deep Convolutional Networks for Large-Scale Image Recognition[J]. arXiv preprint arXiv:1409.1556, 2014.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.