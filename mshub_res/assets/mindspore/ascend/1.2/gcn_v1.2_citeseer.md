# gcn

---

model-name: gcn

backbone-name: gcn

module-type: gnn

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: citeseer

accuracy: 70

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/gnn/gcn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/gcn_ascend_v120_citeseer_official_gnn_bs1_acc70/gcn_ascend_v120_citeseer_official_gnn_bs1_acc70.ckpt>
    asset-sha256: e912d70442e0307066d43d0267ee5e35894dbdbe485a2604fab6e996287caef5

license: Apache2.0

summary: gcn is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of gcn from the MindSpore model zoo on Gitee at model_zoo/official/gnn/gcn.

gcn is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/gnn/gcn](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/gnn/gcn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

input_dim = 3703
output_dim = 6

model = "mindspore/ascend/1.2/gcn_v1.2_citeseer"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, input_dim=input_dim, output_dim=output_dim)
network.set_train(False)

# ...
```

## Citation

1. Thomas N. Kipf, Max Welling. 2016. Semi-Supervised Classification with Graph Convolutional Networks. In ICLR 2016.