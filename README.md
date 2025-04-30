# FocusFlow

FocusFlow is a productivity and mental health web app that helps users manage tasks, reduce stress, and stay focused. Features include a Pomodoro timer, journaling, daily affirmations, stress relief tips, and a personal progress tracker.

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/baoly25/focusflow.git
cd focusflow
```

### 2. Create a Virtual Environment:
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```

### 3. Apply Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Load Affirmations and Tips:
```bash
python manage.py load_affirmations
python manage.py load_tips
```

### 5. Run the Development Server:
```bash
python manage.py runserver
```

### 6. Open in Browser
```bash
http://127.0.0.1:8000/
```