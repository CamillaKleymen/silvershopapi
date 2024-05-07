from sqlalchemy import (Column, String, Integer, Float, DateTime, ForeignKey, Boolean, Date)
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column
    reg_date = Column(DateTime)
    posts = relationship("products", back_populates="prod_fk")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, autoincrement=True, primary_key=True)
    prod_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, unique=True)
    main_text = Column(String, nullable=True)
    price = Column(String, nullable=True)
    reg_date = Column(DateTime)

    prod_fk = relationship(User, lazy="subquery")

class ProdPhoto(Base):
    __tablename__ = "prod_photos"
    id = Column(Integer, autoincrement=True, primary_key = True)
    post_id = Column(Integer, ForeignKey("user_posts.id"))
    photo_path=Column(String, nullable=False)
    reg_date = Column(DateTime)

    post_fk = relationship(Product, lazy="subquery")