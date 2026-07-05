import httpx

from app.config import get_settings
from app.core.exceptions import UpstreamMeError
from app.schemas.auth import DepartmentRef, UserDepartmentRef, UserProfile


async def fetch_me(bearer_token: str) -> UserProfile:
    settings = get_settings()
    url = f"{settings.node_backend_url.rstrip('/')}/me"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                url,
                headers={"Authorization": f"Bearer {bearer_token}"},
            )
    except httpx.HTTPError as exc:
        raise UpstreamMeError(f"Failed to reach Node backend /me: {exc}") from exc

    if response.status_code != 200:
        raise UpstreamMeError(f"Node backend /me returned status {response.status_code}")

    try:
        payload = response.json()
    except ValueError as exc:
        raise UpstreamMeError("Node backend /me returned non-JSON response") from exc

    # backend_botivate_os wraps every response in an ApiResponse envelope:
    # {"success": true, "message": "...", "data": {...profile fields...}}.
    # Unwrap it here; fall back to the raw payload if it's ever returned unwrapped.
    data = payload.get("data", payload) if isinstance(payload, dict) else payload

    return _parse_user_profile(data)


def _parse_user_profile(data: dict) -> UserProfile:
    department = None
    if data.get("department"):
        department = DepartmentRef(
            id=data["department"]["id"],
            name=data["department"]["name"],
            code=data["department"].get("code"),
        )

    user_departments = []
    for entry in data.get("userDepartments", []) or []:
        dept = entry.get("department")
        if not dept:
            continue
        user_departments.append(
            UserDepartmentRef(
                department=DepartmentRef(
                    id=dept["id"],
                    name=dept["name"],
                    code=dept.get("code"),
                ),
                is_primary=entry.get("isPrimary", False),
            )
        )

    return UserProfile(
        id=data["id"],
        role=data["role"],
        department=department,
        user_departments=user_departments,
    )


def collect_department_names(profile: UserProfile) -> list[str]:
    names: list[str] = []
    if profile.department:
        names.append(profile.department.name)
        if profile.department.code:
            names.append(profile.department.code)
    for entry in profile.user_departments:
        names.append(entry.department.name)
        if entry.department.code:
            names.append(entry.department.code)
    # de-duplicate while preserving order
    seen: set[str] = set()
    unique_names = []
    for name in names:
        if name not in seen:
            seen.add(name)
            unique_names.append(name)
    return unique_names
