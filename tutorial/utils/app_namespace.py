from types import DynamicClassAttribute

from .common import CustomizedUniqueEnum


class AppNameSpace(CustomizedUniqueEnum):
    Base = 'All Tutorials'

    REST = 'REST Framework'


class AppNames(CustomizedUniqueEnum):
    Base = 'tutorials'

    REST = 'rest'
