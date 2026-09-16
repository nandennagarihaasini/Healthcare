import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class ProfessionalCanvas(canvas.Canvas):
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
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Running header (for page 2 onwards)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#2B6CB0"))
            self.drawString(54, letter[1] - 36, "HEALTHCARE MANAGEMENT SYSTEM REST API")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#718096"))
            self.drawRightString(letter[0] - 54, letter[1] - 36, "Technical Project Report")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.75)
            self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)

        # Running footer (all pages)
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.75)
        self.line(54, 46, letter[0] - 54, 46)

        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#718096"))
        self.drawString(54, 32, "Confidential — Java & Spring Boot Enterprise Architecture")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 32, page_text)
        self.restoreState()

def build_pdf():
    pdf_path = r"D:\Healthcare project\Healthcare_Project_Report_Best.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=50,
        bottomMargin=52
    )

    styles = getSampleStyleSheet()

    # Colors
    c_primary = colors.HexColor("#1A365D")    # Deep Navy
    c_secondary = colors.HexColor("#2B6CB0")  # Rich Royal Blue
    c_accent = colors.HexColor("#319795")     # Teal Accent
    c_dark = colors.HexColor("#2D3748")       # Body Text Charcoal
    c_light_bg = colors.HexColor("#F7FAFC")   # Soft Off-white
    c_blue_tint = colors.HexColor("#EBF8FF")  # Soft Blue Tint
    c_border = colors.HexColor("#CBD5E0")     # Subtle Border

    # Typography
    main_title = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=c_primary,
        spaceAfter=6
    )

    sub_title = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=18,
        textColor=c_secondary,
        spaceAfter=14
    )

    sec_title = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=c_primary,
        spaceBefore=12,
        spaceAfter=6
    )

    subsec_title = ParagraphStyle(
        'SubSectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=c_secondary,
        spaceBefore=8,
        spaceAfter=4
    )

    body = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=13.8,
        textColor=c_dark,
        spaceAfter=5
    )

    bullet = ParagraphStyle(
        'BulletDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.2,
        textColor=c_dark,
        leftIndent=12,
        spaceAfter=3.5
    )

    code_box = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#1A202C")
    )

    th = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    tc = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=c_dark
    )

    tc_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=11,
        textColor=colors.HexColor("#1A202C")
    )

    story = []

    # ==================== COVER BANNER ====================
    story.append(Paragraph("Healthcare Management System REST API", main_title))
    story.append(Paragraph("Enterprise Software Engineering Project Report & Architecture Guide", sub_title))
    story.append(HRFlowable(width="100%", thickness=2.5, color=c_secondary, spaceAfter=10))

    meta_table_data = [
        [Paragraph("<b>Project Author:</b> Nandennagari Haasini", tc), Paragraph("<b>Target Environment:</b> Java 21 / Spring Boot 4.1.x", tc)],
        [Paragraph("<b>Repository:</b> github.com/nandennagarihaasini/Healthcare", tc), Paragraph("<b>Security:</b> Spring Security (HTTP Basic Auth)", tc)],
        [Paragraph("<b>Documentation:</b> Springdoc OpenAPI / Swagger UI 2.8.6", tc), Paragraph("<b>Database:</b> Relational (MySQL / Embedded H2)", tc)]
    ]
    t_meta = Table(meta_table_data, colWidths=[3.5 * inch, 3.5 * inch])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_blue_tint),
        ('BOX', (0, 0), (-1, -1), 1, c_secondary),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, c_border),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))

    # ==================== 1. PROJECT OVERVIEW ====================
    story.append(Paragraph("1. Project Overview", sec_title))
    story.append(Paragraph(
        "The <b>Healthcare Management System REST API</b> is an enterprise-grade backend service engineered to modernize "
        "and digitize operations in hospitals, clinics, and outpatient healthcare networks. It provides a robust, centralized, "
        "and decoupled platform for managing the entire patient care lifecycle across six critical business domains: "
        "<b>Patients, Doctors, Appointments, Prescriptions, Medical Records, and Billing</b>.",
        body
    ))
    story.append(Paragraph(
        "<b>Problem Statement:</b> Traditional healthcare administration relies on disparate systems—paper files, isolated billing "
        "spreadsheets, and disconnected scheduling registers. This creates critical operational bottlenecks: patient history "
        "fragmentation, consultation scheduling conflicts, unfulfilled prescriptions, and revenue leakages. "
        "<b>Solution:</b> This project establishes a unified, transaction-safe RESTful API adhering to industry-standard "
        "HTTP methods, strict relational integrity via Spring Data JPA, automated data validation, and real-time Swagger documentation.",
        body
    ))
    story.append(Spacer(1, 6))

    # ==================== 2. FUNCTIONAL MODULES ====================
    story.append(Paragraph("2. Functional Modules", sec_title))
    story.append(Paragraph(
        "The architecture is organized around six autonomous yet interconnected functional modules:", body
    ))

    modules_data = [
        [Paragraph("Module", th), Paragraph("Primary Responsibilities", th), Paragraph("Key Endpoints", th)],
        [
            Paragraph("<b>Patient Management</b>", tc_bold),
            Paragraph("Patient onboarding, demographics tracking, contact details, and admission timeline.", tc),
            Paragraph("<code>/api/patients<br/>GET, POST, PUT, DELETE</code>", tc)
        ],
        [
            Paragraph("<b>Doctor Management</b>", tc_bold),
            Paragraph("Directory of medical staff, departmental specialization, phone, and professional email.", tc),
            Paragraph("<code>/api/doctors<br/>GET, POST, PUT, DELETE</code>", tc)
        ],
        [
            Paragraph("<b>Appointment Scheduling</b>", tc_bold),
            Paragraph("Relational nexus linking patient and doctor; enforces future date and entity existence validation.", tc),
            Paragraph("<code>/api/appointments<br/>GET, POST, PUT, DELETE</code>", tc)
        ],
        [
            Paragraph("<b>Prescription Issuance</b>", tc_bold),
            Paragraph("1:1 clinical prescription generated per appointment; records medication name, dosage, and intake advice.", tc),
            Paragraph("<code>/api/prescriptions<br/>GET, POST, PUT, DELETE</code>", tc)
        ],
        [
            Paragraph("<b>Medical Records (EHR)</b>", tc_bold),
            Paragraph("Cumulative electronic health records, clinical diagnoses, and prescribed treatments linked to patients.", tc),
            Paragraph("<code>/api/records<br/>GET, POST, PUT, DELETE</code>", tc)
        ],
        [
            Paragraph("<b>Billing & Invoicing</b>", tc_bold),
            Paragraph("1:1 financial invoices per consultation tracking invoice amount, payment status, and timestamp.", tc),
            Paragraph("<code>/api/billing<br/>GET, POST, PUT, DELETE</code>", tc)
        ]
    ]
    t_mod = Table(modules_data, colWidths=[1.8 * inch, 3.4 * inch, 1.8 * inch])
    t_mod.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), c_secondary),
        ('GRID', (0, 0), (-1, -1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [c_light_bg, colors.white]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_mod)

    story.append(PageBreak())

    # ==================== 3. TECHNOLOGY STACK ====================
    story.append(Paragraph("3. Technology Stack", sec_title))
    tech_table_data = [
        [Paragraph("Category", th), Paragraph("Technology Selected", th), Paragraph("Architectural Rationale", th)],
        [Paragraph("Language", tc_bold), Paragraph("Java 21 (LTS)", tc), Paragraph("Strong typing, high concurrency, virtual threads, and enterprise ecosystem.", tc)],
        [Paragraph("Framework", tc_bold), Paragraph("Spring Boot 4.1.x / 3.x", tc), Paragraph("Auto-configuration, production-ready metrics, embedded Tomcat server.", tc)],
        [Paragraph("Persistence / ORM", tc_bold), Paragraph("Spring Data JPA / Hibernate", tc), Paragraph("Eliminates repetitive SQL; automated schema generation and dirty checking.", tc)],
        [Paragraph("Databases", tc_bold), Paragraph("MySQL 8.0 & H2 In-Memory", tc), Paragraph("MySQL for enterprise persistent storage; H2 for zero-dependency local execution.", tc)],
        [Paragraph("Build Automation", tc_bold), Paragraph("Apache Maven 3.9+", tc), Paragraph("Standardized dependency management and reproducible multi-platform builds.", tc)],
        [Paragraph("Code Optimization", tc_bold), Paragraph("Project Lombok", tc), Paragraph("Reduces boilerplate code via @Data, @Builder, and @RequiredArgsConstructor.", tc)],
        [Paragraph("Data Validation", tc_bold), Paragraph("Jakarta Bean Validation", tc), Paragraph("Declarative constraints (@NotBlank, @FutureOrPresent) preventing corrupt data.", tc)],
        [Paragraph("Security", tc_bold), Paragraph("Spring Security", tc), Paragraph("HTTP Basic Authentication, CSRF protection, and endpoint role access control.", tc)],
        [Paragraph("API Documentation", tc_bold), Paragraph("Springdoc OpenAPI 2.8.6", tc), Paragraph("Dynamic OpenAPI 3 schema and live, interactive browser-based Swagger UI.", tc)],
        [Paragraph("API Testing", tc_bold), Paragraph("Postman Tool", tc), Paragraph("Collection-based test automation, request payloads, and status code verification.", tc)]
    ]
    t_tech = Table(tech_table_data, colWidths=[1.5 * inch, 2.2 * inch, 3.3 * inch])
    t_tech.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), c_secondary),
        ('GRID', (0, 0), (-1, -1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [c_light_bg, colors.white]),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_tech)
    story.append(Spacer(1, 8))

    # ==================== 4. EXTERNAL DEPENDENCIES ====================
    story.append(Paragraph("4. External Dependencies", sec_title))
    story.append(Paragraph("Key Maven dependencies specified in <code>pom.xml</code>:", body))

    dep_bullets = [
        "● <b>spring-boot-starter-webmvc:</b> Core REST framework containing Spring MVC, Jackson JSON serializer, and embedded Apache Tomcat.",
        "● <b>spring-boot-starter-data-jpa:</b> Integrates Hibernate ORM, HikariCP connection pooling, and Spring Data repository proxies.",
        "● <b>spring-boot-starter-validation:</b> Hibernate Validator implementation of Jakarta Validation 3.0 specification.",
        "● <b>spring-boot-starter-security:</b> Secures REST endpoints using Basic Auth and provides SecurityFilterChain bean customization.",
        "● <b>springdoc-openapi-starter-webmvc-ui (v2.8.6):</b> Automatically generates <code>/v3/api-docs</code> and mounts interactive Swagger UI.",
        "● <b>mysql-connector-j & h2:</b> High-performance JDBC drivers for production MySQL and embedded in-memory H2 databases.",
        "● <b>lombok:</b> Compile-time annotation processor for getters, setters, constructors, and builder patterns."
    ]
    for d in dep_bullets:
        story.append(Paragraph(d, bullet))

    story.append(Spacer(1, 8))

    # ==================== 5. ARCHITECTURE ====================
    story.append(Paragraph("5. Architecture", sec_title))
    story.append(Paragraph("The system follows a strict <b>Layered Architecture Pattern</b> with separation of concerns:", body))

    arch_diagram = """
   ┌─────────────────────────────────────────────────────────────────────────────┐
   │                       CLIENT LAYER (Postman / Browser / Swagger UI)         │
   └───────────────────────────────────────┬─────────────────────────────────────┘
                                           │ HTTP Request (JSON Payload + Basic Auth)
                                           ▼
   ┌─────────────────────────────────────────────────────────────────────────────┐
   │ CONTROLLER LAYER: @RestController, @RequestMapping, @Valid                   │
   │ PatientController | DoctorController | AppointmentController | Billing etc. │
   └───────────────────────────────────────┬─────────────────────────────────────┘
                                           │ Validated Domain Entities / DTOs
                                           ▼
   ┌─────────────────────────────────────────────────────────────────────────────┐
   │ SERVICE LAYER: @Service, Business Validation, Transaction Boundaries         │
   │ PatientService | DoctorService | AppointmentService | PrescriptionService   │
   └───────────────────────────────────────┬─────────────────────────────────────┘
                                           │ Spring Data JPA Method Invocations
                                           ▼
   ┌─────────────────────────────────────────────────────────────────────────────┐
   │ REPOSITORY LAYER: JpaRepository<T, ID>, Derived Queries, ORM Mapping        │
   │ PatientRepository | DoctorRepository | AppointmentRepository etc.           │
   └───────────────────────────────────────┬─────────────────────────────────────┘
                                           │ SQL Execution via HikariCP Pool
                                           ▼
   ┌─────────────────────────────────────────────────────────────────────────────┐
   │ DATABASE LAYER: Relational Tables (patients, doctors, appointments, etc.)   │
   └─────────────────────────────────────────────────────────────────────────────┘
    """
    story.append(Paragraph(f"<pre>{arch_diagram}</pre>", code_box))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<b>Entity Relationships:</b> Patient (1:M) Appointment | Doctor (1:M) Appointment | Appointment (1:1) Prescription | "
        "Patient (1:M) MedicalRecord | Appointment (1:1) Billing. Centralized error interception is governed by <code>GlobalExceptionHandler</code>.",
        body
    ))

    story.append(PageBreak())

    # ==================== 6. FOLDER STRUCTURE ====================
    story.append(Paragraph("6. Folder Structure", sec_title))
    story.append(Paragraph("Clean package hierarchy organized by architectural layer:", body))

    fs_diagram = """
D:\\Healthcare project
│
├── .git/                                    # Git repository metadata
├── Healthcare_Management_System_Documentation.pdf # Generated technical reference PDF
├── PROJECT_DOCUMENTATION.md                 # Technical project documentation
├── UPLOAD_TO_GITHUB.bat                     # 1-Click interactive GitHub sync tool
│
├── postman/                                 # Postman workspace & collections
│   └── collections/Healthcare REST API/     # YAML requests for all 6 modules
│
└── healthcare/                              # Spring Boot Application Root
    ├── pom.xml                              # Maven build descriptor & dependencies
    ├── mvnw / mvnw.cmd                      # Cross-platform Maven wrappers
    ├── README.md & INTERVIEW_GUIDE.md       # Project overview & interview Q&A
    │
    └── src/main/java/com/example/healthcare/
        ├── HealthcareApplication.java       # Spring Boot main entry point
        ├── config/
        │   ├── SecurityConfig.java          # Basic Auth & Swagger permitAll rules
        │   └── DataInitializer.java         # Automated database seeder (Dr. Haasini ID: 3)
        ├── controller/                      # 6 REST API Controllers (@RestController)
        ├── service/                         # 6 Business Service classes (@Service)
        ├── repository/                      # 6 JPA Repositories (JpaRepository)
        ├── entity/                          # 6 Relational Entities (@Entity)
        └── exception/                       # GlobalExceptionHandler & ResourceNotFoundException
    """
    story.append(Paragraph(f"<pre>{fs_diagram}</pre>", code_box))
    story.append(Spacer(1, 6))

    # ==================== 7. DEVELOPMENT METHODOLOGY ====================
    story.append(Paragraph("7. Development Methodology", sec_title))
    story.append(Paragraph(
        "The project was engineered using an <b>Agile, Feature-Driven Iterative Lifecycle</b>. Rather than attempting "
        "monolithic construction, features were developed in vertical testable slices:",
        body
    ))
    methodology_bullets = [
        "● <b>Phase 1 — Inception & Scaffolding:</b> Spring Initializr setup, Maven dependencies, MySQL/H2 configuration.",
        "● <b>Phase 2 — Core Master Entities:</b> Constructed Patient and Doctor modules with Repository-Service-Controller chains.",
        "● <b>Phase 3 — Relational Nexus:</b> Implemented Appointment module connecting Patients and Doctors with foreign keys.",
        "● <b>Phase 4 — Clinical & Billing Operations:</b> Constructed 1:1 Prescription, 1:M Medical Records, and 1:1 Billing modules.",
        "● <b>Phase 5 — Defensive Programming:</b> Implemented Jakarta Validation and global exception handling with clean JSON payloads.",
        "● <b>Phase 6 — Security & Documentation:</b> Configured Spring Security Basic Auth, Swagger UI, and automated data seeding.",
        "● <b>Phase 7 — Verification & Release:</b> Executed comprehensive Postman testing, PDF generation, and GitHub version control sync."
    ]
    for m in methodology_bullets:
        story.append(Paragraph(m, bullet))

    story.append(Spacer(1, 6))

    # ==================== 8. TESTING & QUALITY ASSURANCE ====================
    story.append(Paragraph("8. Testing & Quality Assurance", sec_title))
    story.append(Paragraph(
        "Quality assurance was conducted across positive, negative, and edge-case execution matrices using Postman and Swagger UI:",
        body
    ))

    qa_data = [
        [Paragraph("Test Category", th), Paragraph("Endpoint / Scenario Tested", th), Paragraph("Input Condition", th), Paragraph("Expected Result", th)],
        [Paragraph("Positive CRUD", tc_bold), Paragraph("POST /api/patients", tc), Paragraph("Valid patient JSON", tc), Paragraph("201 Created + ID", tc)],
        [Paragraph("Entity Lookup", tc_bold), Paragraph("GET /api/doctors/3", tc), Paragraph("Query ID = 3 (Dr. Haasini)", tc), Paragraph("200 OK + Details", tc)],
        [Paragraph("Validation Edge", tc_bold), Paragraph("POST /api/appointments", tc), Paragraph("Past appointmentDate", tc), Paragraph("400 Bad Request", tc)],
        [Paragraph("Constraint Check", tc_bold), Paragraph("POST /api/patients", tc), Paragraph("Missing contact field", tc), Paragraph("400 + Field Error", tc)],
        [Paragraph("Not Found Exception", tc_bold), Paragraph("GET /api/doctors/999", tc), Paragraph("Non-existent ID", tc), Paragraph("404 Not Found", tc)],
        [Paragraph("Security Gate", tc_bold), Paragraph("GET /api/billing", tc), Paragraph("No credentials", tc), Paragraph("401 Unauthorized", tc)],
        [Paragraph("Unique 1:1 Rule", tc_bold), Paragraph("POST /api/billing", tc), Paragraph("Duplicate appointment ID", tc), Paragraph("Database Rejection", tc)]
    ]
    t_qa = Table(qa_data, colWidths=[1.4 * inch, 1.8 * inch, 2.0 * inch, 1.8 * inch])
    t_qa.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), c_secondary),
        ('GRID', (0, 0), (-1, -1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [c_light_bg, colors.white]),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t_qa)

    story.append(PageBreak())

    # ==================== 9. BUILDING & RUNNING ====================
    story.append(Paragraph("9. Building & Running", sec_title))
    story.append(Paragraph("Follow these instructions to compile, run, and test the project locally:", body))

    run_text = """
1. CLONE THE REPOSITORY:
   git clone https://github.com/nandennagarihaasini/Healthcare.git
   cd Healthcare/healthcare

2. RUN THE APPLICATION (Using embedded Maven Wrapper):
   Windows:  .\\mvnw.cmd clean spring-boot:run
   Linux/Mac: ./mvnw clean spring-boot:run

3. ACCESS ENDPOINTS & DOCUMENTATION:
   - Base REST API URL:            http://localhost:8080/api/
   - Interactive Swagger UI:       http://localhost:8080/swagger-ui.html
   - OpenAPI v3 JSON Schema:       http://localhost:8080/v3/api-docs
   - H2 In-Memory Database Web:    http://localhost:8080/h2-console

4. AUTHENTICATION CREDENTIALS (Spring Security Basic Auth):
   - Username: admin
   - Password: admin123
    """
    story.append(Paragraph(f"<pre>{run_text}</pre>", code_box))
    story.append(Spacer(1, 8))

    # ==================== 10. CONCLUSION ====================
    story.append(Paragraph("10. Conclusion", sec_title))
    story.append(Paragraph(
        "The <b>Healthcare Management System REST API</b> represents a complete, production-ready backend solution for "
        "medical center administration. Developed using <b>Java 21, Spring Boot, Spring Data JPA, and Spring Security</b>, "
        "the project demonstrates best practices in enterprise software engineering: decoupled layered design, strict referential "
        "integrity, declarative bean validation, centralized error handling, and automated interactive API documentation.",
        body
    ))
    story.append(Paragraph(
        "<b>Key Takeaways:</b> The modular architecture ensures seamless scalability and maintainability. Future expansions—such as "
        "JWT token authentication, Role-Based Access Control (RBAC), cloud attachment storage for lab reports, and automated "
        "payment gateways—can be integrated with zero breaking changes to existing client integrations.",
        body
    ))
    story.append(Spacer(1, 10))

    # Sign-off box
    sign_off_data = [
        [
            Paragraph("<b>Repository:</b> https://github.com/nandennagarihaasini/Healthcare", tc),
            Paragraph("<b>Status:</b> Production Ready / Tested ✅", tc)
        ]
    ]
    t_sign = Table(sign_off_data, colWidths=[4.8 * inch, 2.2 * inch])
    t_sign.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_blue_tint),
        ('BOX', (0, 0), (-1, -1), 1, c_secondary),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_sign)

    doc.build(story, canvasmaker=ProfessionalCanvas)
    print("Best PDF built successfully at:", pdf_path)

if __name__ == "__main__":
    build_pdf()
