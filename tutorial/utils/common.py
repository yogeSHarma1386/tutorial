import collections
import os
import time

from enum import unique as unique_enum, Enum


class CustomizedEnum(Enum):
    @classmethod
    def get_values(cls):
        return [(s.name, s.value) for s in cls]

    @classmethod
    def as_map(cls, default_value=None, key_to_lower=False, value_as_none=False):
        key = lambda s: s.name.lower() if key_to_lower else s.name
        value = lambda s: default_value if (default_value is not None or value_as_none) else s.value
        return {key(s): value(s) for s in cls}

    @classmethod
    def as_list(cls, key=None):
        return [s.name if not key else {key: s.name} for s in cls]

    @classmethod
    def values(cls):
        return [s.value for s in cls]

    @classmethod
    def get_member(cls, member_name, is_comparision_case_sensitive=False):
        try:
            if is_comparision_case_sensitive:
                return [s for s in cls if s.value == member_name][0]
            else:
                return [s for s in cls if s.value.lower() == member_name.lower()][0]
        except IndexError as ex:
            raise Exception('\"{0}\" is not a member of the ModelEnum: {1}.'.format(member_name, cls.__name__))    \
                    .with_traceback(ex.__traceback__)


@unique_enum
class UniquelyCustomizedEnum(CustomizedEnum):
    pass


def timeit(func):
    """Utility wrapper to measure time taken by the function call

    :param func: Callback reference for which we need to measure the time
    :param args: Args of the method
    :param kwargs: Kwargs of the method
    :return: return the Wrapper function
    """
    def wrapped(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print('{method} ({args}, {kw}) took {time} sec'.format(method=func.__name__,
                                                               args=args,
                                                               kw=kwargs,
                                                               time=te - ts))
        return result
    return wrapped


@unique_enum
class DynamicEnum(Enum):
    """
    TODO: Rename my functions and their usage
    """
    @classmethod
    def add_members(cls, *args, **kwargs):

        if not hasattr(cls, 'choices'):
            cls.choices = {}

        records = args[0]
        cls.members = [cls._add_member(record) for record in records]
        return cls.members

    @classmethod
    def _add_member(cls, record):

        member = object.__new__(cls)
        member.first = record[0]
        member.last = record[1]

        member._value_ = member.first, member.last
        member._name_ = "{0} - {1}".format(member.first, member.last)
        cls.choices[member.first] = member.last
        return member

    @classmethod
    def get_choices(cls):
        return cls.choices

    @classmethod
    def values(cls):
        return list(cls.choices.values())

    @classmethod
    def keys(cls):
        return list(cls.choices.keys())

    @classmethod
    def members(cls):
        return [(k, v) for k, v in cls.choices.items()]

    @classmethod
    def as_map(cls, default_value=None, key_to_lower=False, value_as_none=False):
        key = lambda s: s.name.lower() if key_to_lower else s.name
        value = lambda s: default_value if (default_value is not None or value_as_none) else s.value
        return {key(s): value(s) for s in cls.choices}


class EnvironmentVariables(UniquelyCustomizedEnum):
    DB_NAME = 'DJ_PRACTICE__DB_NAME'
    DB_USER = 'DJ_PRACTICE__DB_USER'
    DB_PASSWORD = 'DJ_PRACTICE__DB_PASSWORD'


def get_env_variable(var_name, default_value=None):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        print(error_msg)

        return default_value


def get_cleansed_from(value, exculsions):
    """
    This function will cleanse the :param value if it is present in exclusions, by returning None.

    :param value : type - T
    :param exculsions : type - [X]
    :return: None or :param value
    """
    if (isinstance(value, str) or not isinstance(value, collections.Iterable)) and value is not None:
        return None if value in exculsions else value
    elif isinstance(value, collections.Iterable):
        value = list(value)
        [value if exculsion not in value else value.remove(exculsion) for exculsion in exculsions]
        return value
    else:
        return None


def safe_convert(value, type, default=None):
    types = {
        'int': int,
        'float': float,
        'str': str,
        'bool': bool
    }

    if type == 'bool':
        value = value.lower() if isinstance(value, str) else value

        if value in ["true", True, 1, '1']:
            return True
        elif value in ["false", False, None, [], {}, (), set([]), 0, '0']:
            return False
        else:
            return default
    else:
        try:
            return types.get(type)(value)
        except:
            return default
