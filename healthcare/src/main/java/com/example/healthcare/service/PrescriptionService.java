package com.example.healthcare.service;

import com.example.healthcare.entity.Appointment;
import com.example.healthcare.entity.Prescription;
import com.example.healthcare.exception.ResourceNotFoundException;
import com.example.healthcare.repository.AppointmentRepository;
import com.example.healthcare.repository.PrescriptionRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class PrescriptionService {

    private final PrescriptionRepository prescriptionRepository;
    private final AppointmentRepository appointmentRepository;

    public Prescription createPrescription(Prescription prescription) {
        // Validate Appointment exists
        Appointment appointment = appointmentRepository.findById(prescription.getAppointment().getId())
                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found with id: " + prescription.getAppointment().getId()));
        
        prescription.setAppointment(appointment);
        return prescriptionRepository.save(prescription);
    }

    public List<Prescription> getAllPrescriptions() {
        return prescriptionRepository.findAll();
    }

    public Prescription getPrescriptionById(Long id) {
        return prescriptionRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Prescription not found with id: " + id));
    }

    public Prescription updatePrescription(Long id, Prescription prescriptionDetails) {
        Prescription prescription = getPrescriptionById(id);

        if (prescriptionDetails.getAppointment() != null && prescriptionDetails.getAppointment().getId() != null) {
            Appointment appointment = appointmentRepository.findById(prescriptionDetails.getAppointment().getId())
                    .orElseThrow(() -> new ResourceNotFoundException("Appointment not found with id: " + prescriptionDetails.getAppointment().getId()));
            prescription.setAppointment(appointment);
        }

        prescription.setMedication(prescriptionDetails.getMedication());
        prescription.setDosage(prescriptionDetails.getDosage());
        prescription.setInstructions(prescriptionDetails.getInstructions());

        return prescriptionRepository.save(prescription);
    }

    public void deletePrescription(Long id) {
        Prescription prescription = getPrescriptionById(id);
        prescriptionRepository.delete(prescription);
    }
}
