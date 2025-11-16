from smart_inventory.utils.validation.item import (
    validation_item_type,
    validation_item_price,
    validation_item_model,
    validation_item_delete,
    validation_item_permission,
    validation_item_update,
)

from smart_inventory.utils.response.success_response import send as success
from smart_inventory.utils.response.error_response import send as error


# -------------------------------------------------------
# GET ITEM
# -------------------------------------------------------
@frappe.whitelist(allow_guest=True)
def get_item(model: str):
    """Fetch a single Item by model"""
    if not model:
        return error(message="Item model is required")

    try:
        model = validation_item_model(model)
        item = frappe.get_doc("Item", model)
    except Exception as e:
        return error(message=f"Item not found: {str(e)}")

    return success(
        message="Item fetched successfully",
        data=item.as_dict()
    )


# -------------------------------------------------------
# CREATE ITEM
# -------------------------------------------------------
@frappe.whitelist()
def create_item(**data):
    try:
        validation_item_permission()

        data["model"] = validation_item_model(data.get("model"))
        data["type"] = validation_item_type(data.get("type"))
        data["price"] = validation_item_price(data.get("price"))

        item = frappe.new_doc("Item")
        item.update(data)
        item.insert()
        frappe.db.commit()

    except Exception as e:
        return error(message=str(e))

    return success(
        message="Item created successfully",
        data=item
    )


# -------------------------------------------------------
# DELETE ITEM
# -------------------------------------------------------
@frappe.whitelist()
def delete_item(model: str):
    try:
        model = validation_item_delete(model)
        frappe.delete_doc("Item", model)
        frappe.db.commit()

    except Exception as e:
        return error(message=str(e))

    return success(message="Item deleted successfully")


# -------------------------------------------------------
# UPDATE ITEM
# -------------------------------------------------------
@frappe.whitelist()
def update_item(**data):
    try:
        model = data.get("model")
        model = validation_item_update(model)

        item = frappe.get_doc("Item", model)

        if "type" in data:
            data["type"] = validation_item_type(data["type"])

        if "price" in data:
            data["price"] = validation_item_price(data["price"])

        item.update(data)
        item.save()
        frappe.db.commit()

    except Exception as e:
        return error(message=str(e))

    return success(
        message="Item updated successfully",
        data=item
    )