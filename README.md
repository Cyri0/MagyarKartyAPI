# Magyar KártyAPI

### Felhasználás

- Hozz létre egy új Django projectet.

- Klónozd le ezt a repository-t a Django projected szülőkönyvtárába.

- A projected __settings.py__ fájljába importáld be a kartyapi-t

```
INSTALLED_APPS = [
    ...
    'kartyapi',
]
```

- Állítsd be a projectedben az __urls.py__ ban a következőket:

```
from django.urls import include

urlpatterns = [
    path('', include('kartyapi.urls'))
]
```