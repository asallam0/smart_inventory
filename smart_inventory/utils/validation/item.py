import frappe
import re
def validate_item_exists(model):
    if not frappe.db.exists("Item",model):
        frappe.throw("Item does not exist")
    return model 
def validate_unique_item_model(model):
    

    if not model:
        frappe.throw("Item Model is required")

    if frappe.db.exists("Item", {"model": model}):
        frappe.throw(f"Item Model '{model}' already exists")

    return model

def validate_item_type(item_type):
    
    if not item_type:
        frappe.throw("IItem Type is required")
    if not re.match(r'^[\w\- ]+$', item_type):
        frappe.throw("Item Type contains invalid characters")
    return item_type
def validate_item_price(item_price):
    if not item_price:
        frappe.throw("Item price is required")    
    try:
        Item_price=float(item_price)
    except(ValueError, TypeError):
        frappe.throw("Price must be a numeric value")
    if item_price <0:
        frappe.throw("Price must be greater than 0")
    return item_price
def check_permission_create():
    if not frappe.has_permission("Item", "create"):
        frappe.throw("You do not have permission to create an Item")



def check_permission_update(model):
    validate_item_exists(model)

    if not frappe.has_permission("Item", "write"):
        frappe.throw("You do not have permission to update this Item")

    return model


def check_permission_delete(model):
    validate_item_exists(model)

    if not frappe.has_permission("Item", "delete"):
        frappe.throw("You do not have permission to delete this Item")

    return model