from types import DynamicClassAttribute

from .common import UniquelyCustomizedEnum


class AppNameSpace(UniquelyCustomizedEnum):
    Base = 'All Tutorials'

    REST = 'REST Framework'
    WORKFLOW = 'WorkFlow'


class AppNames(UniquelyCustomizedEnum):
    Base = 'tutorials'

    REST = 'rest'
    WORKFLOW = 'workflow'
