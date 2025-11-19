# Writer's Den Backend

The backend server for Writer's Den, a note-taking app designed specifically for writers to capture and organize story ideas. Built with Django Rest Framework and PostgreSQL for robust performance and full-text search capabilities.

## Tech Stack

- Python
- Django Rest Framework
- PostgreSQL (Neon Postgres)
- OAuth 2.0 with Google authentication

## Features

- Full-text search implementation for notes/ideas
- JWT and OAuth authentication using Simple JWT and Djoser
- RESTful API endpoints for managing writing projects and ideas
- Secure session cookie handling

## Requirements

- Python 3.8+
- PostgreSQL (or SQLite for local development)
- Google OAuth credentials

## Installation

1. Clone the repository

```bash
git clone https://github.com/inatgomez/dens-api.git
cd densapp
```

2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set up environment variables

Create a `.env.local` file in the `densapp` directory with the following variables:

```
# Development Environment Variables
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
AUTH_COOKIE_SECURE=False

# Authentication
AUTH_COOKIE_DOMAIN=localhost
AUTH_COOKIE_SAMESITE=Strict
GOOGLE_AUTH_KEY=your_google_auth_key
GOOGLE_AUTH_SECRET_KEY=your_google_auth_secret_key
REDIRECT_URLS=http://localhost:3000/auth/google

# Database (for Neon PostgreSQL)
PGDATABASE=your_database_name
PGUSER=your_database_user
PGPASSWORD=your_database_password
PGHOST=your_database_host
PGPORT=5432
```

5. Database Setup

For a simpler local setup, you can modify `settings.py` to use SQLite:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Or keep the PostgreSQL configuration if you have a PostgreSQL server:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('PGDATABASE'),
        'USER': getenv('PGUSER'),
        'PASSWORD': getenv('PGPASSWORD'),
        'HOST': getenv('PGHOST'),
        'PORT': getenv('PGPORT', 5432),
        'OPTIONS': {
            'sslmode': 'require',
        },
        'DISABLE_SERVER_SIDE_CURSORS': True,
    }
}
```

6. Run migrations

```bash
python manage.py migrate
```

7. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

## Running the Server

```bash
python manage.py runserver
```

The server will be available at http://localhost:8000/

## Google Authentication Setup

To enable Google authentication:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Navigate to "APIs & Services" > "Credentials"
4. Create an OAuth 2.0 Client ID
5. Set the authorized redirect URI to `http://localhost:3000/auth/google`
6. Copy the Client ID and Client Secret to your `.env` file as `GOOGLE_AUTH_KEY` and `GOOGLE_AUTH_SECRET_KEY`

## Authentication Configuration

The application uses Djoser and JWT for authentication with the following configuration:

- Access tokens expire after 5 minutes
- Refresh tokens expire after 24 hours
- Supports Google OAuth2 authentication
- CORS is configured for local development

## Related Projects

- [Writer's Den Frontend](https://github.com/inatgomez/dens-front-end.git): Next.js frontend for this application

## Deployment Notes

When deploying to production:

1. Set `DEBUG=False` in environment variables
2. Set `AUTH_COOKIE_SECURE=True` for production
3. Update `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS` to match your production domains
4. Consider using a production-ready database
5. Be aware of latency issues with free-tier hosting services (2-5 min server startup time possible)

Read the full case study [here](https://github.com/inatgomez/dens-front-end/blob/main/CASE_STUDY.md)
