# example_usage.py

from src.services.employee import DatabaseEmployeeService, RestEmployeeService, EmployeeServiceAdapter
from src.models.users import User

def main():
    db_service = DatabaseEmployeeService()
    rest_service = RestEmployeeService()

    db_adapter = EmployeeServiceAdapter(db_service)
    rest_adapter = EmployeeServiceAdapter(rest_service)

    employee_code = "b193ffc0-b588-4fe3-886b-f1464e705c76"

    # Obtener empleado desde la base de datos
    employee_from_db = db_adapter.get_employee(employee_code)
    print("Employee from DB:", employee_from_db)

    # Obtener empleado desde el servicio REST
    employee_from_rest = rest_adapter.get_employee(employee_code)
    print("Employee from REST:", employee_from_rest)

if __name__ == "__main__":
    main()