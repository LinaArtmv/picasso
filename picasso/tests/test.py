import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from file.models import File

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


class URLTest(TestCase):
    """Проверка доступности url."""

    def setUp(self):
        self.guest_client = Client()

    def test_upload_url_exists(self):
        """Проверка доступности адреса /api/upload/."""
        response = self.guest_client.get('/api/upload/')
        self.assertEqual(response.status_code, 405)

    def test_files_url_exists(self):
        """Проверка доступности адреса /api/files/."""
        response = self.guest_client.get('/api/files/')
        self.assertEqual(response.status_code, 200)


class ModelTest(TestCase):
    """Проверка модели File."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.file = File.objects.create(
            file='http://127.0.0.1:8000/data/image/test.jpeg')

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        file = ModelTest.file
        field_verboses = {
            'file': 'Загруженный файл',
            'uploaded_at': 'Дата и время',
            'processed': 'Обработка'}
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    file._meta.get_field(field).verbose_name, expected_value)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class FileCreateTest(TestCase):
    """Проверка создания объекта модели File."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.file = File.objects.create(
            file='http://127.0.0.1:8000/data/image/test.jpeg')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        self.guest_client = Client()

    def test_create_object(self):
        """Валидная форма создает запись в File."""
        files_count = File.objects.count()
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B')
        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif')
        form_data = {
            'file': uploaded}
        response = self.guest_client.post(
            path='/api/upload/',
            data=form_data,
            follow=True)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(File.objects.count(), files_count + 1)
        self.assertTrue(
            File.objects.filter(
                file='http://127.0.0.1:8000/data/image/test.jpeg').exists())
