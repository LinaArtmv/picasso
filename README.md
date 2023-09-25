## Реализовано REST API для взаимодействия с базой данных.

## Технологии

- [Python 3.10](https://www.python.org/downloads/)
- [Django 3.2](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [Redis](https://redis.io/docs/)

# Пример ответа на POST-запрос на адрес https://linaart.sytes.net/api/upload/: 
```
{
    "file": "http://127.0.0.1:8000/data/data/image/mannik_na_prostokvashe-557490_VoYrXqh.jpeg",
    "uploaded_at": "2023-09-22T03:55:09.735416Z",
    "processed": false
}
```

# Пример GET-запроса на адрес https://linaart.sytes.net/api/files/:

Пример ответа:

```
{
    "file": "http://127.0.0.1:8000/data/data/image/mannik_na_prostokvashe-557490_VoYrXqh.jpeg",
    "uploaded_at": "2023-09-22T03:55:09.735416Z",
    "processed": true
},
{
    "file": "http://127.0.0.1:8000/data/data/image/oladi-na-skoruu-ruku-bez-drojjei_1588187288_9_max.jpg",
    "uploaded_at": "2023-09-22T07:51:14.543794Z",
    "processed": true
}

```


### Автор
- Ангелина Артемьева, github: [LinaArtmv](https://github.com/LinaArtmv)
