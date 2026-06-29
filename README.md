# 📚 Library API — Django REST Framework Project

A production-ready **RESTful API** for a library book management system, built with **Django 6.0**, **Django REST Framework**, and deployed on **Railway**. Features full CRUD operations, token-based authentication, user registration/login via `dj-rest-auth`, and interactive API documentation with **Swagger UI** and **ReDoc**.

🌐 **Live Demo:** [librarydrf-project-production.up.railway.app](https://librarydrf-project-production.up.railway.app)

---

## 🔗 Live Demo

| Link | Description |
|---|---|
| [🏠 App Root](https://librarydrf-project-production.up.railway.app/) | Live deployed application |
| [📖 Swagger UI](https://librarydrf-project-production.up.railway.app/swagger/) | Interactive API explorer |
| [📄 ReDoc](https://librarydrf-project-production.up.railway.app/redoc/) | Alternative API documentation |
| [⚙️ Admin Panel](https://librarydrf-project-production.up.railway.app/admin/) | Django admin interface |

---

## 🚀 Features

- **Full CRUD API** — Create, Read, Update, Delete books via REST endpoints
- **ModelViewSet + Router** — Auto-generated URL patterns using DRF's `SimpleRouter` and `ModelViewSet`
- **Custom APIView implementations** — Manual `APIView` classes for List, Detail, Create, Update, Delete (alongside `generics` alternatives shown in comments)
- **Serializer Validation** — Custom `validate()` and field-level `validate_price()` methods with duplicate detection
- **Token Authentication** — Session + Token auth via DRF's built-in authentication classes
- **User Registration & Login** — Full auth flow via `dj-rest-auth` and `django-allauth` (including social account support)
- **Swagger UI** — Interactive API explorer at `/swagger/`
- **ReDoc** — Alternative API documentation at `/redoc/`
- **Whitenoise** — Static file serving for production without a separate web server
- **Gunicorn** — Production WSGI server
- **Railway Deployment** — Configured with `Procfile`, `ALLOWED_HOSTS`, and `CSRF_TRUSTED_ORIGINS` for Railway cloud platform
- **Permission Control** — Global `IsAuthenticated` permission enforced across all endpoints
- **Function-Based View** — Example `@api_view` implementation included alongside class-based alternatives

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.14 |
| **Framework** | Django 6.0.6 |
| **REST API** | Django REST Framework 3.17 |
| **Auth** | dj-rest-auth, django-allauth, DRF Token Auth |
| **API Docs** | drf-yasg (Swagger UI + ReDoc) |
| **Database** | SQLite3 (dev) |
| **Static Files** | Whitenoise |
| **WSGI Server** | Gunicorn |
| **Deployment** | Railway |
| **Package Manager** | Pipenv |

---

## 📁 Project Structure

```
Library_DRF_project/
├── library_project/          # Django project config
│   ├── settings.py           # Auth, DRF, Whitenoise, Railway config
│   ├── urls.py               # Root URLs: API, auth, Swagger, ReDoc
│   └── wsgi.py
│
├── books/                    # Books API app
│   ├── models.py             # Book model
│   ├── Serializers.py        # BookSerializer with custom validation
│   ├── views.py              # APIView & generics & ModelViewSet implementations
│   ├── urls.py               # Router + URL patterns
│   └── admin.py
│
├── requirements.txt          # Pinned production dependencies
├── Pipfile                   # Dev dependency manager
├── Procfile.txt              # Gunicorn start command for Railway
├── runtime.txt               # Python 3.14 runtime declaration
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/aziz-200/Library__DRF-project.git
cd Library__DRF-project
```

### 2. Install dependencies
```bash
pip install pipenv
pipenv install
pipenv shell
```

Or with pip directly:
```bash
pip install -r requirements.txt
```

### 3. Apply migrations
```bash
python manage.py migrate
```

### 4. Create a superuser
```bash
python manage.py createsuperuser
```

### 5. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/swagger/` to explore the API interactively.

---

## 📦 Dependencies

```
Django==6.0.6
djangorestframework==3.17.1
dj-rest-auth==7.2.0
django-allauth==65.18.0
drf-yasg==1.21.15
gunicorn==26.0.0
whitenoise==6.12.0
PyJWT==1.7.1
```

Install all:
```bash
pipenv install
```

---

## 🔐 Authentication

The API uses **Token Authentication** and **Session Authentication** (configured globally).

All endpoints require authentication by default (`IsAuthenticated`).

### Register
```
POST /api/v1/dj-rest-auth/registration/
```

### Login (get token)
```
POST /api/v1/dj-rest-auth/login/
```

### Logout
```
POST /api/v1/dj-rest-auth/logout/
```

Include the token in requests:
```
Authorization: Token <your_token_here>
```

---

## 📌 API Endpoints

All endpoints are prefixed with `/api/v1/`.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/books/` | List all books |
| `POST` | `/api/v1/books/` | Create a new book |
| `GET` | `/api/v1/books/{id}/` | Retrieve a book by ID |
| `PUT` | `/api/v1/books/{id}/` | Full update a book |
| `PATCH` | `/api/v1/books/{id}/` | Partial update a book |
| `DELETE` | `/api/v1/books/{id}/` | Delete a book |
| `POST` | `/api/v1/dj-rest-auth/login/` | Login & get token |
| `POST` | `/api/v1/dj-rest-auth/logout/` | Logout |
| `POST` | `/api/v1/dj-rest-auth/registration/` | Register new user |
| `GET` | `/swagger/` | Swagger UI docs |
| `GET` | `/redoc/` | ReDoc API docs |

---

## 🗄️ Data Model

### Book

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `title` | CharField(200) | Book title |
| `subtitle` | CharField(200) | Book subtitle |
| `content` | TextField | Book description/content |
| `author` | CharField(200) | Author name |
| `isbn` | CharField(20) | ISBN number |
| `price` | DecimalField | Price (max 1000, must be > 0) |

---

## ✅ Serializer Validation Rules

- **Title** must contain alphabetic characters only
- **Duplicate check** — title + author combination must be unique in the database
- **Price** must be greater than `0` and not exceed `1000`

---

## 🌍 Deployment (Railway)

The project is configured for deployment on [Railway](https://railway.app):

- `Procfile.txt` — defines `gunicorn` as the web process
- `runtime.txt` — specifies Python 3.14
- `ALLOWED_HOSTS` includes `librarydrf-project-production.up.railway.app`
- `CSRF_TRUSTED_ORIGINS` set for HTTPS on Railway domain
- `Whitenoise` handles static files without a CDN
- `DEBUG` is controlled via environment variable

---

## 🔄 View Architecture

The project demonstrates **three DRF view patterns** side by side:

```python
# 1. Generic views (concise, less control)
class BookListApiView(generics.ListCreateAPIView): ...

# 2. Manual APIView (full control)
class BookListApiView(APIView):
    def get(self, request): ...

# 3. ModelViewSet + Router (auto URL generation)
class BookViewSet(ModelViewSet): ...
```

This makes the codebase a great learning reference for comparing DRF approaches.

---

## 👤 Author

**Aziz** — [azizaxtamov0201@gmail.com](mailto:azizaxtamov0201@gmail.com) · [github.com/aziz-200](https://github.com/aziz-200)
