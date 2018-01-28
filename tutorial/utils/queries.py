from datetime import datetime, date

from django.db.models import Q, F, When, Case,                                                              \
    Func, Value, ExpressionWrapper, Expression,                                                             \
    DateTimeField, CharField, IntegerField, BooleanField


# TODO: Support all expression types for:`StrfDatetimeExpressionWrapper` and not just F, Value.
class StrfDatetimeExpressionWrapper(ExpressionWrapper):
    def __init__(self, field_expression, format="%d/%m/%Y"):
        """
        :param field_expression: This should be a sub-class of Expression, defining the datetime value which is to be strftime(d).
        :param format: Acceptable datetime format in which result should be returned.
        :return: string type value of the `field_expression` in specified format.
        """

        if not any([isinstance(field_expression, F), isinstance(field_expression, Value)]):
            raise TypeError("\"{0}\": Expected input of type:\n\n {1} or \n {2}.".format(field_expression,
                                                                                         F,
                                                                                         Value)
                            )

        if isinstance(field_expression, Value) and not any([isinstance(field_expression.value, datetime),
                                                            isinstance(field_expression.value, date)]):
            raise TypeError("\"{0}\": Expected value of type:\n\n {1} or \n {2}.".format(field_expression.value,
                                                                                         datetime,
                                                                                         date))

        strf_func = Func(field_expression, Value(format), function='DATE_FORMAT')
        strf_expression = ExpressionWrapper(strf_func, output_field=CharField())

        super(StrfDatetimeExpressionWrapper, self).__init__(expression=strf_expression, output_field=CharField())


class MonthDiffExpressionWrapper(ExpressionWrapper):
    def __init__(self, field_expr_1, field_expr_2):
        """
        :param field_expr_1:
        :param field_expr_2:
        :return: Number of months in timedelta(field_expr_1 - field_expr_2). It will be integer type value (floor-ed).
        """
        field_expr_1 = StrfDatetimeExpressionWrapper(field_expr_1, "%Y%m")
        field_expr_2 = StrfDatetimeExpressionWrapper(field_expr_2, "%Y%m")

        month_diff_func = Func(field_expr_1, field_expr_2, function='PERIOD_DIFF')
        month_diff_expression = ExpressionWrapper(month_diff_func, output_field=IntegerField())

        super(MonthDiffExpressionWrapper, self).__init__(expression=month_diff_expression, output_field=IntegerField())
