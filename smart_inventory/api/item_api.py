import frappe
from smart_inventory.utils.validation.item import (
    validate_item_exists,
    validate_unique_item_model,
    validate_item_price,
    validate_item_type,
    check_permission_create,
    check_permission_update,
    check_permission_delete
)

from smart_inventory.utils.response.success_response import send as success
from smart_inventory.utils.response.error_response import send as error
@frappe.whitelist(allow_guest=True)
def get_item(model:str):
    """Fetch a single Item by model"""
    if not model:
        return error(message="Item model is required")
    try:
         model=validate_item_exists(model)
         item = frappe.get_doc("Item", model)
    except Exception as e:
        return error(message=f"Item not found: {str(e)}")
    return success(
        message="Item fetched successfully",
        data=item.as_dict()
    )         
@frappe.whitelist()
def create_item(**data):
    try:
        check_permission_create()
        data["model"] = validate_unique_item_model(data.get("model"))
        data["type"] = validate_item_type(data.get("type"))
        data["price"] = validate_item_price(data.get("price"))
        item = frappe.new_doc("Item")
        item.update(data)
        item.insert()
        frappe.db.commit()
    except Exception as e :
         return error(message=str(e))
    return success(
            message="Item Create successfully",
            data= item)
        
@frappe.whitelist()  
def update_item(model,**data):
    try:
        check_permission_update(model)
        item = frappe.get_doc("Item", model)
        if "type" in data:
            data["type"] = validate_item_type(data["type"])
        if "price" in data:
            data["price"] = validate_item_price(data["price"])
        item.update(data)
        item.save()
        frappe.db.commit()
    except Exception as e :
        return error(message=str(e))
    return success(
        message="Item updated successfully",
        data=item
    )
@frappe.whitelist()
def delete_item(model:str):
    try:
        check_permission_delete(model)
        frappe.delete_doc("Item",model)
        frappe.db.commit()
    except Exception as e:
        return error(message=str(e))
    return success(message="Item deleted successfully")
         
    