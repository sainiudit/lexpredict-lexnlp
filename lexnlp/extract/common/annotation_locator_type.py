from enum import Enum

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/master/LICENSE"
__version__ = "1.6.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class AnnotationLocatorType(Enum):
    RegexpBased = 1
    MlWordVectorBased = 2
