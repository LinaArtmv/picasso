from file.models import File
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .serializers import FileUploadSerializer


class FileViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Вьюсет для обработки данных."""

    queryset = File.objects.all()
    serializer_class = FileUploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data,
                                          context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
