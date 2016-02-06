from rest_framework import generics
from serializers import *


class QuestList(generics.ListCreateAPIView):
    serializer_class = QuestSerializer
    queryset = Quest.objects.all()


class QuestDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestSerializer
    queryset = Quest.objects.all()


class AddQuest(generics.CreateAPIView):
    serializer_class = QuestSerializer
    queryset = Quest.objects.all()


class MonsterList(generics.ListCreateAPIView):
    serializer_class = MonsterSerializer
    queryset = Monster.objects.all()
