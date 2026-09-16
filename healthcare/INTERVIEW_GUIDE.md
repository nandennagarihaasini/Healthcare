# 🎙️ Healthcare REST API - Interview Guide

This guide contains the key talking points for explaining this project in a software engineering interview.

## 1. High-Level Overview
**Interviewer:** *"Tell me about the Healthcare REST API project you built."*

**Your Answer:**
> "I built a comprehensive backend API for a Healthcare Management System using Spring Boot. The system manages the core workflows of a hospital, tracking Patients, Doctors, Appointments, Prescriptions, Medical Records, and Billing. I used a layered architecture (Controller, Service, Repository) to maintain a clean separation of concerns, Spring Data JPA for data persistence in MySQL, and Spring Security to secure the endpoints."

## 2. Architecture & Design
**Interviewer:** *"How did you design the database and handle relationships?"*

**Your Answer:**
> "I modeled the database around real-world healthcare workflows using JPA annotations to handle relationships:
> - **Patient & Doctor → Appointment (`@ManyToOne`):** A patient and a doctor can have multiple appointments, so the `Appointment` entity acts as the join entity mapping both IDs.
> - **Appointment → Prescription / Billing (`@OneToOne`):** Each appointment generates exactly one prescription and one billing record.
> - **Patient → Medical Records (`@ManyToOne`):** A patient's medical history grows over time.
> I configured all entities to automatically update the database schema using Hibernate (`ddl-auto=update`)."

## 3. Validation & Exception Handling
**Interviewer:** *"How do you handle bad inputs or missing data?"*

**Your Answer:**
> "I implemented robust validation using Jakarta Validation (`@NotBlank`, `@NotNull`, `@Email`, `@FutureOrPresent`) directly on the Entity fields.
> For exception handling, instead of letting Spring Boot return its default white-label error page, I created a `@ControllerAdvice` class called `GlobalExceptionHandler`. 
> - If an invalid ID is queried, the Service throws a `ResourceNotFoundException`, which the handler converts into a clean JSON `404 Not Found` response.
> - If validation fails, it catches the `MethodArgumentNotValidException` and returns a `400 Bad Request` mapping out exactly which fields failed."

## 4. Security
**Interviewer:** *"How is the application secured?"*

**Your Answer:**
> "I implemented Spring Security with Basic Authentication. I configured a `SecurityFilterChain` that secures all `/api/**` endpoints, meaning clients (or Postman) must pass the correct `Authorization` header. I also specifically excluded the Swagger UI endpoints (`/v3/api-docs` and `/swagger-ui`) using `.permitAll()` so that documentation remains accessible without authentication."

## 5. API Documentation
**Interviewer:** *"How would frontend developers know how to use your API?"*

**Your Answer:**
> "I integrated `springdoc-openapi` which automatically reads my Controllers and generates a live, interactive Swagger UI page at `/swagger-ui.html`. This allows frontend developers to see exactly what JSON payloads are expected and even test the APIs directly from the browser."
