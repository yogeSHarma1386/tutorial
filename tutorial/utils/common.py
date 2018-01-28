import collections
import os
from datetime import time

from enum import unique as unique_enum, Enum


class CustomizedEnum(Enum):

    @classmethod
    def get_all_members(cls):
        """
        :return: list of all members of the class.
        """
        return [s for s in cls]

    @classmethod
    def paired_details(cls):
        """
        :return: tuple(class_member.name, class_member.value) for all members of the class.
        """
        return [(s.name, s.value) for s in cls]

    @classmethod
    def as_map(cls, default_value=None, key_to_lower=False, value_as_none=False):
        """
        :param default_value:
        :param key_to_lower: Should the key values be in lowercase? (Accepts True/ False)
        :param value_as_none: If default_value is present or value_value_as_none is acceptable,
                                class_member.value = default_value

        :return: dict({class_member.key: class_member.value}) for all members of the class.
        """
        key = lambda s: s.name.lower() if key_to_lower else s.name
        value = lambda s: default_value if (default_value is not None or value_as_none) else s.value
        return {key(s): value(s) for s in cls}

    @classmethod
    def as_list(cls, should_return_names=True, key=None):
        """
        :param key: Should values be returned in {key -> value} pairs? If so, this parameter will contain that key.
        :param should_return_names: Should return name(s) or value(s)?
                                        True -> means will return names
                                        False -> means will return values
        :return: List of class_member.name(s) in either of these format
                    ['MEMBER_1', 'MEMBER_2', 'MEMBER_3', 'MEMBER_4'] where key = None

                                        OR

                    [{'key_value': 'MEMBER_1'}, {'key_value': 'MEMBER_2'},
                     {'key_value': 'MEMBER_3'}, {'key_value': 'MEMBER_4'}] where key = 'key_value'

        """
        result = []
        if should_return_names:
            result = [s.name if not key else {key: s.name} for s in cls]
        else:
            result = [s.value if not key else {key: s.value} for s in cls]

        return result

    @classmethod
    def names(cls):
        """
        :return: class_member.name for all class members.
        """
        return [s.names for s in cls]

    @classmethod
    def values(cls):
        """
        :return: class_member.value for all class members.
        """
        return [s.value for s in cls]

    @classmethod
    def get_member(cls, member_value, is_comparision_case_sensitive=False):
        """
        :param member_value: value of a valid class member
        :param is_comparision_case_sensitive: Should the comparision made be case sensitive? (Accepts True/ False)
        :return: class_member where class_member.value == member_value
        """
        try:
            if is_comparision_case_sensitive:
                return [s for s in cls if s.value == member_value][0]
            else:
                return [s for s in cls if s.value.lower() == member_value.lower()][0]
        except IndexError as ex:
            raise Exception('\"{0}\" is not a member of the ModelEnum: {1}.'.format(member_value, cls.__name__))


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
        print('{method} ({args}, {kw}) took {time} sec'.format(
            method=func.__name__, args=args, kw=kwargs, time=te - ts))
        return result
    return wrapped


