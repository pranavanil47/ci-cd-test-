# Create Java application source code
os.makedirs("vulnerable-java-app/src/main/java/com/example", exist_ok=True)

java_app_content = '''package com.example;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.dom4j.Document;
import org.dom4j.DocumentHelper;
import org.json.JSONObject;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.HashMap;
import java.util.Map;

/**
 * Vulnerable Java application for Trivy SBOM and SCA testing
 * Contains intentionally vulnerable dependencies and code patterns
 */
@RestController
public class VulnerableApplication {
    
    private static final Logger logger = LogManager.getLogger(VulnerableApplication.class);
    private static final String SECRET_KEY = "insecure-secret-for-testing";
    
    @GetMapping("/")
    public Map<String, Object> home() {
        Map<String, Object> response = new HashMap<>();
        response.put("message", "Vulnerable Java app for Trivy testing");
        response.put("vulnerabilities", new String[]{
            "Spring Framework 4.3.18 - CVE-2018-15756",
            "Jackson 2.9.8 - Deserialization CVEs", 
            "Log4j 2.14.1 - CVE-2021-44228 (Log4Shell)",
            "Commons Collections 3.2.1 - CVE-2015-6420",
            "Struts 2.3.34 - Multiple RCE CVEs",
            "MySQL Connector 8.0.15 - Multiple CVEs",
            "And many more vulnerable dependencies..."
        });
        response.put("endpoints", new String[]{
            "/json - Jackson deserialization demo",
            "/xml - XXE vulnerability demo",
            "/log - Log4j injection demo",
            "/jwt - JWT vulnerabilities demo",
            "/sql - SQL injection demo"
        });
        
        return response;
    }
    
    @PostMapping("/json")
    public Map<String, Object> jsonDeserialization(@RequestBody String jsonData) {
        Map<String, Object> response = new HashMap<>();
        
        try {
            // Vulnerable Jackson deserialization - allows RCE
            ObjectMapper mapper = new ObjectMapper();
            mapper.enableDefaultTyping(); // Dangerous setting
            
            Object result = mapper.readValue(jsonData, Object.class);
            response.put("result", result.toString());
            response.put("warning", "Vulnerable Jackson deserialization used");
            
        } catch (Exception e) {
            response.put("error", e.getMessage());
            logger.error("JSON deserialization error: " + e.getMessage(), e);
        }
        
        return response;
    }
    
    @PostMapping("/xml")
    public Map<String, Object> xmlParsing(@RequestBody String xmlData) {
        Map<String, Object> response = new HashMap<>();
        
        try {
            // Vulnerable XML parsing - allows XXE attacks
            Document document = DocumentHelper.parseText(xmlData);
            response.put("result", document.asXML());
            response.put("warning", "Vulnerable XML parsing with XXE risk");
            
        } catch (Exception e) {
            response.put("error", e.getMessage());
            logger.error("XML parsing error: " + e.getMessage(), e);
        }
        
        return response;
    }
    
    @GetMapping("/log")
    public Map<String, Object> logInjection(@RequestParam String userInput) {
        Map<String, Object> response = new HashMap<>();
        
        // Vulnerable Log4j usage - allows JNDI injection (Log4Shell)
        logger.info("User input received: " + userInput);
        
        response.put("message", "Input logged with vulnerable Log4j");
        response.put("input", userInput);
        response.put("warning", "Log4j 2.14.1 vulnerable to CVE-2021-44228");
        
        return response;
    }
    
    @GetMapping("/jwt")
    public Map<String, Object> jwtVulnerability(@RequestParam String payload) {
        Map<String, Object> response = new HashMap<>();
        
        try {
            // Vulnerable JWT usage - algorithm confusion possible
            String token = Jwts.builder()
                .setSubject(payload)
                .signWith(SignatureAlgorithm.HS256, SECRET_KEY)
                .compact();
                
            response.put("token", token);
            response.put("warning", "Vulnerable JWT library with algorithm confusion risk");
            
        } catch (Exception e) {
            response.put("error", e.getMessage());
            logger.error("JWT error: " + e.getMessage(), e);
        }
        
        return response;
    }
    
    @GetMapping("/sql")
    public Map<String, Object> sqlInjection(@RequestParam String userId) {
        Map<String, Object> response = new HashMap<>();
        
        try {
            // Vulnerable SQL query - allows injection
            String query = "SELECT * FROM users WHERE id = " + userId;
            
            // Simulate database connection (vulnerable MySQL connector)
            Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/testdb", "user", "pass");
            PreparedStatement stmt = conn.prepareStatement(query);
            ResultSet rs = stmt.executeQuery();
            
            response.put("query", query);
            response.put("warning", "Vulnerable SQL query with injection risk");
            
        } catch (Exception e) {
            response.put("error", e.getMessage());
            logger.error("SQL error: " + e.getMessage(), e);
        }
        
        return response;
    }
    
    public static void main(String[] args) {
        System.out.println("Starting vulnerable Java application...");
        System.out.println("This app contains multiple vulnerable dependencies for Trivy testing");
        
        // Initialize vulnerable components for testing
        InvokerTransformer transformer = new InvokerTransformer("toString", null, null);
        JSONObject json = new JSONObject();
        
        System.out.println("Vulnerable Java app ready for SBOM and SCA analysis");
    }
}
'''

with open("vulnerable-java-app/src/main/java/com/example/VulnerableApplication.java", "w") as f:
    f.write(java_app_content)

print("Created VulnerableApplication.java")