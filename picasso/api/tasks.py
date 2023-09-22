from pathlib import Path
from time import sleep

from celery import shared_task
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from file.models import File as model_file


@shared_task()
def upload(file_id, path, file_name):
    print('Uploading file...')
    sleep(10)
    storage = FileSystemStorage()
    path_object = Path(path)

    with path_object.open(mode='rb') as file:
        pict = File(file, name=path_object.name)
        instance = model_file.objects.get(id=file_id)
        instance.processed = True
        instance.file = pict
        instance.save()

    storage.delete(file_name)
    print('Uploaded!')
