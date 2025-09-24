# Ajira Guild Management System

A Django-based job guild platform for jobseekers, employers, and admins. Includes job posting, applications, notifications, multilingual support, offline-friendly UI, and MySQL DB.

## Setup

1. Create and activate a virtualenv:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install requirements:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your DB credentials.
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the server:
   ```bash
   python manage.py runserver
   ```

## Mermaid Diagrams

### ERD
```
erDiagram
    USER ||--o{ JOB : posts
    USER ||--o{ APPLICATION : applies
    JOB ||--o{ APPLICATION : receives
    JOB }o--|| JOBCATEGORY : belongs_to

    USER {
      UUID id PK
      string username
      string email
      string role
    }
    JOB {
      UUID id PK
      string title
      text description
      date deadline
    }
    APPLICATION {
      UUID id PK
      text cover_letter
      string resume_path
      string status
    }
    JOBCATEGORY {
      UUID id PK
      string name
    }
```

### DFD
```
flowchart TD
  User -->|register/login| WebUI
  Employer -->|post job| WebUI
  WebUI -->|reads/writes| DjangoApp
  DjangoApp -->|queries| MySQL[(MySQL)]
  DjangoApp -->|sends| EmailServer((Email))
  DjangoApp -->|writes| NotificationsDB[(Notifications)]
  MobileApp -->|API calls| DjangoAPI
```

## Project Structure
- ajira_guild/
  - accounts/
  - jobs/
  - notifications/
  - training/
  - core/
  - templates/
  - static/
  - manage.py
  - requirements.txt
  - .env.example

## References
- [Django Project](https://docs.djangoproject.com/en/4.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [django-mysql](https://django-mysql.readthedocs.io/en/latest/)
