from rest_framework.serializers import ValidationError
from datetime import time


class ExecutionTimeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val > time(minute=2):
            raise ValidationError("This field cannot be greater than 120 seconds")


class PeriodValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val > 7:
            raise ValidationError("This field cannot be more than 7 days old")