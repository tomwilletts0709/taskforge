from sqlalchemy import select
from sqlalchemy.orm import Session

from app.users.models import Users
from app.domain import Roles


class UserRepository:
    def __init__(self, db: Session): 
        self.db = db

    def create_user(self, user: Users) -> Users:
        self.db.add(user)
        self.db.commit() 
        self.db.refresh(user) 
        return user
    
    def update_user(self, user_id: int, name: str, email: str, role: Roles) -> Users:  
        statement = select(Users).where(Users.id  == user_id)
        user = self.db.execute(statement).scalars().first()

        if user is None: 
            raise ValueError("No User ID Found")
        
        user.name = name
        user.email = email
        user.role = role.value
        
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_user(self, user_id: int, name: str) -> Users:
        statement = select(Users).where(Users.id == user_id)
        result = self.db.execute(statement).scalars().first()

        if result is None: 
            raise ValueError("Not Found")
        return result
    
    def list_users(self) -> list[Users]: 
        statement = select(Users)
        users = self.db.execute(statement).scalars().all()
        return users
    

    #may get rid of for front facing users as they may just become inactive. Will have a think.
    def delete_user(self, user_id: int) -> Users: 
        statement = select(Users).where(Users.id == user_id)
        result = self.db.execute(statement).scalars().first() 
        
        if result is None: 
            raise ValueError("No User ID Found")
        
        self.db.delete(result)
        self.db.commit()
        return result 