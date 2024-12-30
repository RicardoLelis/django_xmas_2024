from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import LanguageSerializer, LanguageDescSerializer
from .models import Language

@api_view(['GET'])
def get_languages(request):
    languages = Language.objects.all()
    serializer = LanguageSerializer(languages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_language_desc(request, pk):
    language = Language.objects.get(id=pk)
    serializer = LanguageDescSerializer(language, many=False)
    return Response(serializer.data)

