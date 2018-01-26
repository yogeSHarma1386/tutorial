import pytz
from datetime import datetime, date, timedelta, date as datetime_date
from dateutil.relativedelta import relativedelta

########################## Should only be used if have to avoid the usage of arrow #############################


def add_months_to(dte, count=1):
    """This function adds count to the current datetime.datetime / datetime.date object"""
    return dte + relativedelta(months=count)


def span_dte_across_time_frame(dte, time_frame, is_ceil):
    """This function returns datetime.datetime / datetime.date by ceiling or flooring the provided date according to \
    a valid provided time frame."""
    resultant_dt = dte
    lower_frame = time_frame.lower()
    allowed_time_frames = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']

    if lower_frame in allowed_time_frames:
        index_count = allowed_time_frames.index(lower_frame)
    else:
        raise ValueError("%s is not a valid frame. Please provide one of the following: %s"
                         .format(time_frame, ', '.join(allowed_time_frames))
                         )

    if isinstance(resultant_dt, datetime) and index_count <= len(allowed_time_frames):

        mapping_to_floor = {
            0: resultant_dt.replace(year=resultant_dt.year, month=1, day=1, hour=0, minute=0, second=0, microsecond=0),
            1: resultant_dt.replace(month=resultant_dt.month, day=1, hour=0, minute=0, second=0, microsecond=0),
            2: resultant_dt.replace(hour=0, minute=0, second=0, microsecond=0),
            3: resultant_dt.replace(minute=0, second=0, microsecond=0),
            4: resultant_dt.replace(second=0, microsecond=0),
            5: resultant_dt.replace(microsecond=0)
        }

        resultant_dt = mapping_to_floor[index_count]

        if is_ceil:
            mapping_to_ceil = {
                0: resultant_dt.replace(year=resultant_dt.year+1) - timedelta(microseconds=1),
                1: resultant_dt.replace(month=add_months_to(resultant_dt, 1).month) - timedelta(microseconds=1),
                2: resultant_dt + timedelta(days=1) - timedelta(microseconds=1),
                3: resultant_dt + timedelta(hours=1) - timedelta(microseconds=1),
                4: resultant_dt + timedelta(minutes=1) - timedelta(microseconds=1),
                5: resultant_dt + timedelta(seconds=1) - timedelta(microseconds=1)
            }
            resultant_dt = mapping_to_ceil[index_count]
    elif isinstance(resultant_dt, datetime_date) and index_count < 2:

        mapping_to_floor = {
            0: resultant_dt.replace(day=1, month=1, year=resultant_dt.year),
            1: resultant_dt.replace(day=1, month=resultant_dt.month),
        }

        resultant_dt = mapping_to_floor[index_count]

        if is_ceil:
            mapping_to_ceil = {
                0: resultant_dt.replace(year=resultant_dt.year + 1),
                1: resultant_dt.replace(month=add_months_to(resultant_dt, 1).month),
            }
            resultant_dt = mapping_to_ceil[index_count] - timedelta(days=1)
    else:
        raise ValueError("Wrong set of inputs to find %s.".format("ceil" if is_ceil else "floor"))

    return resultant_dt


def dt_ceiling(dte, frame):
    ''' Returns a date/ datetime object (according to the one sent in the parameter).

    :param frame: the timeframe.  Can be any ``datetime`` property (day, hour, minute...).

    Usage::

        >>> dt_ceiling(date(year=2016, month=3, day=3), 'month')
        Result date(year=2016, month=3, day=31)
    '''
    return span_dte_across_time_frame(dte, time_frame=frame, is_ceil=True)


def dt_flooring(dte, frame):
    ''' Returns a date/ datetime object (according to the one sent in the parameter).

    :param frame: the timeframe.  Can be any ``datetime`` property (day, hour, minute...).

    Usage::

        >>> dt_flooring(date(year=2016, month=2, day=3), 'month')
        Result date(year=2016, month=2, day=1)
    '''

    return span_dte_across_time_frame(dte, time_frame=frame, is_ceil=False)

###############################################################################################################