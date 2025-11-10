import frappe
import re
def validation_item_type(Item_type):
    Item_type= sanitize_text(Item_type)
    if not Item_name:
        frappe.throw("Item name is required")
    if not re.match(r'^[\w\- ]+$', Item_type):
        frappe.throw("Item name contains invalid characters")
    return Item_type
def validation_item_price(Item_price):
    if not Item_price:
        frappe.throw("Item price is required")    
    try:
        Item_price=float(Item_price)
    except(ValueError, TypeError):
        frappe.throw("Price must be a number")
    if Item_price <0:
        frappe.throw("Price must be greater than 0")
    return Item_price
def validation_item_model(Item_model):
    Item_code=sanitize_text(Item_model)
    if not Item_model:
        frappe.frappe.throw("Item Code is required")
    if frappe.db.exists("Item",{"model":Item_model}):
        frappe.throw(f"Item Code '{Item_model}' already exists")
    return Item_model
def validation_item_delete(Item_model):
    if not Item_model:
        frappe.throw("Item is required")
    if not frappe.db.exists("Item",Item_model):
        frappe.throw("Item does not exist")
    if not frappe.has_permission("Item","delete"):
        frappe.throw("You do not have permission to delete this company")
    return Item_model