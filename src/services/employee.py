# src/services/employee.py

from src.supa.client import sb
from src.models.users import User
import httpx

class DatabaseEmployeeService:
    def get_employee_by_code(self, employee_code: str) -> User:
        user_response = sb.auth.admin.get_user_by_id(employee_code)
        return User.from_response(user_response)

class RestEmployeeService:
    def fetch_employee(self, employee_code: str) -> User:
        response = httpx.get(f"http://localhost:8000/users/{employee_code}")
        response.raise_for_status()
        return User(**response.json())

class EmployeeServiceAdapter:
    def __init__(self, service):
        self.service = service

    def get_employee(self, employee_code: str) -> User:
        if isinstance(self.service, DatabaseEmployeeService):
            return self.service.get_employee_by_code(employee_code)
        elif isinstance(self.service, RestEmployeeService):
            return self.service.fetch_employee(employee_code)
        else:
            raise ValueError("Unsupported service type")