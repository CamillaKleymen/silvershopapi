from database import get_db
from database.models import User, Product, ProdPhoto
from datetime import datetime

# Getting data about prod
def get_all_or_exact_product_db(product_id):
    db = next(get_db())
    if product_id:
        exact_prod = db.query(Product).filter_by(id=product_id).first()
        return exact_prod
    elif product_id == 0:
        all_product = db.query(Product).all()
        return [ i for i in all_product]


# Redacting a prod
def change_prod_data_db(product_id, changeable_info, new_data):
    db = next(get_db())
    product = db.query(Product).filter_by(id=product_id).first()
    if product:
        try:
            if changeable_info == "main_text":
                product.main_text = new_data
                db.commit()
                return True
            elif changeable_info == "price":
                product.price = new_data
                db.commit()
                return True
            db.commit()
        except:
            return "Unfortunately at this moment changing of data unavailable"
    return False

# Deleting a post
def delete_product_db(product_id):
    db = next(get_db())
    prod_to_delete = db.query(Product).filter_by(id=product_id).first()
    if prod_to_delete:
        db.delete(prod_to_delete)
        db.commit()
        return True
    return False

#check exact product
def get_product_db(product_id: int):
    db = next(get_db())
    print(product_id)
    exact_product = db.query(Product).filter_by(id=product_id).first()
    print(exact_product)
    return exact_product


def add_product_db(name):
    db = next(get_db())
    new_product = Product(name=name, reg_date=datetime.now())
    db.add(new_product)
    db.commit()
    return True