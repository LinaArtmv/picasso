from django.core.files import File
from django.core.files.storage import FileSystemStorage
from file.models import File as model_file
from rest_framework import serializers

from .tasks import upload


class FileUploadSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с моделью File."""

    def validate_file(self, value):
        file = value
        if not file:
            raise serializers.ValidationError(
                {'file': 'Нужно прикрепить файл'})
        return value

    def create(self, validated_data):
        file = self.context.get('request').FILES['file']
        file_obj = model_file.objects.create(**validated_data)
        storage = FileSystemStorage()
        storage.save(file.name, File(file))
        upload.delay(file_id=file_obj.id,
                     path=storage.path(file.name),
                     file_name=file.name)
        return file_obj

    class Meta:
        model = model_file
        fields = ('file', 'uploaded_at', 'processed')
        read_only_fields = ('processed', )
