# 🚀 High-Availability Traffic Monitor
**A Pro-Grade DevOps Stack: Nginx + Flask + Redis**

## 🏗️ Architecture
This project demonstrates a production-ready containerized environment:
* **Nginx:** Reverse proxy handling traffic on Port 80.
* **Flask:** Backend API processing logic on Port 5002 (Isolated).
* **Redis:** High-speed in-memory database for hit tracking.
* **GitHub Actions:** Automated CI/CD pipeline verifying builds on every push.

## 🛠️ Tech Stack
- **Infrastructure:** Docker, Docker Compose
- **Web Server:** Nginx
- **Backend:** Python (Flask)
- **Database:** Redis
- **CI/CD:** GitHub Actions

## 🚦 How to Run
1. Clone the repo.
2. Run `docker-compose up -d`.
3. Access via `http://localhost`.
