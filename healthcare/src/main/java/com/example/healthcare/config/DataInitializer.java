package com.example.healthcare.config;

import com.example.healthcare.entity.Doctor;
import com.example.healthcare.entity.Patient;
import com.example.healthcare.repository.DoctorRepository;
import com.example.healthcare.repository.PatientRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;

@Configuration
public class DataInitializer {

    @Bean
    CommandLineRunner initDatabase(DoctorRepository doctorRepository, PatientRepository patientRepository) {
        return args -> {
            if (doctorRepository.count() == 0) {
                // Doctor 1
                doctorRepository.save(Doctor.builder()
                        .name("Dr. Sarah Smith")
                        .specialization("Cardiology")
                        .phone("555-0299")
                        .email("sarah.smith@hospital.com")
                        .build());

                // Doctor 2
                doctorRepository.save(Doctor.builder()
                        .name("Dr. John Doe")
                        .specialization("Cardiology")
                        .phone("1234567890")
                        .email("john.doe@example.com")
                        .build());

                // Doctor 3: Dr. Haasini (ID = 3)
                doctorRepository.save(Doctor.builder()
                        .name("Dr. Haasini")
                        .specialization("Neurology")
                        .phone("9876543210")
                        .email("dr.haasini@hospital.com")
                        .build());
            }

            if (patientRepository.count() == 0) {
                patientRepository.save(Patient.builder()
                        .name("John Doe")
                        .dob(LocalDate.of(1990, 1, 1))
                        .gender("Male")
                        .contact("9876543210")
                        .address("New Delhi")
                        .build());
            }
        };
    }
}
