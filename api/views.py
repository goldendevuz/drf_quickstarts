from drf_multiple_model.views import ObjectMultipleModelAPIView

from api.models import Play, Poem
from api.serializers import PlaySerializer, PoemSerializer


class TextAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Play.objects.all(), 'serializer_class': PlaySerializer},
        {'queryset': Poem.objects.filter(style='Sonnet'), 'serializer_class': PoemSerializer},
    ]