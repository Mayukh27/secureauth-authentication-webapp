CREATE DATABASE secure_auth;

USE secure_auth;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(255),
        failed_attempts INT DEFAULT 0
);