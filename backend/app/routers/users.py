    from fastapi import APIRouter, Depends, HTTPException
    from sqlalchemy.ext.asyncio import AsyncSession
    from ..database import get_db
    from ..models.user import User
    from ..schemas.user import UserCreate, UserRead

    router = APIRouter(prefix="/users", tags=["Users"])

    @router.post("/", response_model=UserRead)
    async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
        """Создание нового пользователя"""
        user = User(**user_in.dict())
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @router.get("/{user_id}", response_model=UserRead)
    async def get_user(user_id: str, db: AsyncSession = Depends(get_db)):
        """Получение пользователя по ID"""
        user = await db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        return user

    @router.get("/", response_model=list[UserRead])
    async def list_users(db: AsyncSession = Depends(get_db)):
        """Список всех пользователей"""
        result = await db.execute(select(User))
        return result.scalars().all()
    ```
  - `routers/notifications.py`:
    ```python
