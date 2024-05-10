from sqlalchemy import (Column, String, Integer, Float, DateTime, ForeignKey, Boolean, Date)
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)  # Added String type for password
    reg_date = Column(DateTime)
   # posts = relationship("Product", back_populates="prod_fk")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    prod_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, unique=True)
    main_text = Column(String, nullable=True)
    price = Column(String, nullable=True)
    reg_date = Column(DateTime)
    prod_fk = relationship(User, lazy="subquery")

class ProdPhoto(Base):
    __tablename__ = "prod_photos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    photo_path = Column(String, nullable=False)
    reg_date = Column(DateTime)
    post_fk = relationship(Product, lazy="subquery")