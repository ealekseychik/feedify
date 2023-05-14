from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

Base = DeclarativeBase()

GroupToUser = Table(
    'mtm_group_to_user',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('tg_user_id', Integer, ForeignKey('tg_users.id')),
    Column('vk_user_id', Integer, ForeignKey('vk_group.id')))


class User(Base):
    __tablename__ = 'tg_users'

    id = Column(Integer(), primary_key=True)
    tg_id = Column(String(20), nullable=False, primary_key=True)
    created_on = Column(DateTime(), default=datetime.now)

    groups = relationship(secondary=GroupToUser, back_populates='users')


class Group(Base):
    __tablename__ = 'vk_group'

    id = Column(Integer(), primary_key=True)
    vk_id = Column(String(20), nullable=False, primary_key=True)
    updated_on = Column(DateTime(), default=datetime.now)
    last_id = Column(Integer(), nullable=True)

    users = relationship(secondary=GroupToUser, back_populates='groups')
