# encoding: utf-8
"""
@author: Yuxian Meng
@contact: yuxian_meng@shannonai.com
@time: 2020/12/17 14:50
@desc: 

"""


from typing import List
from transformers import BertConfig, RobertaConfig


class BertMrcT2TDependencyConfig(BertConfig):
    def __init__(self, pos_tags: List[str], dep_tags: List[str], **kwargs):
        super(BertMrcT2TDependencyConfig, self).__init__(**kwargs)
        self.pos_tags = pos_tags
        self.dep_tags = dep_tags
        self.pos_dim = kwargs.get("pos_dim", 0)
        self.mrc_dropout = kwargs.get("mrc_dropout", 0.0)
        self.additional_layer = kwargs.get("additional_layer", 0)
        self.additional_layer_type = kwargs.get("additional_layer_type", "lstm")
        self.additional_layer_dim = kwargs.get("additional_layer_dim", self.hidden_size) or self.hidden_size


class RobertaMrcT2TDependencyConfig(RobertaConfig):
    def __init__(self, pos_tags: List[str], dep_tags: List[str], **kwargs):
        super(RobertaMrcT2TDependencyConfig, self).__init__(**kwargs)
        self.pos_tags = pos_tags
        self.dep_tags = dep_tags
        self.pos_dim = kwargs.get("pos_dim", 0)
        self.mrc_dropout = kwargs.get("mrc_dropout", 0.0)
        self.additional_layer = kwargs.get("additional_layer", 0)
        self.additional_layer_type = kwargs.get("additional_layer_type", "lstm")
        self.additional_layer_dim = kwargs.get("additional_layer_dim", self.hidden_size) or self.hidden_size