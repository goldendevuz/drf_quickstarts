from rest_framework import serializers

from api.models import Play, Poem


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ('genre', 'title', 'pages')


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ('title', 'stanzas')
