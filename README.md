# SecureAuth – Authentication Web Application with Rate Limiting

SecureAuth is a backend-focused web application designed to demonstrate secure authentication mechanisms and cyber security fundamentals.  
The project implements user registration and login with encrypted password storage and login rate limiting to prevent brute-force attacks.

This project was developed as part of hands-on learning in backend development and security concepts.

---

## 🔐 Features

- User registration and login system  
- Secure password hashing using **bcrypt**  
- Login attempt rate limiting (brute-force protection)  
- Session-based authentication  
- MySQL database integration  
- Simple and clean web interface  

---

## 🧱 Tech Stack

- **Backend:** Python, Flask  
- **Database:** MySQL  
- **Security:** bcrypt password hashing  
- **Frontend:** HTML, CSS  
- **Tools:** Git, GitHub  

---

## 📁 Project Structure
```
secure-auth-webapp/
│
├── app.py
├── requirements.txt
│
├── templates/
│ ├── register.html
│ ├── login.html
│ └── dashboard.html
│
└── static/
└── style.css
```

## ⚙️ Database Schema

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    failed_attempts INT DEFAULT 0
);
```

**▶️ How to Run the Project**

1. Install dependencies
```
pip install -r requirements.txt
```
2. Create MySQL database
```
CREATE DATABASE secure_auth;
```
3. Update database credentials in app.py
```
host="localhost"
user="root"
password="your_password"
database="secure_auth"
```
4. Run the application
```
python app.py
```
5. Open in browser
```
http://127.0.0.1:5000
```
**🛡️ Security Concepts Implemented**

Password encryption using bcrypt hashing

Prevention of brute-force login attempts using rate limiting

Secure credential storage

Session-based access control


**🎯 Learning Outcomes**

Understanding of authentication workflows

Practical implementation of cryptographic hashing

Backend development using Flask

Integration of MySQL with web applications

Awareness of basic cyber security best practices


**👤 Author**

Mayukh Ghosh

B.Tech Computer Science Engineering (2027 Batch)

GitHub: https://github.com/Mayukh27

LinkedIn: https://www.linkedin.com/in/mayukh-g27
