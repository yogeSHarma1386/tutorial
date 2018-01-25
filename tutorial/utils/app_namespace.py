from types import DynamicClassAttribute

from .common import UniquelyCustomizedEnum


class AppNameSpace(UniquelyCustomizedEnum):
    Base = 'All Tutorials'

    REST = 'REST Framework'


class AppNames(UniquelyCustomizedEnum):
    Base = 'tutorials'

    REST = 'rest'
