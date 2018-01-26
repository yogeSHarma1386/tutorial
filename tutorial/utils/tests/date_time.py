
import arrow
import pytz

from datetime import datetime, date, timedelta, date as datetime_date
from dateutil.relativedelta import relativedelta

from tutorial.utils.date_time import dt_flooring, dt_ceiling


def test_dte_ceiling(self):
    # FIXME: Change these to have proper test cases.
    print("---------------------Ceiling---------------------")

    d0 = datetime(2018, 10, 8, 4, 35, 8, 987, pytz.UTC)
    print("---------------------DateTimes---------------------", d0)

    print("year:", dt_ceiling(d0, "year"),
          arrow.get(d0).ceil("year").datetime,
          dt_ceiling(d0, "year") == arrow.get(d0).ceil("year").datetime)

    print("month:", dt_ceiling(d0, "month"),
          arrow.get(d0).ceil("month").datetime,
          dt_ceiling(d0, "month") == arrow.get(d0).ceil("month").datetime)

    print("day:", dt_ceiling(d0, "day"),
          arrow.get(d0).ceil("day").datetime,
          dt_ceiling(d0, "day") == arrow.get(d0).ceil("day").datetime)

    print("hour:", dt_ceiling(d0, "hour"),
          arrow.get(d0).ceil("hour").datetime,
          dt_ceiling(d0, "hour") == arrow.get(d0).ceil("hour").datetime)

    print("minute:", dt_ceiling(d0, "minute"),
          arrow.get(d0).ceil("minute").datetime,
          dt_ceiling(d0, "minute") == arrow.get(d0).ceil("minute").datetime)

    print("second:", dt_ceiling(d0, "second"),
          arrow.get(d0).ceil("second").datetime,
          dt_ceiling(d0, "second") == arrow.get(d0).ceil("second").datetime)

    # print("microsecond:",   dt_ceiling(d0, "microsecond"),  arrow.get(d0).ceil("microsecond").datetime)

    print()
    print()
    print()

    print("---------------------Date---------------------", d0)
    d0 = date(2018, 10, 8)
    print("year:", dt_ceiling(d0, "year"), arrow.get(d0).ceil("year").date())
    print("month:", dt_ceiling(d0, "month"), arrow.get(d0).ceil("month").date())
    # print("day:",           dt_ceiling(d0, "day"),          arrow.get(d0).ceil("day").date())
    # # print("hour:",          dt_ceiling(d0, "hour"),         arrow.get(d0).ceil("hour").date())
    # # print("minute:",        dt_ceiling(d0, "minute"),       arrow.get(d0).ceil("minute").date())
    # # print("second:",        dt_ceiling(d0, "second"),       arrow.get(d0).ceil("second").date())
    # # print("microsecond:",   dt_ceiling(d0, "microsecond"),  arrow.get(d0).ceil("microsecond").date())


def test_dte_flooring(self):
    # FIXME: Change these to have proper test cases.
    print("---------------------Flooring---------------------")

    d1 = datetime(2018, 10, 8, 4, 35, 8, 987, pytz.UTC)
    print("---------------------DateTimes---------------------", d1)

    print("year:", dt_flooring(d1, "year"),
          arrow.get(d1).floor("year").datetime,
          dt_flooring(d1, "year") == arrow.get(d1).floor("year").datetime)

    print("month:", dt_flooring(d1, "month"),
          arrow.get(d1).floor("month").datetime,
          dt_flooring(d1, "month") == arrow.get(d1).floor("month").datetime)

    print("day:", dt_flooring(d1, "day"),
          arrow.get(d1).floor("day").datetime,
          dt_flooring(d1, "day") == arrow.get(d1).floor("day").datetime)

    print("hour:", dt_flooring(d1, "hour"),
          arrow.get(d1).floor("hour").datetime,
          dt_flooring(d1, "hour") == arrow.get(d1).floor("hour").datetime)

    print("minute:", dt_flooring(d1, "minute"),
          arrow.get(d1).floor("minute").datetime,
          dt_flooring(d1, "minute") == arrow.get(d1).floor("minute").datetime)

    print("second:", dt_flooring(d1, "second"),
          arrow.get(d1).floor("second").datetime,
          dt_flooring(d1, "second") == arrow.get(d1).floor("second").datetime)

    # print("microsecond:",   dt_ceiling(d0, "microsecond"),  arrow.get(d0).ceil("microsecond").datetime)

    print()
    print()
    print()

    d1 = date(2018, 10, 8)
    print("---------------------Date---------------------", d1)

    print("year:", dt_flooring(d1, "year"), arrow.get(d1).floor("year").date())
    print("month:", dt_flooring(d1, "month"), arrow.get(d1).floor("month").date())
    # print("day:",           dt_flooring(d1, "day"),          arrow.get(d1).floor("day").date())
    # print("hour:",          dt_flooring(d1, "hour"),         arrow.get(d1).floor("hour").date())
    # print("minute:",        dt_flooring(d1, "minute"),       arrow.get(d1).floor("minute").date())
    # print("second:",        dt_flooring(d1, "second"),       arrow.get(d1).floor("second").date())
    # print("microsecond:",   dt_ceiling(d0, "microsecond"),  arrow.get(d0).ceil("microsecond").date())
