from django.conf.urls import patterns, url
from django.conf import settings
from views import *

urlpatterns = patterns(
        '',

        url(r'^quests/$', QuestList.as_view(), name='quest-list'),
        url(r'^quests/(?P<pk>[0-9]+)$', QuestDetail.as_view(), name='quest-list'),
        url(r'^add-quest$', AddQuest.as_view(), name='add-quest'),
        url(r'^monsters/$', MonsterList.as_view(), name='monster-list'),

        # Handling media files
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
