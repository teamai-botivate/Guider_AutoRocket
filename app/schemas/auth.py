from pydantic import BaseModel


class DecodedToken(BaseModel):
    user_id: str
    email: str | None = None
    role: str
    tenant_id: str
    name: str | None = None
    departments: list[str] = []


class DepartmentRef(BaseModel):
    id: str
    name: str
    code: str | None = None


class UserDepartmentRef(BaseModel):
    department: DepartmentRef
    is_primary: bool = False


class UserProfile(BaseModel):
    id: str
    role: str
    department: DepartmentRef | None = None
    user_departments: list[UserDepartmentRef] = []
