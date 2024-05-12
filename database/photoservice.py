from database import get_db
from database.models import ProdPhoto
from datetime import datetime

def add_photo_db(prod_id, photo_path):
    db = next(get_db())
    photo = ProdPhoto(product_id=prod_id, photo_path=photo_path, reg_date=datetime.now())
    db.add(photo)
    db.commit()
    return prod_id
