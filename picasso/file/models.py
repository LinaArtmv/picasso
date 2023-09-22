from django.db import models

data = {
    'image': ['jpg', 'png', 'jpeg'],
    'text': ['txt', 'pdf', 'doc', 'docx'],
    'table': ['xls', 'xlsx'],
    'music': ['mp3', 'wav'],
    'video': ['mp4', 'avi']
}


def directory_path(instance, filename):
    name = filename.split('.')
    for element in data:
        if name[-1] in data[element]:
            return '{0}/{1}'.format(element, filename)
        return 'other/{0}'.format(filename)


class File(models.Model):
    """Модель Файл."""

    file = models.FileField('Загруженный файл',
                            upload_to=directory_path)
    uploaded_at = models.DateTimeField('Дата и время',
                                       auto_now_add=True)
    processed = models.BooleanField('Обработка',
                                    default=False)

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'Файлы'
