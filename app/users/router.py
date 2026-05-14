from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.users.repository import UserRepository
from app.users.schemas import UserCreate, UserRead
from app.users.service import UserService
from app.deps import get_db


router = APIRouter()

def get_user_service(db: Session = Depends(get_db)): 
    repository = UserRepository(db)
    return UserService(repository)


@router.post("/users", response_model=UserRead, status_code=201)
async def create_user(
    payload: UserCreate, 
    service: UserService = Depends(get_user_service),
):
    try: 
        return service.create_user(
            name=payload.name,
            email=payload.email,
            password=payload.password,
            role=payload.role,
        )
    except ValueError as e: 
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users", response_model=list[UserRead], status_code=200)
async def list_users(
    service: UserService = Depends(get_user_service)
): 
    try: 
        return service.list_users()
    except ValueError: 
        raise HTTPException(status_code=400)

@router.get("/users/{user_id}", response_model=UserRead, status_code=200)
async def get_user(
    user_id: int, 
    service: UserService = Depends(get_user_service)
): 
    try: 
        return service.get_user(user_id)
    except ValueError: 
        raise HTTPException(status_code=404, detail="User Not Found.")
    
@router.delete("/users/{user_id}", status_code=200)
async def delete_user(
    user_id: int, 
    service: UserService = Depends(get_user_service)
):
    try: 
        service.delete_user(user_id)
    except ValueError: 
        raise HTTPException(status_code=404, detail="User Not Found.")
