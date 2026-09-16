# Healthcare Management System REST API
## Project Documentation

**Project Name:** Healthcare Management System REST API  

**Technology Stack:**
- Java 21
- Spring Boot 4.1.1 / 3.x
- Spring Data JPA (Hibernate)
- MySQL / H2 Relational Database
- Maven
- Lombok
- Jakarta Validation
- Spring Security (Basic Authentication)
- Springdoc OpenAPI (Swagger UI)
- Postman (API Testing)

---

## 1. Project Overview
The **Healthcare Management System REST API** is a backend application developed using Spring Boot. It enables the management of patients, doctors, appointments, prescriptions, medical records, and billing through RESTful APIs.

The application follows a layered architecture consisting of Controller, Service, Repository, and Entity layers to ensure clean code organization and maintainability.

---

## 2. Objectives
- Manage patient personal and demographic information.
- Register and maintain doctor profiles and medical specialties.
- Schedule, manage, and track hospital appointments.
- Issue and track digital prescriptions tied to consultations.
- Maintain clinical medical records and patient treatment histories.
- Record billing invoices, amounts, and payment statuses.
- Provide REST APIs for complete CRUD operations.
- Maintain relationships and referential integrity between entities using Spring Data JPA.

---

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| **Java 21** | Primary Object-Oriented Programming Language |
| **Spring Boot** | Enterprise Backend Framework |
| **Spring Data JPA** | Database Operations & ORM |
| **MySQL / H2** | Relational Database Management System |
| **Maven** | Dependency & Build Management |
| **Lombok** | Reduces Boilerplate Code (`@Data`, `@Builder`) |
| **Jakarta Validation** | Input Validation (`@NotBlank`, `@Email`) |
| **Spring Security** | Basic Authentication & API Protection |
| **Springdoc OpenAPI** | Interactive Swagger UI Documentation |
| **Postman** | API Testing & Verification |

---

## 4. Project Architecture

```text
Client (Postman / Browser)
         │
         ▼
 Controller Layer
         │
         ▼
   Service Layer
         │
         ▼
 Repository Layer
         │
         ▼
Database (MySQL / H2)
```

---

## 5. Project Structure

```text
HealthcareManagementSystem
│
├── controller
│   ├── PatientController.java
│   ├── DoctorController.java
│   ├── AppointmentController.java
│   ├── PrescriptionController.java
│   ├── MedicalRecordController.java
│   └── BillingController.java
│
├── entity
│   ├── Patient.java
│   ├── Doctor.java
│   ├── Appointment.java
│   ├── Prescription.java
│   ├── MedicalRecord.java
│   └── Billing.java
│
├── repository
│   ├── PatientRepository.java
│   ├── DoctorRepository.java
│   ├── AppointmentRepository.java
│   ├── PrescriptionRepository.java
│   ├── MedicalRecordRepository.java
│   └── BillingRepository.java
│
├── service
│   ├── PatientService.java
│   ├── DoctorService.java
│   ├── AppointmentService.java
│   ├── PrescriptionService.java
│   ├── MedicalRecordService.java
│   └── BillingService.java
│
├── exception
│   ├── ResourceNotFoundException.java
│   └── GlobalExceptionHandler.java
│
├── config
│   └── SecurityConfig.java
│
└── HealthcareApplication.java
```

---

## 6. Database Design

### Patient
| Field | Type |
|---|---|
| `id` | Long (Primary Key) |
| `name` | String |
| `dob` | LocalDate |
| `gender` | String |
| `contact` | String |
| `address` | String |
| `createdAt` | LocalDateTime |

### Doctor
| Field | Type |
|---|---|
| `id` | Long (Primary Key) |
| `name` | String |
| `specialization` | String |
| `phone` | String |
| `email` | String |

### Appointment
| Field | Type |
|---|---|
| `id` | Long (Primary Key) |
| `patient` | Foreign Key (`Patient`) |
| `doctor` | Foreign Key (`Doctor`) |
| `appointmentDate` | LocalDateTime |
| `reason` | String |
| `status` | String |

### Prescription
| Field | Type |
|---|---|
| `id` | Long (Primary Key) |
| `appointment` | Foreign Key (`Appointment`, Unique) |
| `medication` | String |
| `dosage` | String |
| `instructions` | String |

### Medical Record
| Field | Type |
|---|---|
| `id` | Long (Primary Key) |
| `patient` | Foreign Key (`Patient`) |
| `diagnosis` | String |
| `treatment` | String |
| `recordDate` | LocalDateTime |

### Billing
| Field | Type |
|---|---|
| `id` | Long (Primary Key) |
| `appointment` | Foreign Key (`Appointment`, Unique) |
| `amount` | BigDecimal |
| `status` | String |
| `billingDate` | LocalDateTime |

