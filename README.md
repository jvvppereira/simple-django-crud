# 👥 Simple Django CRUD (Customer 360)

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Maintainability](https://qlty.sh/gh/jvvppereira/projects/simple-django-crud/maintainability.svg)](https://qlty.sh/gh/jvvppereira/projects/simple-django-crud)

A clean, modern, and lightweight Django-based Customer Relationship Management (CRM) app. Also known as **Customer 360**, this application offers an end-to-end dashboard to track customers, manage their contact information, log customer interactions (calls, emails, SMS, letters, social media), and view structured engagement analytics.

---

## ✨ Features

- **🗂️ Complete Customer CRM (CRUD):** Easily register, read, update, and manage customer records.
- **💬 Interaction History Logs:** Document every communication touchpoint (Inbound or Outbound) over various channels (Phone, Email, SMS, Letter, Social Media).
- **📊 Engagement Analytics:** Auto-generated 30-day analytics dashboard tracking overall interaction volume and breakdown by channel and direction.
- **🐳 Docker & Dev Containers Support:** Built-in `Dockerfile`, `requirements.txt`, and `.devcontainer` configuration for seamless containerized development or instant cloud deployment.
- **⚡ Clean UI / UX:** Responsive and interactive HTML templates.

---

## 🛠️ Tech Stack

- **Backend Framework:** Django 5.x (Python)
- **Database:** SQLite 3 (self-contained file, perfect for lightweight and rapid deployments)
- **Containerization:** Docker & VS Code Dev Containers
- **Frontend:** HTML5, CSS3, Bootstrap/Custom CSS for styling

---

## 🚀 Getting Started

### 📋 Prerequisites
Ensure you have the following installed on your machine:
- [Docker](https://www.docker.com/get-started) (Required for containerized execution/development)
- [VS Code](https://code.visualstudio.com/) + [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) (Highly recommended for the easiest development experience)

---

### Option 1: Development via Dev Containers (Recommended) 🐳

This project is fully configured for VS Code **Dev Containers**. This is the easiest way to start developing without worrying about local Python setups, dependencies, or database migrations, as everything is handled inside the container.

1. Open this project folder in **VS Code**.
2. When prompted with a notification in the bottom right saying *"Folder contains a Dev Container configuration. Reopen folder to develop in a container"*, click **Reopen in Container**.
   - *Alternatively, open the Command Palette (`Cmd+Shift+P` on macOS / `Ctrl+Shift+P` on Windows) and run `Dev Containers: Reopen in Container`.*
3. VS Code will build the container image, install Python extensions, forward port `8000`, and run database migrations automatically.
4. Open the integrated terminal inside VS Code and start the server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
5. Navigate to `http://localhost:8000/` in your browser.

---

### Option 2: Running with Standard Docker 🐳

If you prefer to run the application in the background as a standalone container:

1. **Build the Docker Image:**
   ```bash
   docker build -t simple-django-crud .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -d -p 8000:8000 --name django-crud-app simple-django-crud
   ```
   Open your browser and visit `http://localhost:8000/` to access the running application.

> [!NOTE]
> When running inside Docker, the SQLite database is local to the container instance. To persist data across container lifecycle events, you can mount the SQLite database file as a volume:
> `docker run -d -p 8000:8000 -v $(pwd)/db.sqlite3:/app/db.sqlite3 --name django-crud-app simple-django-crud`

---

## 📁 Project Structure

```text
simple-django-crud/
├── .devcontainer/          # VS Code Dev Container configuration
│   └── devcontainer.json   # Container settings, extensions, and hooks
├── customer360/            # Core Django Application & Project Settings
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML Templates (index, add, interact, summary, etc.)
│   ├── __init__.py
│   ├── asgi.py
│   ├── models.py           # Database Schema (Customer, Interaction)
│   ├── settings.py         # Django Settings Configuration
│   ├── urls.py             # URL Routes & Endpoints mapping
│   ├── views.py            # Business Logic & Controllers
│   └── wsgi.py
├── static/                 # Static Assets (CSS, JS, Images)
├── .gitignore              # Git ignore rules
├── db.sqlite3              # SQLite Database file
├── Dockerfile              # Containerization recipe
├── manage.py               # Django management utility
├── requirements.txt        # Python dependency manifest
└── README.md               # English Documentation (This file)
```

---

## 🗄️ Database Schema & Models

### 👤 Customer Model
Represents a customer profile in the system.
* `id` (AutoField, Primary Key)
* `name` (CharField, max 100)
* `email` (EmailField, max 100)
* `phone` (CharField, max 20)
* `address` (CharField, max 200)
* `social_media` (CharField, max 100, optional)

### 💬 Interaction Model
Represents a recorded communication touchpoint with a customer.
* `customer` (ForeignKey to Customer)
* `channel` (CharField, choices: `Phone`, `SMS`, `Email`, `Letter`, `Social Media`)
* `direction` (CharField, choices: `Inbound`, `Outbound`)
* `interaction_date` (DateField, auto-set to current date)
* `summary` (TextField)

---

## 🔗 Available Endpoints

| URL Route | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | **Dashboard / Customer List:** Displays all registered customers. |
| `/add` | `GET/POST` | **Add Customer:** Form to register a new customer profile. |
| `/interact/<int:cid>` | `GET/POST` | **Add Interaction:** Form to log a phone call, email, or other event for a specific customer (`cid`). |
| `/summary` | `GET` | **Interaction Summary:** Dashboard analytics showing breakdown of customer communications over the last 30 days. |

---

## 🛡️ License

This project is open-source and available under the [MIT License](LICENSE).
