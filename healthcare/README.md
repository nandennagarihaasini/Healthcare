# 🏥 Healthcare REST API

A fully functional Backend API for a Healthcare Management System built using Spring Boot, Spring Data JPA, and MySQL.

## 🚀 Features

- **Patient Management:** Complete CRUD operations.
- **Doctor Management:** Store and manage doctor details.
- **Appointments:** Schedule and track appointments (links Patient and Doctor).
- **Prescriptions:** Issue prescriptions tied to an appointment.
- **Medical Records:** Track history of diagnoses and treatments for a patient.
- **Billing:** Manage billing statuses and amounts tied to an appointment.

## 🛠️ Technology Stack

- **Java 21**
- **Spring Boot 3.x**
- **Spring Web** (REST APIs)
- **Spring Data JPA** (Hibernate)
- **Spring Security** (Basic Authentication)
- **MySQL** (Relational Database)
- **Lombok** (Boilerplate reduction)
- **Jakarta Validation** (Input sanitization)
- **Swagger / OpenAPI** (API Documentation)

## 📦 How to Run

1. **Database Setup**
   Ensure MySQL is running and create the database:
   ```sql
   CREATE DATABASE healthcare_db;
   ```

2. **Configuration**
   The application is configured to connect to `localhost:3306` with username `root` and password `root`. You can modify these in `src/main/resources/application.properties`.

3. **Run Application**
   ```bash
   ./mvnw spring-boot:run
   ```

4. **Access the API**
   - The application runs on `http://localhost:8080`.
   - All API endpoints under `/api/**` require Basic Authentication.
   - **Username:** `admin`
   - **Password:** `admin123`

## 📖 API Documentation (Swagger)

Once the application is running, open your browser and navigate to:
**[http://localhost:8080/swagger-ui.html](http://localhost:8080/swagger-ui.html)**

## 🧪 Postman Testing

A `Healthcare_Postman_Collection.json` file is provided in the root directory. 
1. Open Postman.
2. Click **Import** and select the JSON file.
3. Don't forget to configure Basic Auth in Postman (`admin` / `admin123`) before sending requests.
