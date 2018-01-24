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
class CustomizedUniqueEnum(CustomizedEnum):
    pass


class ModelEnum(CustomizedUniqueEnum):
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
        logger.info('{method} ({args}, {kw}) took {time} sec'.format(
            method=func.__name__, args=args, kw=kwargs, time=te - ts))
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

