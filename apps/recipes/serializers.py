from rest_framework import serializers
from models import *


class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag


class QuestSerializer(serializers.ModelSerializer):
    monsters = MonsterSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Quest

    # Create new quest
    def create(self, validated_data):
        monsters_data = validated_data.pop('monsters')
        tags_data = validated_data.pop('tags')
        quest = Quest.objects.create(**validated_data)
        for monster in monsters_data:
            try:
                monster = Monster.objects.get(name=monster["name"])
            except Monster.DoesNotExist:
                monster = Monster.objects.create(**monster)
            quest.monsters.add(monster)

        for tag in tags_data:
            try:
                tag = Tag.objects.get(name=tag["name"])
            except Tag.DoesNotExist:
                tag = Tag.objects.create(**tag)
            quest.tags.add(tag)

        return quest
