
from parser.models.biaffine_dependency_config import BertDependencyConfig
from parser.models.t2t_dependency_config import BertMrcT2TDependencyConfig
from parser.models.span_proposal_config import BertSpanProposalConfig, RoBertaSpanProposalConfig
from parser.models.s2t_query_dependency_config import BertMrcS2TQueryDependencyConfig, RobertaMrcS2TQueryDependencyConfig
from parser.models.s2s_query_dependency_config import BertMrcS2SQueryDependencyConfig, RobertaMrcS2SQueryDependencyConfig

from parser.models.biaffine_dependency_parser import BiaffineDependencyParser
from parser.models.t2t_dependency_parser import BiaffineDependencyT2TParser
from parser.models.span_proposal import SpanProposal
from parser.models.s2t_query_dependency_parser import BiaffineDependencyS2TQeuryParser
from parser.models.s2s_query_dependency_parser import BiaffineDependencyS2SQeuryParser
