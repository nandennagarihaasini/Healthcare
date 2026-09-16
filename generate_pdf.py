import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#666666"))
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 36, page_text)
        self.drawString(54, 36, "Healthcare Management System REST API — Project Documentation")
        self.restoreState()

def build_pdf():
    pdf_path = r"D:\Healthcare project\Healthcare_Management_System_Documentation.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=colors.HexColor("#1A202C"),
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=20,
        textColor=colors.HexColor("#2B6CB0"),
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=20,
        textColor=colors.HexColor("#1A365D"),
        spaceBefore=14,
        spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2C5282"),
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#2D3748"),
        leftIndent=15,
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1A202C")
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#2D3748")
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#1A202C")
    )

    story = []

    # ------------------ COVER / HEADER ------------------
    story.append(Paragraph("Healthcare Management System REST API", title_style))
    story.append(Paragraph("Project Documentation", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#2B6CB0"), spaceAfter=15))

    story.append(Paragraph("<b>Project Name:</b> Healthcare Management System REST API", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Technology Stack:</b>", body_style))
    tech_bullets = [
        "● Java 21",
        "● Spring Boot 4.1.1 / 3.x",
        "● Spring Data JPA (Hibernate)",
        "● MySQL / H2 Relational Database",
        "● Maven (Dependency Management)",
        "● Lombok",
        "● Jakarta Validation",
        "● Spring Security (Basic Auth)",
        "● Springdoc OpenAPI (Swagger UI)",
        "● Postman (API Testing & Verification)"
    ]
    for b in tech_bullets:
        story.append(Paragraph(b, bullet_style))

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E2E8F0"), spaceAfter=10))

    # ------------------ 1. PROJECT OVERVIEW ------------------
    story.append(Paragraph("1. Project Overview", h1_style))
    story.append(Paragraph(
        "The <b>Healthcare Management System REST API</b> is an enterprise-grade backend service built using "
        "<b>Spring Boot</b>. It enables complete digital administration of modern healthcare operations across six "
        "vital modules: <b>Patients, Doctors, Appointments, Prescriptions, Medical Records, and Billing</b>.",
        body_style
    ))
    story.append(Paragraph(
        "The system adheres strictly to a clean, decoupled <b>Layered Architecture</b> comprising Controller, "
        "Service, Repository, and Entity layers. This ensures high testability, separation of business concerns, "
        "robust input validation, centralized exception handling, and enterprise database integration.",
        body_style
    ))

    story.append(Spacer(1, 10))

    # ------------------ 2. OBJECTIVES ------------------
    story.append(Paragraph("2. Objectives", h1_style))
    objectives = [
        "● <b>Patient Administration:</b> Maintain demographic records, contact info, and registration history.",
        "● <b>Doctor Management:</b> Store physician profiles, specialties, and professional contact details.",
        "● <b>Appointment Scheduling:</b> Connect patients and doctors for scheduled medical consultations.",
        "● <b>Prescription Issuance:</b> Digitally track medications, dosages, and administration instructions.",
        "● <b>Medical Record Tracking:</b> Maintain comprehensive diagnostic histories and treatment plans.",
        "● <b>Billing & Finance:</b> Record invoices, billing amounts, and payment statuses per consultation.",
        "● <b>Enterprise REST APIs:</b> Expose full CRUD endpoints adhering to standard HTTP status codes.",
        "● <b>Relational Data Integrity:</b> Model 1:Many and 1:1 foreign key relationships using Spring Data JPA."
    ]
    for obj in objectives:
        story.append(Paragraph(obj, bullet_style))

    story.append(PageBreak())

    # ------------------ 3. TECHNOLOGIES USED ------------------
    story.append(Paragraph("3. Technologies Used", h1_style))
    tech_data = [
        [Paragraph("Technology", table_header_style), Paragraph("Purpose", table_header_style)],
        [Paragraph("Java 21", table_cell_bold), Paragraph("Primary object-oriented programming language", table_cell_style)],
        [Paragraph("Spring Boot", table_cell_bold), Paragraph("Rapid enterprise backend application framework", table_cell_style)],
        [Paragraph("Spring Data JPA", table_cell_bold), Paragraph("Data persistence, Hibernate ORM, repository abstraction", table_cell_style)],
        [Paragraph("MySQL / H2", table_cell_bold), Paragraph("Relational database engines for storage and testing", table_cell_style)],
        [Paragraph("Maven", table_cell_bold), Paragraph("Build automation and dependency management tool", table_cell_style)],
        [Paragraph("Lombok", table_cell_bold), Paragraph("Eliminates boilerplate code (@Data, @Builder, etc.)", table_cell_style)],
        [Paragraph("Jakarta Validation", table_cell_bold), Paragraph("Declarative request body validation (@NotBlank, @Email)", table_cell_style)],
        [Paragraph("Spring Security", table_cell_bold), Paragraph("API authentication and endpoint authorization", table_cell_style)],
        [Paragraph("Springdoc OpenAPI", table_cell_bold), Paragraph("Interactive live Swagger UI documentation", table_cell_style)],
        [Paragraph("Postman", table_cell_bold), Paragraph("Automated REST API testing and validation suite", table_cell_style)]
    ]
    t_tech = Table(tech_data, colWidths=[2.2 * inch, 4.8 * inch])
    t_tech.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0"))
    ]))
    story.append(t_tech)

    story.append(Spacer(1, 14))

    # ------------------ 4. PROJECT ARCHITECTURE ------------------
    story.append(Paragraph("4. Project Architecture", h1_style))
    story.append(Paragraph("The system implements a production-grade 4-layer architectural design pattern:", body_style))

    arch_text = """
                       ┌────────────────────────────────────────┐
                       │  Client Layer (Postman / Browser UI)   │
                       └───────────────────┬────────────────────┘
                                           │ HTTP Request / JSON
                                           ▼
                       ┌────────────────────────────────────────┐
                       │            Controller Layer            │
                       │  (Patient, Doctor, Appointment, etc.)  │
                       └───────────────────┬────────────────────┘
                                           │ Validated Entity/DTO
                                           ▼
                       ┌────────────────────────────────────────┐
                       │             Service Layer              │
                       │   (Business Logic & Validation Rules)  │
                       └───────────────────┬────────────────────┘
                                           │ Domain Operations
                                           ▼
                       ┌────────────────────────────────────────┐
                       │            Repository Layer            │
                       │        (Spring Data JPA / ORM)         │
                       └───────────────────┬────────────────────┘
                                           │ SQL Queries / DDL
                                           ▼
                       ┌────────────────────────────────────────┐
                       │     Database Layer (MySQL / H2 DB)     │
                       └────────────────────────────────────────┘
    """
    story.append(Paragraph(f"<pre>{arch_text}</pre>", code_style))

    story.append(PageBreak())

    # ------------------ 5. PROJECT STRUCTURE ------------------
    story.append(Paragraph("5. Project Structure", h1_style))
    struct_text = """
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
    """
    story.append(Paragraph(f"<pre>{struct_text}</pre>", code_style))

    story.append(Spacer(1, 10))

    # ------------------ 6. DATABASE DESIGN ------------------
    story.append(Paragraph("6. Database Design", h1_style))
    story.append(Paragraph("The database contains six interconnected entities designed with normalized schemas:", body_style))

    db_tables = [
        ("Patient Entity", [
            [Paragraph("Field", table_header_style), Paragraph("Type", table_header_style), Paragraph("Constraint / Details", table_header_style)],
            [Paragraph("id", table_cell_bold), Paragraph("Long", table_cell_style), Paragraph("Primary Key, Auto-increment", table_cell_style)],
            [Paragraph("name", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank", table_cell_style)],
            [Paragraph("dob", table_cell_bold), Paragraph("LocalDate", table_cell_style), Paragraph("Date of birth", table_cell_style)],
            [Paragraph("gender", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("Male / Female / Other", table_cell_style)],
            [Paragraph("contact", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank, Phone number", table_cell_style)],
            [Paragraph("address", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("Residential address", table_cell_style)],
            [Paragraph("createdAt", table_cell_bold), Paragraph("LocalDateTime", table_cell_style), Paragraph("@CreationTimestamp", table_cell_style)],
        ]),
        ("Doctor Entity", [
            [Paragraph("Field", table_header_style), Paragraph("Type", table_header_style), Paragraph("Constraint / Details", table_header_style)],
            [Paragraph("id", table_cell_bold), Paragraph("Long", table_cell_style), Paragraph("Primary Key, Auto-increment", table_cell_style)],
            [Paragraph("name", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank", table_cell_style)],
            [Paragraph("specialization", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank (e.g. Cardiology)", table_cell_style)],
            [Paragraph("phone", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank", table_cell_style)],
            [Paragraph("email", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank, @Email", table_cell_style)],
        ]),
        ("Appointment Entity", [
            [Paragraph("Field", table_header_style), Paragraph("Type", table_header_style), Paragraph("Constraint / Details", table_header_style)],
            [Paragraph("id", table_cell_bold), Paragraph("Long", table_cell_style), Paragraph("Primary Key, Auto-increment", table_cell_style)],
            [Paragraph("patient", table_cell_bold), Paragraph("Patient", table_cell_style), Paragraph("Foreign Key (@ManyToOne)", table_cell_style)],
            [Paragraph("doctor", table_cell_bold), Paragraph("Doctor", table_cell_style), Paragraph("Foreign Key (@ManyToOne)", table_cell_style)],
            [Paragraph("appointmentDate", table_cell_bold), Paragraph("LocalDateTime", table_cell_style), Paragraph("@FutureOrPresent", table_cell_style)],
            [Paragraph("reason", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank", table_cell_style)],
            [Paragraph("status", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("SCHEDULED / COMPLETED", table_cell_style)],
        ]),
        ("Prescription Entity", [
            [Paragraph("Field", table_header_style), Paragraph("Type", table_header_style), Paragraph("Constraint / Details", table_header_style)],
            [Paragraph("id", table_cell_bold), Paragraph("Long", table_cell_style), Paragraph("Primary Key, Auto-increment", table_cell_style)],
            [Paragraph("appointment", table_cell_bold), Paragraph("Appointment", table_cell_style), Paragraph("Foreign Key (@OneToOne, Unique)", table_cell_style)],
            [Paragraph("medication", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank, Drug name", table_cell_style)],
            [Paragraph("dosage", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank (e.g. 10mg)", table_cell_style)],
            [Paragraph("instructions", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("Dosage schedule / advice", table_cell_style)],
        ]),
        ("Medical Record Entity", [
            [Paragraph("Field", table_header_style), Paragraph("Type", table_header_style), Paragraph("Constraint / Details", table_header_style)],
            [Paragraph("id", table_cell_bold), Paragraph("Long", table_cell_style), Paragraph("Primary Key, Auto-increment", table_cell_style)],
            [Paragraph("patient", table_cell_bold), Paragraph("Patient", table_cell_style), Paragraph("Foreign Key (@ManyToOne)", table_cell_style)],
            [Paragraph("diagnosis", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank, Clinical condition", table_cell_style)],
            [Paragraph("treatment", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("@NotBlank, Medical action taken", table_cell_style)],
            [Paragraph("recordDate", table_cell_bold), Paragraph("LocalDateTime", table_cell_style), Paragraph("@CreationTimestamp", table_cell_style)],
        ]),
        ("Billing Entity", [
            [Paragraph("Field", table_header_style), Paragraph("Type", table_header_style), Paragraph("Constraint / Details", table_header_style)],
            [Paragraph("id", table_cell_bold), Paragraph("Long", table_cell_style), Paragraph("Primary Key, Auto-increment", table_cell_style)],
            [Paragraph("appointment", table_cell_bold), Paragraph("Appointment", table_cell_style), Paragraph("Foreign Key (@OneToOne, Unique)", table_cell_style)],
            [Paragraph("amount", table_cell_bold), Paragraph("BigDecimal", table_cell_style), Paragraph("@NotNull, @PositiveOrZero", table_cell_style)],
            [Paragraph("status", table_cell_bold), Paragraph("String", table_cell_style), Paragraph("PAID / UNPAID / PENDING", table_cell_style)],
            [Paragraph("billingDate", table_cell_bold), Paragraph("LocalDateTime", table_cell_style), Paragraph("@CreationTimestamp", table_cell_style)],
        ])
    ]

    for title, rows in db_tables:
        story.append(Paragraph(title, h2_style))
        t = Table(rows, colWidths=[1.8 * inch, 1.8 * inch, 3.4 * inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.white]),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0"))
        ]))
        story.append(t)
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ------------------ 7. ENTITY RELATIONSHIPS ------------------
    story.append(Paragraph("7. Entity Relationships", h1_style))
    rel_diag = """
                                Patient
                                   │
                ┌──────────────────┼──────────────────┐
                │ 1                │ 1                │ 1
                ▼ M                ▼ M                │
           Appointment       MedicalRecord            │
                │                                     │
                ├─────────────────────────────────────┤
                │ 1                                 1 │
                ▼ 1                                 ▼ M
           Prescription                           Doctor
                │
                ▼ 1:1
             Billing
    """
    story.append(Paragraph(f"<pre>{rel_diag}</pre>", code_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Relationship Details:</b>", h2_style))
    rel_bullets = [
        "● <b>Patient 1 → Many Appointments:</b> A patient can book multiple hospital visits over time.",
        "● <b>Doctor 1 → Many Appointments:</b> A doctor conducts consultations with many patients.",
        "● <b>Appointment 1 → 1 Prescription:</b> Each clinical consultation generates one specific prescription.",
        "● <b>Patient 1 → Many Medical Records:</b> A patient accumulates multiple medical diagnosis entries.",
        "● <b>Appointment 1 → 1 Billing:</b> Each consultation has exactly one associated billing invoice."
    ]
    for rb in rel_bullets:
        story.append(Paragraph(rb, bullet_style))

    story.append(Spacer(1, 12))

    # ------------------ 8. API ENDPOINTS ------------------
    story.append(Paragraph("8. API Endpoints", h1_style))

    api_groups = [
        ("Patient APIs", [
            [Paragraph("Method", table_header_style), Paragraph("Endpoint", table_header_style), Paragraph("Description", table_header_style)],
            [Paragraph("POST", table_cell_bold), Paragraph("/api/patients", table_cell_style), Paragraph("Register new patient record", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/patients", table_cell_style), Paragraph("Retrieve all registered patients", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/patients/{id}", table_cell_style), Paragraph("Retrieve single patient by ID", table_cell_style)],
            [Paragraph("PUT", table_cell_bold), Paragraph("/api/patients/{id}", table_cell_style), Paragraph("Update patient details", table_cell_style)],
            [Paragraph("DELETE", table_cell_bold), Paragraph("/api/patients/{id}", table_cell_style), Paragraph("Remove patient from system", table_cell_style)],
        ]),
        ("Doctor APIs", [
            [Paragraph("Method", table_header_style), Paragraph("Endpoint", table_header_style), Paragraph("Description", table_header_style)],
            [Paragraph("POST", table_cell_bold), Paragraph("/api/doctors", table_cell_style), Paragraph("Register new doctor profile", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/doctors", table_cell_style), Paragraph("List all active doctors", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/doctors/{id}", table_cell_style), Paragraph("Get doctor profile by ID", table_cell_style)],
            [Paragraph("PUT", table_cell_bold), Paragraph("/api/doctors/{id}", table_cell_style), Paragraph("Update doctor information", table_cell_style)],
            [Paragraph("DELETE", table_cell_bold), Paragraph("/api/doctors/{id}", table_cell_style), Paragraph("De-register doctor profile", table_cell_style)],
        ]),
        ("Appointment APIs", [
            [Paragraph("Method", table_header_style), Paragraph("Endpoint", table_header_style), Paragraph("Description", table_header_style)],
            [Paragraph("POST", table_cell_bold), Paragraph("/api/appointments", table_cell_style), Paragraph("Schedule a consultation", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/appointments", table_cell_style), Paragraph("List all scheduled appointments", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/appointments/{id}", table_cell_style), Paragraph("Get appointment details by ID", table_cell_style)],
            [Paragraph("PUT", table_cell_bold), Paragraph("/api/appointments/{id}", table_cell_style), Paragraph("Reschedule / modify appointment", table_cell_style)],
            [Paragraph("DELETE", table_cell_bold), Paragraph("/api/appointments/{id}", table_cell_style), Paragraph("Cancel scheduled appointment", table_cell_style)],
        ]),
        ("Prescription APIs", [
            [Paragraph("Method", table_header_style), Paragraph("Endpoint", table_header_style), Paragraph("Description", table_header_style)],
            [Paragraph("POST", table_cell_bold), Paragraph("/api/prescriptions", table_cell_style), Paragraph("Issue new prescription", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/prescriptions", table_cell_style), Paragraph("List all prescriptions", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/prescriptions/{id}", table_cell_style), Paragraph("Get prescription by ID", table_cell_style)],
            [Paragraph("PUT", table_cell_bold), Paragraph("/api/prescriptions/{id}", table_cell_style), Paragraph("Update medication or dosage", table_cell_style)],
            [Paragraph("DELETE", table_cell_bold), Paragraph("/api/prescriptions/{id}", table_cell_style), Paragraph("Delete prescription entry", table_cell_style)],
        ]),
        ("Medical Record APIs", [
            [Paragraph("Method", table_header_style), Paragraph("Endpoint", table_header_style), Paragraph("Description", table_header_style)],
            [Paragraph("POST", table_cell_bold), Paragraph("/api/records", table_cell_style), Paragraph("Record clinical diagnosis", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/records", table_cell_style), Paragraph("List all clinical records", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/records/{id}", table_cell_style), Paragraph("Retrieve record by ID", table_cell_style)],
            [Paragraph("PUT", table_cell_bold), Paragraph("/api/records/{id}", table_cell_style), Paragraph("Update diagnosis/treatment", table_cell_style)],
            [Paragraph("DELETE", table_cell_bold), Paragraph("/api/records/{id}", table_cell_style), Paragraph("Remove medical record", table_cell_style)],
        ]),
        ("Billing APIs", [
            [Paragraph("Method", table_header_style), Paragraph("Endpoint", table_header_style), Paragraph("Description", table_header_style)],
            [Paragraph("POST", table_cell_bold), Paragraph("/api/billing", table_cell_style), Paragraph("Generate invoice for appointment", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/billing", table_cell_style), Paragraph("List all billing entries", table_cell_style)],
            [Paragraph("GET", table_cell_bold), Paragraph("/api/billing/{id}", table_cell_style), Paragraph("Get billing details by ID", table_cell_style)],
            [Paragraph("PUT", table_cell_bold), Paragraph("/api/billing/{id}", table_cell_style), Paragraph("Update amount or payment status", table_cell_style)],
            [Paragraph("DELETE", table_cell_bold), Paragraph("/api/billing/{id}", table_cell_style), Paragraph("Remove billing record", table_cell_style)],
        ])
    ]

    for title, rows in api_groups:
        story.append(Paragraph(title, h2_style))
        t = Table(rows, colWidths=[1.4 * inch, 2.6 * inch, 3.0 * inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
            ('TOPPADDING', (0, 0), (-1, -1), 3.5),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.white]),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0"))
        ]))
        story.append(t)
        story.append(Spacer(1, 5))

    story.append(PageBreak())

    # ------------------ 9. VALIDATION USED ------------------
    story.append(Paragraph("9. Validation Used", h1_style))
    story.append(Paragraph(
        "To ensure robust data sanitization and prevent corrupt records from entering the database, "
        "the application uses standard <b>Jakarta Bean Validation</b> annotations:",
        body_style
    ))
    validations = [
        "● <code>@NotBlank</code>: Enforces that strings (names, contacts, specializations, reasons) cannot be null or empty.",
        "● <code>@NotNull</code>: Ensures foreign key relationship entities and critical numeric fields are present.",
        "● <code>@Email</code>: Validates that doctor email addresses follow valid RFC-compliant syntax.",
        "● <code>@FutureOrPresent</code>: Ensures scheduled appointment dates cannot be placed in the past.",
        "● <code>@PositiveOrZero</code>: Guarantees that billing amounts cannot be negative values.",
        "● <code>@Valid</code>: Triggers automatic validation cascades across controller request payloads."
    ]
    for val in validations:
        story.append(Paragraph(val, bullet_style))

    story.append(Spacer(1, 10))

    # ------------------ 10. EXCEPTION HANDLING ------------------
    story.append(Paragraph("10. Exception Handling", h1_style))
    story.append(Paragraph(
        "The project handles exceptions centrally across the application using a dedicated "
        "<b><code>@ControllerAdvice</code></b> class (<code>GlobalExceptionHandler</code>), ensuring standardized JSON error responses.",
        body_style
    ))

    story.append(Paragraph("<b>Custom Exception:</b>", h2_style))
    story.append(Paragraph("● <code>ResourceNotFoundException</code>: Thrown when an invalid ID is requested.", bullet_style))

    story.append(Paragraph("<b>Global Exception Handler Handles:</b>", h2_style))
    story.append(Paragraph("● <b>Resource Not Found (404):</b> Returned when queries for non-existent entities fail.", bullet_style))
    story.append(Paragraph("● <b>Validation Errors (400):</b> Catches <code>MethodArgumentNotValidException</code> and returns detailed field-by-field error maps.", bullet_style))
    story.append(Paragraph("● <b>Internal Server Errors (500):</b> Catches unhandled runtime exceptions with user-friendly error messages.", bullet_style))

    story.append(Spacer(1, 10))

    # ------------------ 11. HTTP STATUS CODES ------------------
    story.append(Paragraph("11. HTTP Status Codes", h1_style))
    status_data = [
        [Paragraph("Status Code", table_header_style), Paragraph("Meaning", table_header_style), Paragraph("Scenario in Project", table_header_style)],
        [Paragraph("200 OK", table_cell_bold), Paragraph("Success", table_cell_style), Paragraph("Successful GET, PUT, and general operations", table_cell_style)],
        [Paragraph("201 Created", table_cell_bold), Paragraph("Created", table_cell_style), Paragraph("Returned when a new entity is saved via POST", table_cell_style)],
        [Paragraph("204 No Content", table_cell_bold), Paragraph("Deleted", table_cell_style), Paragraph("Successful DELETE operation", table_cell_style)],
        [Paragraph("400 Bad Request", table_cell_bold), Paragraph("Validation Failure", table_cell_style), Paragraph("Missing required fields or invalid format", table_cell_style)],
        [Paragraph("401 Unauthorized", table_cell_bold), Paragraph("Auth Required", table_cell_style), Paragraph("Missing or invalid Basic Auth credentials", table_cell_style)],
        [Paragraph("404 Not Found", table_cell_bold), Paragraph("Resource Missing", table_cell_style), Paragraph("Entity with requested ID does not exist", table_cell_style)],
        [Paragraph("500 Internal Error", table_cell_bold), Paragraph("Server Fault", table_cell_style), Paragraph("Unhandled system or database exceptions", table_cell_style)]
    ]
    t_status = Table(status_data, colWidths=[1.5 * inch, 1.8 * inch, 3.7 * inch])
    t_status.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0"))
    ]))
    story.append(t_status)

    story.append(PageBreak())

    # ------------------ 12. FEATURES ------------------
    story.append(Paragraph("12. Features", h1_style))
    features = [
        "● <b>Patient Management:</b> Complete CRUD lifecycle tracking for hospital patients.",
        "● <b>Doctor Management:</b> Physician directory with specialty and contact categorization.",
        "● <b>Appointment Scheduling:</b> Relational scheduling connecting patients with available doctors.",
        "● <b>Prescription Generation:</b> Medication dosage and patient administration instructions.",
        "● <b>Medical Record History:</b> Comprehensive diagnostic and clinical treatment logs.",
        "● <b>Billing & Invoicing:</b> Payment status and financial records linked directly to appointments.",
        "● <b>Relational Modeling:</b> Configured with JPA <code>@ManyToOne</code> and <code>@OneToOne</code> mappings.",
        "● <b>Live Swagger Documentation:</b> Interactive API documentation playground at <code>/swagger-ui.html</code>.",
        "● <b>Spring Security:</b> Protected endpoints using Basic Authentication.",
        "● <b>Automated Database DDL:</b> Automatic table schema generation and updates via Hibernate."
    ]
    for feat in features:
        story.append(Paragraph(feat, bullet_style))

    story.append(Spacer(1, 10))

    # ------------------ 13. FUTURE ENHANCEMENTS ------------------
    story.append(Paragraph("13. Future Enhancements", h1_style))
    enhancements = [
        "● <b>JWT Token Authentication:</b> Stateless token-based security replacing HTTP Basic Auth.",
        "● <b>Role-Based Access Control (RBAC):</b> Discrete roles for Patients, Doctors, and Administrators.",
        "● <b>Telehealth Integration:</b> WebRTC video call links embedded within appointment records.",
        "● <b>Automated SMS & Email Reminders:</b> Notifications for upcoming scheduled appointments.",
        "● <b>Payment Gateway Integration:</b> Stripe or Razorpay integration for real-time invoice payments.",
        "● <b>Cloud Storage (AWS S3):</b> Secure cloud hosting for lab reports and MRI/X-ray attachments.",
        "● <b>Docker & CI/CD:</b> Containerized microservices deployment with automated GitHub Actions."
    ]
    for enh in enhancements:
        story.append(Paragraph(enh, bullet_style))

    story.append(Spacer(1, 10))

    # ------------------ 14. CONCLUSION ------------------
    story.append(Paragraph("14. Conclusion", h1_style))
    story.append(Paragraph(
        "The <b>Healthcare Management System REST API</b> represents an enterprise-ready, robust backend solution "
        "designed for medical facilities and clinical administration. By applying modern Spring Boot principles, "
        "clean layered architecture, declarative validation, relational JPA mapping, and centralized exception handling, "
        "the project achieves high code maintainability, security, and scalability suitable for production deployment "
        "and technical interview demonstrations.",
        body_style
    ))

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF generated successfully at:", pdf_path)

if __name__ == "__main__":
    build_pdf()
