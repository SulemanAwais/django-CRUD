# 📝 TODOMaster - A Django TODO App

Welcome to the TODOMaster 🎉 ! This is a simple, user-friendly application built with Django that helps you manage your daily tasks effectively. 🚀
The deployed version of this app can be accessed here [🌐](https://suleman-todo.vercel.app/)

* 📦 Deployed on [Vercel](https://vercel.com/)

* 🔗 Database hosted on [Clever Cloud](https://www.clever-cloud.com)
## 🌟 Features

- ➕ **Add new tasks**
- ✏️ **Edit existing tasks**
- ❌ **Delete tasks**
- 📱 **Responsive design for all devices**

## 📂 Project Structure

```bash
django-CRUD/
│
├── CRUDapplication/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── manage.py
│
├── EMS/
│   └── # EMS-specific files
│
├── playground/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   ├── templates/
│   │   └── # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── db.sqlite3
├── build.sh
└── .gitignore
```
## 🛠️ Installation

### Prerequisites
- 🐍 Python 3.10+
- 📦 pip (Python package installer)
- 🌱 Git (for cloning the repository)
### Steps
#### 1. Clone the repository:
```bash
git clone https://github.com/SulemanAwais/django-CRUD.git
cd django-CRUD
```
#### 2. Create Virtual Environment 
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
#### 3. Install dependencies 
```bash
pip install -r requirements.txt
```
#### 4. Setup database
```bash
python manage.py migrate
```
#### 5. Run the Development server
```bash
python manage.py runserver
```
🎉 Open `http://127.0.0.1:8000` in your browser to see the app in action!

## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Big thanks to the Django community for their awesome documentation and tutorials.
- Icons and images from Devicon[https://devicon.dev].





