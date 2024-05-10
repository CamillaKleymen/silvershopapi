from fastapi import Request, Body, UploadFile, APIRouter
from database.photoservice import *
from database.productservice import *
from urllib import request

prod_routers = APIRouter(prefix="/products",
                          tags=["Product management"])

#add post
@prod_routers.post("/api/add_prod")
async def add_prod(product_id: int, main_text: str, price=float):
    new_prod = add_prod(product_id=product_id, main_text=main_text, price=price)
    if new_prod:
        return {"status": 1, "message": "Product successfully added"}
    return {"status":0, "message": "Product wasn't added"}

#get all or exact post

@prod_routers.get("/api/products/")
async def get_all_or_exact_prod(product_id: int):
    prod = get_product_db(product_id)
    if prod:
        return {"status": 1, "message": prod}
    return {"status": 0, "message": "Product not found"}

# change data
@prod_routers.put("api/products/")
async def change_product(product_id: int, main_text: str, price: float):
    if product_id and main_text and price:
        change_prod_data_db(product_id, main_text, price)
        return {"status":1, "message":"Product successfully changed"}
    return {"status":0, "message":"Error"}

@prod_routers.delete("api/products")
async def delete_product(product_id: int):
    try:
        delete_product(product_id)
        return {"status":1, "message": "Product successfully deleted"}
    except:
        return {"status": 0, "message": "Product wasn't deleted "}




