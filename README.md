# Doctor Appointment Booking System (DABS)

DABS is a Django-based web application that lets patients search for doctors, book appointments online, and lets doctors and admins manage bookings through dedicated dashboards. It was built as a full-stack project (Python/Django backend with HTML, CSS, and JavaScript on the frontend) covering three separate user roles: **Patient**, **Doctor**, and **Admin**.

## Features

### Patient
- Sign up and log in to a personal account
- Browse available doctors and book an appointment by selecting doctor, date, time, and reason for visit
- Automatic slot-limit check — booking is blocked once a doctor's slots for a given date are full (max 10/day)
- View "About Us" and general site info

### Doctor
- Doctor registration and login
- Dedicated doctor dashboard showing all appointments booked with that doctor
- Empty-state view when no appointments exist yet

### Admin
- Admin sign up and login
- Central dashboard listing every appointment in the system
- Edit or delete any appointment record
- Manage (view/delete) registered doctors

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Database | SQLite (Django ORM) |
| Frontend | HTML, CSS, JavaScript (Django Templates) |
| Auth | Custom username/password checks against the database |

## Project Structure

```
Doctor-Appointment-Booking-System-DABS-/
├── dproject/                  # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── dproject1/                 # Main application
│   ├── models.py              # appointment, userdata, admin, doc models
│   ├── views.py                # Business logic for booking, login, dashboards
│   ├── urls.py                  # App-level URL routes
│   ├── form.py                   # Sign-up form
│   ├── templates/                 # HTML pages (home, login, dashboards, etc.)
│   ├── static/                     # CSS, JS, and image assets
│   └── migrations/
├── manage.py
└── requirements.txt
```

## Core Models

- **appointment** — stores patient booking details (name, email, address, phone, age, gender, chosen doctor, fee, date, time, reason)
- **userdata** — patient account details for login/signup
- **admin** — admin account details
- **doc** — registered doctor credentials

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Prabhat2811/Doctor-Appointment-Booking-System-DABS-.git
   cd Doctor-Appointment-Booking-System-DABS-
   ```

2. (Optional but recommended) Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations
   ```bash
   python manage.py migrate
   ```

5. Run the development server
   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser at `http://127.0.0.1:8000/`

## Usage

- Visit the home page to browse the platform and use the navigation bar to reach **Login**, **Sign Up**, **Doctor Login**, and **Admin Login**.
- Patients sign up, log in, and book an appointment with a doctor of their choice.
- Doctors log in to view the appointments booked with them on their dashboard.
- Admins log in to view, edit, or delete any appointment, and to manage registered doctors.

## Roadmap / Possible Improvements

- Migrate authentication to Django's built-in `auth` system with hashed passwords
- Move raw `GET`-based form submissions to Django `ModelForm`s with server-side validation
- Add email/SMS appointment confirmations
- Add payment gateway integration for consultation fees
- Add pagination and search/filter for the admin dashboard

## Author

**Prabhat Ranjan**
- GitHub: [Prabhat2811](https://github.com/Prabhat2811)
- LinkedIn: [prabhat-ranjan-29801422a](https://linkedin.com/in/prabhat-ranjan-29801422a)
- LeetCode: [Prabhat2811](https://leetcode.com/u/Prabhat2811/)
