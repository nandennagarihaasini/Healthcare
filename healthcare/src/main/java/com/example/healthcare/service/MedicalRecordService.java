package com.example.healthcare.service;

import com.example.healthcare.entity.MedicalRecord;
import com.example.healthcare.entity.Patient;
import com.example.healthcare.exception.ResourceNotFoundException;
import com.example.healthcare.repository.MedicalRecordRepository;
import com.example.healthcare.repository.PatientRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class MedicalRecordService {

    private final MedicalRecordRepository medicalRecordRepository;
    private final PatientRepository patientRepository;

    public MedicalRecord createMedicalRecord(MedicalRecord record) {
        // Validate Patient exists
        Patient patient = patientRepository.findById(record.getPatient().getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient not found with id: " + record.getPatient().getId()));
        
        record.setPatient(patient);
        return medicalRecordRepository.save(record);
    }

    public List<MedicalRecord> getAllMedicalRecords() {
        return medicalRecordRepository.findAll();
    }

    public MedicalRecord getMedicalRecordById(Long id) {
        return medicalRecordRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Medical Record not found with id: " + id));
    }

    public MedicalRecord updateMedicalRecord(Long id, MedicalRecord recordDetails) {
        MedicalRecord record = getMedicalRecordById(id);

        if (recordDetails.getPatient() != null && recordDetails.getPatient().getId() != null) {
            Patient patient = patientRepository.findById(recordDetails.getPatient().getId())
                    .orElseThrow(() -> new ResourceNotFoundException("Patient not found with id: " + recordDetails.getPatient().getId()));
            record.setPatient(patient);
        }

        record.setDiagnosis(recordDetails.getDiagnosis());
        record.setTreatment(recordDetails.getTreatment());

        return medicalRecordRepository.save(record);
    }

    public void deleteMedicalRecord(Long id) {
        MedicalRecord record = getMedicalRecordById(id);
        medicalRecordRepository.delete(record);
    }
}
