from pydantic import BaseModel, model_validator


class UserCreate(BaseModel): 
    name: str = Field(min_length=5, max_length=50)
    email: str 
    password: str = Field(min_legnth=5, max_length=50)
    password_repeat: str = Field(min_length=5, max_length=50)

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.password_repeat:
            raise ValueError("Passwords Do Not Match. Try Again.")
        return self
    
class UserRead(BaseModel): 
    id: int
    name: str
    email: str
    is_active: bool = True #would need to add email verification in here

