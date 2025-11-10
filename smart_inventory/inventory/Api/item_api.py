import frappe
from smart_inventory.inventory.validations.item_validators import validation_item_type
from smart_inventory.inventory.validations.item_validators import validation_item_price
from smart_inventory.inventory.validations.item_validators import validation_item_model
from smart_inventory.inventory.validations.item_validators import validation_item_delete
from smart_inventory.inventory.utlis.response.success_response import send as success
from smart_inventory.inventory.utlis.response..error_response import send as error
@frappe.whitelist(allow_guest=True)
def get_item(Item_type):
    if not Item_model:
        frappe.throw("Enter The Itme Name")  
    try:
         doc_Item= frappe.get_doc("Item",Item_model ,
          [model,price,stock_quantity],
           as_dict = True)
    except Exception as e:
        error(message=f"404 if the Item not found: {str(e)}")
    else:
        success(
            message="Item fetched successfully",
            data= doc_Item
        )         
@frappe.whitelist()
def Create_item(**date):
    try:
        data["model"] = validation_item_model(data.get("model"))
        data["type"] = validation_item_type(data.get("type"))
        data["price"] = validation_item_price(data.get("price"))
        item = frappe.new_doc("Item")
        item.update(data)
        item.insert()
        frappe.db.commit()
    except Exception as e :
         error(message=str(e))
    else:
        success(
            message="Item Create successfully",
            data= item
        )
@frappe.whitelist()
def delete_item(Item_model):
    try:
        Item_model=validation_item_delete(Item_model)
        frappe.delete_doc("Item",Item_model)
        frappe.db.commit()
    except Exception as e:
        error(message=str(e))
    else:
         success(message="Company deleted successfully")
    
    
    