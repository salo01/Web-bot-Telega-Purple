from sqlalchemy import Column, String, Text, ForeignKey
    from sqlalchemy.dialects.postgresql import UUID
    import uuid
    from ..database import Base

    class Template(Base):
        __tablename__ = 'templates'
        # Уникальный идентификатор шаблона
        id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
        # Название шаблона
        name = Column(String, nullable=False)
        # Тело шаблона с поддержкой переменных
        body = Column(Text, nullable=False)
        # Связь с пользователем-владельцем
        owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    ```
- `routers/`: модули API-эндпоинтов для CRUD-операций.
  - `routers/users.py`:
    ```python
