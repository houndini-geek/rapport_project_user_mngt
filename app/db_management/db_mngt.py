from app import db
import uuid

from werkzeug.security import generate_password_hash

from app.models import User


class DbManagement:
    def __init__(self) -> None:
        pass


    # logon_name : Mapped[str] =  mapped_column(String(80),unique=True)
    # display_name : Mapped[str] =  mapped_column(String(150))
    # user_role : Mapped[str] =  mapped_column(String(50), default='user', server_default=text('user'),)
    # department : Mapped[str] =  mapped_column(String(100))
    # site_name : Mapped[str] =  mapped_column(String(100))
    # first_time_login : Mapped[bool] = mapped_column(
    #     default=True,
    #     server_default=text('true'),
    # )
    # is_active : Mapped[bool] = mapped_column(
    #     default=True,
    #     server_default=text('true'),
    # )

    def save_user(self,user_info):
            user_id = uuid.uuid4()
            user = User(
                 logon_name =  user_info['logon_name'],
                 display_name = user_info['display_name'],
                 user_id = user_id,
                 user_role = user_info['user_role'],
                 department = user_info['department'],
                 site_name = user_info['site_name'],
                 password_hash = generate_password_hash(user_info['initial_password']),
                 first_time_login = True,
                 is_active = user_info['is_active']
            )
            db.session.add(user)
            db.session.commit()
            print('User created!')
      
