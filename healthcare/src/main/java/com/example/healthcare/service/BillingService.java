package com.example.healthcare.service;

import com.example.healthcare.entity.Appointment;
import com.example.healthcare.entity.Billing;
import com.example.healthcare.exception.ResourceNotFoundException;
import com.example.healthcare.repository.AppointmentRepository;
import com.example.healthcare.repository.BillingRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class BillingService {

    private final BillingRepository billingRepository;
    private final AppointmentRepository appointmentRepository;

    public Billing createBilling(Billing billing) {
        // Validate Appointment exists
        Appointment appointment = appointmentRepository.findById(billing.getAppointment().getId())
                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found with id: " + billing.getAppointment().getId()));
        
        billing.setAppointment(appointment);
        return billingRepository.save(billing);
    }

    public List<Billing> getAllBillingRecords() {
        return billingRepository.findAll();
    }

    public Billing getBillingById(Long id) {
        return billingRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Billing record not found with id: " + id));
    }

    public Billing updateBilling(Long id, Billing billingDetails) {
        Billing billing = getBillingById(id);

        if (billingDetails.getAppointment() != null && billingDetails.getAppointment().getId() != null) {
            Appointment appointment = appointmentRepository.findById(billingDetails.getAppointment().getId())
                    .orElseThrow(() -> new ResourceNotFoundException("Appointment not found with id: " + billingDetails.getAppointment().getId()));
            billing.setAppointment(appointment);
        }

        billing.setAmount(billingDetails.getAmount());
        billing.setStatus(billingDetails.getStatus());

        return billingRepository.save(billing);
    }

    public void deleteBilling(Long id) {
        Billing billing = getBillingById(id);
        billingRepository.delete(billing);
    }
}
