from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, default=True)
    password = Column(String)

    works = relationship('Work', order_by='Work.time.desc()')
    conns = relationship('Conn', order_by='Conn.time.desc()')

    def __repr__(self):
        return f"User({self.id} {self.email} {self.password})"


class Conn(Base):
    __tablename__ = "conns"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String)
    time = Column(Date)
    ip = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"Conn({self.id} {self.email} {self.time} {self.ip})"


class Work(Base):
    __tablename__ = "works"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    time = Column(Date)
    n = Column(Integer)
    p = Column(Integer)
    q = Column(Integer)
    status = Column(String)
    elapsed = Column(String)
    email = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Work({self.id} {self.time} {self.n} {self.p} {self.q} {self.status} {self.elapsed} {self.email})"
