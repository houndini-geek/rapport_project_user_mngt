from app import db
from sqlalchemy import String, text
from sqlalchemy.orm import Mapped,mapped_column
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id : Mapped[int] =  mapped_column(primary_key=True)
    user_id : Mapped[uuid.UUID] =  mapped_column(default=uuid.uuid4)
    logon_name : Mapped[str] =  mapped_column(String(80),unique=True)
    display_name : Mapped[str] =  mapped_column(String(150))
    user_role : Mapped[str] =  mapped_column(String(50), default='user', server_default=text('user'),)
    department : Mapped[str] =  mapped_column(String(100))
    site_name : Mapped[str] =  mapped_column(String(100))
    password_hash : Mapped[str] =  mapped_column(String(255))
    first_time_login : Mapped[bool] = mapped_column(
        default=True,
        server_default=text('true'),
    )
    is_active : Mapped[bool] = mapped_column(
        default=True,
        server_default=text('true'),
    )