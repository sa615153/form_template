from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declared_attr

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_URI_local
from config import DB_URI_linux
from sqlalchemy import create_engine

from database import Session
from sqlalchemy import or_

Base = declarative_base()

class MyMixin(object):
    __table_args__ = {'mysql_engine': 'InnoDB'}

class User(MyMixin,Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    nickname = Column(String(15),index=True,unique=True)
    email = Column(String(128),index=True,unique=True)
    role = Column(Integer,default=None)
    posts = Column(String(10),default="posts")

    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    @staticmethod
    def login_check(user_name):
        session = Session()
        user = session.query(User).filter(or_(
            User.nickname == user_name)).first()
        print session
        session.commit()
        if not user:
            return None
        return user

    def __repr__(self):
        return '<User %r>' % (self.nickname)










if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(DB_URI_local, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)