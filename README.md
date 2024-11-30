# Task Management App

A Django-based task management app that allows users to log in with Google OAuth, and perform CRUD operations on tasks.

## Features
- **Google OAuth Login**: Secure authentication using Google accounts.
- **Task Management**:
  - Create tasks with a title and description.
  - View a list of all tasks.
  - Edit and delete tasks.
- **Admin Features**:
  - Manage users and tasks.
  - Store Google OAuth keys.
- **Responsive Design**: Aesthetic and user-friendly interface.

---

## Tech Stack
- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Authentication**: Google OAuth via `social-auth-app-django`

---

## Setup Instructions

### Prerequisites
- Python 3.8 or above installed on your system.
- A Google Cloud project with OAuth credentials.

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/task-management-app.git
cd task-management-app
