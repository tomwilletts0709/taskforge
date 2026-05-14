import hashlib

from app.domain import Roles
from app.users.models import Users
from app.users.repository import UserRepository


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, name: str, email: str, password: str, role: Roles):
        password_hash = hash_password(password)

        user = Users(
            name=name,
            email=email,
            password_hash=password_hash,
            role=role.value,
        )

        user = self.user_repo.create_user(user)
        return user

    def get_user(self, user_id: int):
        return self.user_repo.get_user(user_id)

    def update_user(self, user_id: int, name: str, email: str, role: Roles):
        user = self.user_repo.update_user(
            user_id=user_id,
            name=name,
            email=email,
            role=role.value,
        )
        return user

    def delete_user(self, user_id: int):
        self.user_repo.delete_user(user_id)
        return None

    def list_users(self) -> list[Users]:
        users = self.user_repo.list_users()
        return users
