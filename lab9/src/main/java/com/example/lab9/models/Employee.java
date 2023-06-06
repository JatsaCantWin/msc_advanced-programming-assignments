package com.example.lab9.models;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class Employee {
    @Id
    private String id;
    private String name;
    private String surname;
    private String role;

    public Employee() {
    }

    public Employee(String id, String name, String surname, String role) {
        this.id = id;
        this.name = name;
        this.surname = surname;
        this.role = role;
    }

    public String getId() {
        return id;
    }
    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getSurname() {
        return surname;
    }
    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getRole() {
        return role;
    }
    public void setRole(String role) {
        this.role = role;
    }
}
