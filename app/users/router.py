from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.users.repository import UserRepository
from app.users.schemas import UserCreate, UserRead, UserUpdate
from app.users.service import UserService
from app.deps import get_db


router = APIRouter()

def get_user_service(db: Session = Depends(get_db)): 
    repository = UserRepository(db)
    return UserService(repository)


@router.post("/user", response_model=UserRead, status_code=201)
async def create_user(
    payload: UserRead, 
    service: UserService = Depends
): 
    try: 
        return service.create_user(
            name=payload.name,
            email=payload.email,
            role=payload.role)
    except ValueError: 
        raise HTTPException(status_code=404, detail="No User ID Found")
    
@router.get("/user", response_model=UserRead, status_code=201)
async def list_users(
    payload: UserRead,
    service: UserService = Depends
): 
    try: 
        return service.list_users(
            name=payload.name,
            email=payload.email,
            role=payload.role
        )
    except ValueError: 
        raise HTTPException(status_code=500)

@router.get("/users"/{user_id}, response_model=UserRead, status_code=201)
async def get_user(
    
)

