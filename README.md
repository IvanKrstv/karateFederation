# Karate Federation Management System

A Django-based web application designed to manage a Karate Federation's data, including clubs, athletes, coaches, and competitive teams.

**[Visit the deployed version here](http://16.170.99.142/)**
## Features

- **Clubs Management** — CRUD operations, dashboard with search and pagination, detailed club profiles with athletes and teams.
- **Athletes & Coaches** — Track belts, personal info, club affiliations, and coaching staff.
- **Competitive Teams** — Register teams of athletes from the same club, managed from the club detail page.
- **Tournaments** — Create and manage tournaments with participating teams.
- **User Accounts** — Registration, login, logout with a custom user model (extended AbstractUser).
- **Role-based Permissions** — Three user groups: Viewer (view only), Editor (add/change), Manager (full CRUD).
- **REST API** — Athletes endpoint with filtering by belt, gender, and club. Permissions tied to Django groups.
- **Async Tasks** — Welcome email sent via Celery + Redis on user registration.
- **Modern UI** — Responsive design with dedicated dashboards and intuitive navigation.

## Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Task Queue**: Celery + Redis
- **Database**: PostgreSQL
- **Frontend**: HTML5, Vanilla CSS, Django Template Language
- **Web Server**: Nginx + Gunicorn
- **Containerization**: Docker, Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- Redis

### Local Development

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd karateFederation
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your credentials:
   ```
   SECRET_KEY=your-secret-key
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASS=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Start the Celery worker** (in a separate terminal):
   ```bash
   celery -A karateFederation worker --loglevel=info
   ```

Visit `http://127.0.0.1:8000/` in your browser.

### Docker Deployment

1. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Make sure `DB_HOST=db` and `CELERY_BROKER_URL=redis://redis:6379/0` for Docker networking.

2. **Build and start all services**:
   ```bash
   docker-compose up --build
   ```

   This starts: Django (Gunicorn), PostgreSQL, Redis, Celery worker, and Nginx.

3. **Create a superuser**:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

Visit `http://localhost/` in your browser.

## User Groups

Three groups are created automatically via migrations:

| Group | Permissions |
|---|---|
| Viewer | View only |
| Editor | Add, change, view |
| Manager | Add, change, delete, view |

Assign users to groups via Django Admin at `/admin/`.

## REST API

Base URL: `/athletes/api/`

| Method | Endpoint | Description | Permission |
|---|---|---|---|
| GET | `/athletes/api/` | List all athletes | Anyone |
| POST | `/athletes/api/` | Create athlete | Editor, Manager |
| GET | `/athletes/api/<id>/` | Retrieve athlete | Anyone |
| PATCH | `/athletes/api/<id>/` | Update athlete | Editor, Manager |
| DELETE | `/athletes/api/<id>/` | Delete athlete | Manager |

**Query filters:**
- `?belt=black`
- `?gender=m`
- `?club_id=1`
- Filters can be combined: `?belt=black&gender=m`

## Project Structure

```
karateFederation/   # Core settings, URLs, Celery config
accounts/           # Custom user model, registration, login, logout
clubs/              # Clubs and teams management
athletes/           # Athletes, teams, REST API
coaches/            # Coach management
tournaments/        # Tournament management
common/             # Shared validators, mixins, context processors
templates/          # Global and app-specific HTML templates
static/             # CSS styles and static assets
nginx/              # Nginx configuration
```

## Running Tests

```bash
python manage.py test accounts common clubs athletes
```

## License

This app is part of a training project for SoftUni, Bulgaria.