@unique_enum
class DynamicEnum(Enum):
    """
    A class which builds Enum dynamically, using the function add_members.
    """
    # TODO: Rename my functions and their usage
    @classmethod
    def add_members(cls, *args, **kwargs):
        """
        :param args: First value of this parameter will be used as the dynamic source for building members of this Enum.
                        This source must have name and value in tupled pairs.
                        For e.g. [  ('MEMBER_1_NAME', 'MEMBER_1_VALUE'),
                                    ('MEMBER_2_NAME', 'MEMBER_2_VALUE'),
                                    ('MEMBER_3_NAME', 'MEMBER_3_VALUE')
                                ]
        :param kwargs:
        :return: Members of this Enum.
        """

        if not hasattr(cls, 'choices'):
            cls.choices = {}

        records = args[0]
        cls.members = [cls._add_member(record) for record in records]
        return cls.members

    @classmethod
    def _add_member(cls, record):
        """
        :param record: This parameter must contain name and value in tupled pair.
        :return: class member
        """

        member = object.__new__(cls)
        member.first = record[0]
        member.last = record[1]

        member._value_ = member.first, member.last
        member._name_ = "{0} - {1}".format(member.first, member.last)
        cls.choices[member.first] = member.last
        return member

    @classmethod
    def get_all_members(cls):
        """
        :return: list of all members of the class.
        """
        # FIXME: This might not be the correct output.
        return [s for s in cls.choices]

    @classmethod
    def paired_details(cls):
        """
        :return: tuple(class_member.name, class_member.value) for all members of the class.
        """
        return [(k, v) for k, v in cls.choices.items()]

    @classmethod
    def as_map(cls, default_value=None, key_to_lower=False, value_as_none=False):
        """
        :param default_value:
        :param key_to_lower: Should the key values be in lowercase? (Accepts True/ False)
        :param value_as_none: If default_value is present or value_value_as_none is acceptable,
                                class_member.value = default_value

        :return: dict({class_member.key: class_member.value}) for all members of the class.
        """
        # FIXME: This might not be the correct output.
        key = lambda s: s.name.lower() if key_to_lower else s.name
        value = lambda s: default_value if (default_value is not None or value_as_none) else s.value
        return {key(s): value(s) for s in cls.choices}

    @classmethod
    def as_list(cls, should_return_names=True, key=None):
        """
        :param key: Should values be returned in {key -> value} pairs? If so, this parameter will contain that key.
        :param should_return_names: Should return name(s) or value(s)?
                                        True -> means will return names
                                        False -> means will return values
        :return: List of class_member.name(s) in either of these format
                    ['MEMBER_1', 'MEMBER_2', 'MEMBER_3', 'MEMBER_4'] where key = None

                                        OR

                    [{'key_value': 'MEMBER_1'}, {'key_value': 'MEMBER_2'},
                     {'key_value': 'MEMBER_3'}, {'key_value': 'MEMBER_4'}
                    ] where key = 'key_value'

        """
        # FIXME: This might not be the correct output.
        result = []
        if should_return_names:
            result = [s.name if not key else {key: s.name} for s in cls]
        else:
            result = [s.value if not key else {key: s.value} for s in cls]

        return result

    @classmethod
    def names(cls):
        """
        :return: List of names of class_members.
        """
        return list(cls.choices.keys())

    @classmethod
    def values(cls):
        """
        :return: List of values of class_members.
        """
        return list(cls.choices.values())

    @classmethod
    def get_member(cls, member_value, is_comparision_case_sensitive=False):
        """
        :param member_value: value of a valid class member
        :param is_comparision_case_sensitive: Should the comparision made be case sensitive? (Accepts True/ False)
        :return: class_member where class_member.value == member_value
        """
        # FIXME: This might not be the correct output.
        try:
            if is_comparision_case_sensitive:
                return [s for s in cls if s.value == member_value][0]
            else:
                return [s for s in cls if s.value.lower() == member_value.lower()][0]
        except IndexError as ex:
            raise Exception('\"{0}\" is not a member of the ModelEnum: {1}.'.format(member_value, cls.__name__))

    @classmethod
    def get_choices(cls):
        """
        :return: list all choices of the class.
        """
        return cls.choices


class EnvironmentVariables(UniquelyCustomizedEnum):
    """
    Set all the environment variables in utils itself.
    """
    DB_NAME = 'DJ_PRACTICE__DB_NAME'
    DB_USER = 'DJ_PRACTICE__DB_USER'
    DB_PASSWORD = 'DJ_PRACTICE__DB_PASSWORD'


def get_env_variable(var_name, default_value=None):
    """
    This function gets the value of an environment variable.

    :param var_name: Name of the environment variable to be searched for.
    :param default_value: Default value will be returned if environment variable is not present.
    :return: Value of the environment variable.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        print(error_msg)

        return default_value


def get_cleansed_from(value, exculsions):
    """
    This function will cleanse the :param value if it is present in exclusions, by returning None.

    :param value : :type - T
    :param exculsions : :type - [X]
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


def safe_convert(value, desired_type, default_value=None):
    """
    This function safely converts a value to the desired data-type.

    :param value: The value to be converted.
    :param desired_type: Desired data-type of the result.
    :param default_value: Default value, in case the conversion fails.
    :return: converted value
    """
    types = {
        'int': int,
        'float': float,
        'str': str,
        'bool': bool
    }

    if desired_type == 'bool':
        value = value.lower() if isinstance(value, str) else value

        if value in ["true", True, 1, '1']:
            return True
        elif value in ["false", False, None, [], {}, (), set([]), 0, '0']:
            return False
        else:
            return default_value
    else:
        try:
            return types.get(desired_type)(value)
        except:
            return default_value
