# Karate Federation Management System

A Django-based web application designed to manage a Karate Federation's data, including clubs, athletes, coaches, and competitive teams.

## 🥋 Features

- **Clubs Management**:
  - Dashboard with search and pagination for easy navigation.
  - CRUD operations for clubs (Create, Read, Update, Delete).
  - Detailed club profiles showing statistics, athletes, and teams.
- **Athletes & Coaches**:
  - Track athletes' belts, personal info, and club affiliations.
  - Manage coaching staff for each club.
- **Competitive Teams**:
  - Register teams of exactly 3 athletes from the same club.
  - Direct management of teams from the club's detail page.
- **Modern UI**:
  - Responsive design with a dedicated dashboard for each category.
  - Clean, styled forms and intuitive navigation.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, Vanilla CSS, Django Template Language
- **Database**: PostgreSQL
- **Media**: Image uploads for clubs, athletes, and coaches.

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd karateFederation
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` in your browser to see the application!

## 📂 Project Structure

- `karateFederation/`: Core settings and URL configurations.
- `clubs/`: Management of Karate clubs and competitive teams.
- `athletes/`: Athlete and Team model definitions.
- `coaches/`: Coach management logic.
- `common/`: Shared mixins, validators, and context processors.
- `templates/`: Global and app-specific HTML templates.
- `static/`: CSS styles and static assets.

## 📝 License

This app is part of a training project for SoftUni, Bulgaria.
