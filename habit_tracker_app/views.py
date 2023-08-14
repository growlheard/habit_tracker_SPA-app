from rest_framework import generics

from habit_tracker_app.models import Habit
from habit_tracker_app.pagination import HabitPagination
from habit_tracker_app.permissions import IsPublicReadOnly, IsOwnerOrReadOnly
from habit_tracker_app.serializers import HabitSerializer


class HabitListView(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsPublicReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrReadOnly]


class HabitCreateView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsPublicReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitUpdateView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrReadOnly]


class HabitDeleteView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PublicHabitListView(generics.ListAPIView):
    queryset = Habit.objects.filter(public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
