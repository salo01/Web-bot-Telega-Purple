    from sqlalchemy import Column, String, Boolean
    from sqlalchemy.dialects.postgresql import UUID
    import uuid
    from ..database import Base

    class User(Base):
        __tablename__ = 'users'
        # Уникальный идентификатор пользователя
        id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
        # Discord ID пользователя
        discord_id = Column(String, unique=True, index=True, nullable=False)
        # Имя пользователя из Discord
        username = Column(String, nullable=False)
        # Флаг администратора
        is_admin = Column(Boolean, default=False)
    ```
  - `models/notification.py`:
    ```python
