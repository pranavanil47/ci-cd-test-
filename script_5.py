# 3. Create vulnerable Java application with Maven
pom_xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example</groupId>
    <artifactId>vulnerable-java-app</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>
    
    <name>Vulnerable Java App</name>
    <description>Intentionally vulnerable Java application for Trivy testing</description>
    
    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <dependencies>
        <!-- Vulnerable Spring Framework versions -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>4.3.18.RELEASE</version> <!-- CVE-2018-15756 -->
        </dependency>
        
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-web</artifactId>
            <version>4.3.18.RELEASE</version> <!-- Multiple CVEs -->
        </dependency>
        
        <!-- Vulnerable Jackson versions -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.9.8</version> <!-- Multiple deserialization CVEs -->
        </dependency>
        
        <!-- Vulnerable Apache Commons -->
        <dependency>
            <groupId>commons-collections</groupId>
            <artifactId>commons-collections</artifactId>
            <version>3.2.1</version> <!-- CVE-2015-6420 -->
        </dependency>
        
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-compress</artifactId>
            <version>1.15</version> <!-- CVE-2018-11771 -->
        </dependency>
        
        <!-- Vulnerable Log4j -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.14.1</version> <!-- CVE-2021-44228 Log4Shell -->
        </dependency>
        
        <!-- Vulnerable Struts -->
        <dependency>
            <groupId>org.apache.struts</groupId>
            <artifactId>struts2-core</artifactId>
            <version>2.3.34</version> <!-- Multiple RCE CVEs -->
        </dependency>
        
        <!-- Vulnerable XML processing -->
        <dependency>
            <groupId>org.dom4j</groupId>
            <artifactId>dom4j</artifactId>
            <version>2.0.0</version> <!-- XXE vulnerabilities -->
        </dependency>
        
        <!-- Vulnerable database drivers -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.15</version> <!-- Multiple CVEs -->
        </dependency>
        
        <!-- Vulnerable HTTP client -->
        <dependency>
            <groupId>org.apache.httpcomponents</groupId>
            <artifactId>httpclient</artifactId>
            <version>4.5.5</version> <!-- Multiple CVEs -->
        </dependency>
        
        <!-- Vulnerable JSON processing -->
        <dependency>
            <groupId>org.json</groupId>
            <artifactId>json</artifactId>
            <version>20180130</version> <!-- Denial of service -->
        </dependency>
        
        <!-- Vulnerable template engines -->
        <dependency>
            <groupId>org.freemarker</groupId>
            <artifactId>freemarker</artifactId>
            <version>2.3.26-incubating</version> <!-- Template injection -->
        </dependency>
        
        <!-- Vulnerable serialization -->
        <dependency>
            <groupId>org.apache.xbean</groupId>
            <artifactId>xbean-reflect</artifactId>
            <version>3.18</version> <!-- Deserialization issues -->
        </dependency>
        
        <!-- Vulnerable JWT library -->
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt</artifactId>
            <version>0.6.0</version> <!-- Algorithm confusion -->
        </dependency>
        
        <!-- Vulnerable Hibernate -->
        <dependency>
            <groupId>org.hibernate</groupId>
            <artifactId>hibernate-core</artifactId>
            <version>5.2.17.Final</version> <!-- SQL injection potential -->
        </dependency>
        
        <!-- Vulnerable Apache CXF -->
        <dependency>
            <groupId>org.apache.cxf</groupId>
            <artifactId>cxf-core</artifactId>
            <version>3.2.7</version> <!-- Multiple CVEs -->
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>8</source>
                    <target>8</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
'''

with open("vulnerable-java-app/pom.xml", "w") as f:
    f.write(pom_xml_content)

print("Created pom.xml with vulnerable Java dependencies")