#!/bin/bash

# Add an employee
echo "Adding an employee..."
curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "name": "John", "surname": "Doe", "role": "Engineer"}' http://localhost:5000/employees
echo ""

# Get all employees
echo "Getting all employees..."
curl http://localhost:5000/employees
echo ""

# Get an employee by ID
echo "Getting an employee by ID..."
curl http://localhost:5000/employees/1
echo ""

# Modify an employee
echo "Modifying an employee..."
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Jane", "surname": "Smith", "role": "Manager"}' http://localhost:5000/employees/1
echo ""

# Get the modified employee
echo "Getting the modified employee..."
curl http://localhost:5000/employees/1
echo ""
