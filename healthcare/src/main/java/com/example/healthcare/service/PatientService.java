package com.example.healthcare.service;

import com.example.healthcare.entity.Patient;
import com.example.healthcare.exception.ResourceNotFoundException;
import com.example.healthcare.repository.PatientRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class PatientService {

    private final PatientRepository patientRepository;

    public Patient createPatient(Patient patient) {
        return patientRepository.save(patient);
    }

    public List<Patient> getAllPatients() {
        return patientRepository.findAll();
    }

    public Patient getPatientById(Long id) {
        return patientRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Patient not found with id: " + id));
    }

    public Patient updatePatient(Long id, Patient patientDetails) {
        Patient patient = getPatientById(id);

        patient.setName(patientDetails.getName());
        patient.setDob(patientDetails.getDob());
        patient.setGender(patientDetails.getGender());
        patient.setContact(patientDetails.getContact());
        patient.setAddress(patientDetails.getAddress());

        return patientRepository.save(patient);
    }

    public void deletePatient(Long id) {
        Patient patient = getPatientById(id);
        patientRepository.delete(patient);
    }
}
