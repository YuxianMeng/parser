# encoding: utf-8
"""
@author: Yuxian Meng
@contact: yuxian_meng@shannonai.com

@version: 1.0
@file: mrc_biaffine_dependency_config
@time: 2020/12/17 14:50
@desc: 

"""


from typing import List
from transformers import BertConfig


class BertMrcDependencyConfig(BertConfig):
    def __init__(self, pos_tags: List[str], dep_tags: List[str], **kwargs):
        super(BertMrcDependencyConfig, self).__init__(**kwargs)
        self.pos_tags = pos_tags
        self.dep_tags = dep_tags
        self.pos_dim = kwargs.get("pos_dim", 0)
        self.mrc_dropout = kwargs.get("mrc_dropout", 0.0)
        self.additional_layer = kwargs.get("additional_layer", 0)
