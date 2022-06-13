# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
List networks or models.

Loading network definition or pretrained model from mindspore mindspore_hub.
"""

import os
import shutil
import tempfile
import subprocess
from ._utils.download import _download_repo_from_url
from .manage import get_hub_dir

HUB_CONFIG_FILE = 'mindspore_hub_conf.py'
ENTRY_POINT = 'create_network'


def _delete_if_exist(path):
    """Delete backup files"""
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def _get_all_branch_version(hub_dir):
    os.chdir(hub_dir)
    p = subprocess.Popen('git branch -a', stdout=subprocess.PIPE)
    versions = p.stdout.read().decode('UTF-8').split('\n')
    versions = [item.strip() for item in versions if 'remotes' in item and '->' not in item]
    versions = tuple(item.split('origin/')[-1] for item in versions if 'origin/' in item)
    return versions


def hub_list(version=None, force_reload=True):
    r"""
    List all assets supported by MindSpore Hub.

    Args:
        version (str): Specify which version to list. None indicates the latest version. Default: None.
        force_reload (bool): Whether to reload the network from url. Default: True.

    Returns:
        list, a list of assets supported by MindSpore Hub.
    """
    if version is None:
        version = 'master'
    if not isinstance(version, str):
        raise TypeError('`version` must be a str type or None(default).')
    if not isinstance(force_reload, bool):
        raise TypeError('`force_reload` must be a bool type.')

    repo_link = 'https://gitee.com/mindspore/hub.git'
    hub_dir = get_hub_dir()
    res_dir = os.path.join(hub_dir, 'mshub_res')

    if force_reload or (not os.path.isdir(res_dir)):
        if not force_reload:
            print(f'Warning. Can\'t find net cache, will reloading.')
        tmp_dir = tempfile.TemporaryDirectory(dir=hub_dir)
        _download_repo_from_url(repo_link, tmp_dir.name)
        _delete_if_exist(res_dir)
        os.rename(os.path.join(tmp_dir.name, 'hub.git', 'mshub_res'), res_dir)

    # branch_versions = _get_all_branch_version(hub_dir)
    branch_versions = ('master', 'r1.0', 'r1.0.1', 'r1.1', 'r1.2', 'r1.3', 'r1.4', 'r1.5', 'r1.6')
    if version not in branch_versions:
        raise ValueError('`version` must be a correct version: '
                         f'{branch_versions}.')

    assets = []
    for model_version in os.listdir(os.path.join(res_dir, 'assets', 'mindspore')):
        for md_file in os.listdir(os.path.join(res_dir, 'assets', 'mindspore', model_version)):
            asset = md_file[:-len('.md')]
            if asset not in assets:
                assets.append(asset)

    assets.sort()
    return assets
