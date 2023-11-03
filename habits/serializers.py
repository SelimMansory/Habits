from rest_framework import serializers
from habits.models import Habit
from habits.validators import ExecutionTimeValidator, PeriodValidator


class HabitSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if (data.get('binding_habit', None) and data.get('reward', None)) is not None:
            raise serializers.ValidationError(
                "only one of the fields 'binding_habit' or 'reward' can be used")
        elif (data.get('pleasant_habit', None) is True and (
                data.get('binding_habit', None) or data.get('reward', None))
              is not None):
            raise serializers.ValidationError(
                "pleasant_habit can't have reward or binding_habit")
        elif data.get('binding_habit', None) is not None:
            if data.get('binding_habit', None).pleasant_habit is False:
                raise serializers.ValidationError("binding_habit must have the True attribute of a pleasant_habit")
            else:
                return data
        else:
            return data

    class Meta:
        model = Habit
        fields = ('place', 'time', 'action', 'pleasant_habit', 'binding_habit', 'period', 'reward', 'execution_time',
                  'is_publish')
        validators = [ExecutionTimeValidator(field='execution_time'), PeriodValidator(field='period')]