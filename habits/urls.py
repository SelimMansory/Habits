from rest_framework.routers import DefaultRouter
from habits.apps import HabitsConfig
from habits.views import HabitViewSet

app_name = HabitsConfig.name

router_habits = DefaultRouter()
router_habits.register(r'', HabitViewSet, basename='habit')

urlpatterns = [

] + router_habits.urls