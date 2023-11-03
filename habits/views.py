from habits.models import Habit
from rest_framework import viewsets
from habits.pagination import MyPagination
from habits.permissions import HabitsPermission
from habits.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, HabitsPermission]
    serializer_class = HabitSerializer
    pagination_class = MyPagination

    def perform_create(self, serializer):
        new_object = serializer.save()
        new_object.owner = self.request.user
        new_object.save()

    def list(self, request, *args, **kwargs):
        habit_owner = Habit.objects.filter(owner=self.request.user)
        habit_true = Habit.objects.filter(is_publish=True)
        habit_filter = habit_true | habit_owner
        paginator = MyPagination()
        result_page = paginator.paginate_queryset(habit_filter, request)
        serializer = HabitSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)