package com.example.healthcare.controller;

import com.example.healthcare.entity.Billing;
import com.example.healthcare.service.BillingService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/billing")
@RequiredArgsConstructor
public class BillingController {

    private final BillingService billingService;

    @PostMapping
    public ResponseEntity<Billing> createBilling(@Valid @RequestBody Billing billing) {
        Billing createdBilling = billingService.createBilling(billing);
        return new ResponseEntity<>(createdBilling, HttpStatus.CREATED);
    }

    @GetMapping
    public ResponseEntity<List<Billing>> getAllBillingRecords() {
        return ResponseEntity.ok(billingService.getAllBillingRecords());
    }

    @GetMapping("/{id}")
    public ResponseEntity<Billing> getBillingById(@PathVariable Long id) {
        return ResponseEntity.ok(billingService.getBillingById(id));
    }

    @PutMapping("/{id}")
    public ResponseEntity<Billing> updateBilling(
            @PathVariable Long id,
            @Valid @RequestBody Billing billingDetails) {
        return ResponseEntity.ok(billingService.updateBilling(id, billingDetails));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteBilling(@PathVariable Long id) {
        billingService.deleteBilling(id);
        return ResponseEntity.noContent().build();
    }
}
