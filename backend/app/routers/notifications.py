    from fastapi import APIRouter, Depends, HTTPException
    from sqlalchemy.ext.asyncio import AsyncSession
    from ..database import get_db
    from ..models.notification import Notification
    from ..schemas.notification import NotificationCreate, NotificationRead

    router = APIRouter(prefix="/notifications", tags=["Notifications"])

    @router.post("/", response_model=NotificationRead)
    async def create_notification(
        notif_in: NotificationCreate,
        db: AsyncSession = Depends(get_db)
    ):
        """Создать новое уведомление"""
        notif = Notification(**notif_in.dict())
        db.add(notif)
        await db.commit()
        await db.refresh(notif)
        return notif

    @router.get("/{notif_id}", response_model=NotificationRead)
    async def get_notification(notif_id: str, db: AsyncSession = Depends(get_db)):
        """Получить уведомление по ID"""
        notif = await db.get(Notification, notif_id)
        if not notif:
            raise HTTPException(status_code=404, detail="Уведомление не найдено")
        return notif
    ```
  - `routers/templates.py`:
    ```python
