from django.urls import path
from habit_tracker_app.views import (
    HabitListView,
    HabitDetailView,
    HabitCreateView,
    HabitUpdateView,
    HabitDeleteView,
    PublicHabitListView,
)

urlpatterns = [
    path('habits/', HabitListView.as_view(), name='habit-list'),
    path('habits/<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    path('habits/create/', HabitCreateView.as_view(), name='habit-create'),
    path('habits/<int:pk>/update/', HabitUpdateView.as_view(), name='habit-update'),
    path('habits/<int:pk>/delete/', HabitDeleteView.as_view(), name='habit-delete'),
    path('habits/public/', PublicHabitListView.as_view(), name='public-habit-list'),
    path('', HabitListView.as_view(), name='index'),
]