import collections

from __builtin__ import reduce
from django.db import connection
from django.utils.decorators import ContextDecorator

from tutorial.utils import UniquelyCustomizedEnum


class ModelEnum(UniquelyCustomizedEnum):
    pass


class QueryCountMe(ContextDecorator):

    def __init__(self, *args, **kwargs):
        self.label = kwargs["label"] if "label" in kwargs else ""

    def __call__(self, *args, **kwargs):
        if not self.label:
            self.label = args[0].__name__ if args else self.label

        return super(QueryCountMe, self).__call__(*args, **kwargs)

    def __enter__(self):
        self.initial_query_count = len(connection.queries)
        return self

    def __exit__(self, *args):
        count = len(connection.queries) - self.initial_query_count
        total_time = reduce(lambda a, b: a + float(b['time']), connection.queries[-count:], 0.0)

        print("For {} {} queries hit".format(self.label, count))
        print("Total time taken {}".format(total_time))

        return False


def get_flattened_dictionary(messed_up_iterable, key_string, value_keys, overwrite_if_repeats=False):
    """

    :param messed_up_iterable: The input dictionary.
    :param key_string: It is the key string whose value will be taken as the key for the resultant flattened dictionary.
    :param value_keys: It is the key string whose value will be taken as the value for the resultant flattened dictionary.
    :param overwrite_if_repeats: If messedup_iterable__item[key_string] is already present in the resultant flattened dictionary
                                 just derived, should it replace (True) the value or skip (False)?

    Sample working of this function:-

    Case 1:
    :param messedup_iterable:
        [
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Lakshmi Relekar', 'user_id': 89, 'aggregator_id': 14},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Demo User', 'user_id': 98, 'aggregator_id': 18},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Ayush Agarwal', 'user_id': 64, 'aggregator_id': 17},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Vinit Rai', 'user_id': 117, 'aggregator_id': 33},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Suresh N', 'user_id': 135, 'aggregator_id': 68},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Vivekananda Athukuri3', 'user_id': 163, 'aggregator_id': 63},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Admin2 Two', 'user_id': 104, 'aggregator_id': 84}
        ]
    :param key_string: 'aggregator_id'
    :param value_keys: 'full_name'
    :param overwrite_if_repeats: False (by default)
    :return: {17: 'Ayush Agarwal', 18: 'Demo User', 68: 'Suresh N', 33: 'Vinit Rai', 84: 'Admin2 Two', 14: 'Lakshmi Relekar', 63: 'Vivekananda Athukuri3'}


    Case 2:
    :param messedup_iterable:
        [
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Lakshmi Relekar', 'user_id': 89, 'aggregator_id': 14},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Demo User', 'user_id': 98, 'aggregator_id': 18},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Ayush Agarwal', 'user_id': 64, 'aggregator_id': 17},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Vinit Rai', 'user_id': 117, 'aggregator_id': 33},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Suresh N', 'user_id': 135, 'aggregator_id': 68},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Vivekananda Athukuri3', 'user_id': 163, 'aggregator_id': 63},
            {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Admin2 Two', 'user_id': 104, 'aggregator_id': 84}
        ]
    :param key_string: 'aggregator_id'
    :param value_keys: ['customer_code', 'full_name', 'sap_entry_status', 'user_id']
    :param overwrite_if_repeats: False (by default)
    :return:
        {
            17: {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Ayush Agarwal', 'user_id': 64},
            18: {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Demo User', 'user_id': 98},
            68: {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Suresh N', 'user_id': 135},
            33: {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Vinit Rai', 'user_id': 117},
            84: {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Admin2 Two', 'user_id': 104},
            14: {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Lakshmi Relekar', 'user_id': 89},
            63: {'sap_entry_status': 'pending_verification', 'customer_code': None, 'full_name': 'Vivekananda Athukuri3', 'user_id': 163}
        }
    """

    value_keys = list(set(value_keys)) if not isinstance(value_keys, str) and isinstance(value_keys, collections.Iterable) else value_keys

    flattened_dict = dict()
    for unorganised_item in messed_up_iterable:
        if (overwrite_if_repeats and unorganised_item[key_string] in flattened_dict) or unorganised_item[key_string] not in flattened_dict:
            if isinstance(value_keys, str) or not isinstance(value_keys, collections.Iterable):
                flattened_dict[unorganised_item[key_string]] = unorganised_item[value_keys]
            else:
                flattened_dict[unorganised_item[key_string]] = dict()
                for key in value_keys:
                    flattened_dict[unorganised_item[key_string]][key] = unorganised_item[key]
    return flattened_dict