---

## 7. Entity Relationships

```text
Patient
   │
   ├──────< Appointment >────── Doctor
   │                │
   │                ├──── Prescription (1:1)
   │                │
   │                └──── Billing (1:1)
   │
   └──────< MedicalRecord (1:Many)
```

### Relationship Details
- One Patient can have multiple Appointments (1:Many).
- One Doctor can have multiple Appointments (1:Many).
- One Appointment has one Prescription (1:1).
- One Patient can have multiple Medical Records (1:Many).
- One Appointment has one Billing record (1:1).

---

## 8. API Endpoints

### Patient APIs
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/patients` | Create Patient |
| `GET` | `/api/patients` | Get All Patients |
| `GET` | `/api/patients/{id}` | Get Patient By ID |
| `PUT` | `/api/patients/{id}` | Update Patient |
| `DELETE` | `/api/patients/{id}` | Delete Patient |

### Doctor APIs
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/doctors` | Create Doctor |
| `GET` | `/api/doctors` | Get All Doctors |
| `GET` | `/api/doctors/{id}` | Get Doctor By ID |
| `PUT` | `/api/doctors/{id}` | Update Doctor |
| `DELETE` | `/api/doctors/{id}` | Delete Doctor |

### Appointment APIs
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/appointments` | Create Appointment |
| `GET` | `/api/appointments` | Get All Appointments |
| `GET` | `/api/appointments/{id}` | Get Appointment By ID |
| `PUT` | `/api/appointments/{id}` | Update Appointment |
| `DELETE` | `/api/appointments/{id}` | Delete Appointment |

### Prescription APIs
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/prescriptions` | Create Prescription |
| `GET` | `/api/prescriptions` | Get All Prescriptions |
| `GET` | `/api/prescriptions/{id}` | Get Prescription By ID |
| `PUT` | `/api/prescriptions/{id}` | Update Prescription |
| `DELETE` | `/api/prescriptions/{id}` | Delete Prescription |

### Medical Record APIs
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/records` | Create Medical Record |
| `GET` | `/api/records` | Get All Medical Records |
| `GET` | `/api/records/{id}` | Get Medical Record By ID |
| `PUT` | `/api/records/{id}` | Update Medical Record |
| `DELETE` | `/api/records/{id}` | Delete Medical Record |

### Billing APIs
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/billing` | Create Billing Record |
| `GET` | `/api/billing` | Get All Billing Records |
| `GET` | `/api/billing/{id}` | Get Billing Record By ID |
| `PUT` | `/api/billing/{id}` | Update Billing Record |
| `DELETE` | `/api/billing/{id}` | Delete Billing Record |

---

## 9. Validation Used
- `@NotBlank`
- `@NotNull`
- `@Email`
- `@FutureOrPresent`
- `@PositiveOrZero`
- `@Valid`

These validations ensure that only valid and sanitized data is stored in the database.

---

## 10. Exception Handling
The project uses global exception handling through `@ControllerAdvice` (`GlobalExceptionHandler`).

### Custom Exception
- `ResourceNotFoundException`

### Global Exception Handler Handles:
- **Resource Not Found (404)**
- **Validation Errors (400)**
- **Internal Server Errors (500)**

---

## 11. HTTP Status Codes

| Status Code | Description |
|---|---|
| `200` | OK |
| `201` | Created |
| `204` | No Content |
| `400` | Bad Request |
| `401` | Unauthorized |
| `404` | Not Found |
| `500` | Internal Server Error |

---

## 12. Features
- Patient Management
- Doctor Management
- Appointment Scheduling
- Digital Prescription Issuance
- Medical Record History Tracking
- Billing and Invoicing Management
- CRUD Operations
- RESTful API Design
- Entity Relationships using Spring Data JPA
- Declarative Validation
- Global Exception Handling
- Spring Security (Basic Auth)
- Live Swagger UI Documentation
- MySQL / H2 Database Integration

---

## 13. Future Enhancements
- JWT Authentication & Authorization
- Role-Based Access Control (Patient, Doctor, Admin)
- Real-time Appointment Notifications (SMS/Email)
- Telehealth Video Consultation Integration
- Payment Gateway Integration (Stripe / Razorpay)
- Cloud Storage for Medical Scans and Lab Reports
- Docker Containerization & CI/CD Pipeline

---

## 14. Conclusion
The Healthcare Management System REST API is a Spring Boot-based backend application that provides CRUD operations for managing patients, doctors, appointments, prescriptions, medical records, and billing. The project demonstrates RESTful API development, Spring Data JPA relationships, validation, exception handling, and database integration while following a layered architecture for maintainability and scalability.
