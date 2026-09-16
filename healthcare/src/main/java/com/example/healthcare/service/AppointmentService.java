package com.example.healthcare.service;

import com.example.healthcare.entity.Appointment;
import com.example.healthcare.entity.Doctor;
import com.example.healthcare.entity.Patient;
import com.example.healthcare.exception.ResourceNotFoundException;
import com.example.healthcare.repository.AppointmentRepository;
import com.example.healthcare.repository.DoctorRepository;
import com.example.healthcare.repository.PatientRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class AppointmentService {

    private final AppointmentRepository appointmentRepository;
    private final PatientRepository patientRepository;
    private final DoctorRepository doctorRepository;

    public Appointment createAppointment(Appointment appointment) {
        // Validate Patient exists
        Patient patient = patientRepository.findById(appointment.getPatient().getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient not found with id: " + appointment.getPatient().getId()));

        // Validate Doctor exists
        Doctor doctor = doctorRepository.findById(appointment.getDoctor().getId())
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found with id: " + appointment.getDoctor().getId()));

        appointment.setPatient(patient);
        appointment.setDoctor(doctor);

        return appointmentRepository.save(appointment);
    }

    public List<Appointment> getAllAppointments() {
        return appointmentRepository.findAll();
    }

    public Appointment getAppointmentById(Long id) {
        return appointmentRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found with id: " + id));
    }

    public Appointment updateAppointment(Long id, Appointment appointmentDetails) {
        Appointment appointment = getAppointmentById(id);

        // Validate and update Patient if provided
        if (appointmentDetails.getPatient() != null && appointmentDetails.getPatient().getId() != null) {
            Patient patient = patientRepository.findById(appointmentDetails.getPatient().getId())
                    .orElseThrow(() -> new ResourceNotFoundException("Patient not found with id: " + appointmentDetails.getPatient().getId()));
            appointment.setPatient(patient);
        }

        // Validate and update Doctor if provided
        if (appointmentDetails.getDoctor() != null && appointmentDetails.getDoctor().getId() != null) {
            Doctor doctor = doctorRepository.findById(appointmentDetails.getDoctor().getId())
                    .orElseThrow(() -> new ResourceNotFoundException("Doctor not found with id: " + appointmentDetails.getDoctor().getId()));
            appointment.setDoctor(doctor);
        }

        appointment.setAppointmentDate(appointmentDetails.getAppointmentDate());
        appointment.setReason(appointmentDetails.getReason());
        appointment.setStatus(appointmentDetails.getStatus());

        return appointmentRepository.save(appointment);
    }

    public void deleteAppointment(Long id) {
        Appointment appointment = getAppointmentById(id);
        appointmentRepository.delete(appointment);
    }
}
