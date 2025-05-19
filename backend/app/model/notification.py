    from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
    from sqlalchemy.dialects.postgresql import UUID
    import uuid
    from ..database import Base

    class Notification(Base):
        __tablename__ = 'notifications'
        # Уникальный идентификатор уведомления
        id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
        # Заголовок уведомления
        title = Column(String, nullable=False)
        # Текст сообщения или шаблон
        content = Column(String, nullable=False)
        # Дата и время следующей отправки
        next_run = Column(DateTime, nullable=False)
        # Флаг активного состояния
        is_active = Column(Boolean, default=True)
        # Связь с пользователем-организатором
        owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    ```
  - `models/template.py`:
    ```python
