from flask import Flask, jsonify, request

app = Flask(__name__)
employees = []
next_employee_id = 1


@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)


@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            return jsonify(employee)
    return jsonify({'message': 'Employee not found'}), 404


@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    global next_employee_id
    employee = {
        'id': next_employee_id,
        'name': data['name'],
        'surname': data['surname'],
        'role': data['role']
    }
    employees.append(employee)
    next_employee_id += 1
    return jsonify(employee), 201


@app.route('/employees/<int:employee_id>', methods=['PUT'])
def modify_employee(employee_id):
    data = request.get_json()
    for employee in employees:
        if employee['id'] == employee_id:
            employee['name'] = data['name']
            employee['surname'] = data['surname']
            employee['role'] = data['role']
            return jsonify(employee)
    return jsonify({'message': 'Employee not found'}), 404


@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            employees.remove(employee)
            return jsonify(employee)
    return jsonify({'message': 'Employee not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)