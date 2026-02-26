package com.erp.erp.adapter.in.web.controller;

import com.erp.erp.infrastructure.security.JwtTokenProvider;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping("/api/v1/auth")
public class AuthController {

    private final JwtTokenProvider jwtTokenProvider;

    public AuthController(JwtTokenProvider jwtTokenProvider) {
        this.jwtTokenProvider = jwtTokenProvider;
    }
    
    @GetMapping("/me")
    public ResponseEntity<Map<String, Object>> me() {
        Map<String, Object> response = Map.of(
            "id",       jwtTokenProvider.getCurrentUserId().orElse("unknown"),
            "username", jwtTokenProvider.getCurrentUsername().orElse("unknown"),
            "email",    jwtTokenProvider.getCurrentEmail().orElse("unknown"),
            "roles",    jwtTokenProvider.getCurrentRoles()
        );
        return ResponseEntity.ok(response);
    }
}
