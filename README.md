# RESTful-VPS-Control-API

# installation

### with docker
```docker compose -f docker-compose.yml up -d --build```

### without docker
```PYTHONPATH=$(pwd) poetry run python app/manage.py runserver 0.0.0.0:8080```

# migrations

### with docker
```docker compose exec drf_service python app/manage.py migrate```

### without docker
```poetry run python app/manage.py migrate```
