import frappe 
from smart_inventory.utils.validation.customer import(
    validate_customer_exists,
    validate_customer_name,
    validate_customer_address,
    validate_customer_phone,
    check_permission_create,
    check_permission_update,
    check_permission_delete
)
from smart_inventory.utils.response.success_response import send as success
from smart_inventory.utils.response.error_response import send as error
@frappe.whitelist(allow_guest=True)
def get_customer(customer_id:str):
    """Fetch a single customer by customer_id"""
    if not customer_id:
       frappe.throw("Customer ID is required")
    try:
         customer_id=validate_customer_exists(customer_id)
         customer = frappe.get_doc("Customer", customer_id)
    except Exception as e:
        return error(message=f"customer not found: {str(e)}")
    return success(
        message="customer fetched successfully",
        data=customer.as_dict()
    )
@frappe.whitelist()
def create_customer(**data):
    """Create New Customer"""
    try:
        check_permission_create()
        data["customer_name"]=validate_customer_name(data.get("customer_name"))
        data["address"]=validate_customer_address(data.get("address"))
        data["phone"]=validate_customer_phone(data.get("phone"))
        customer=frappe.new_doc("Customer")
        customer.update(data)
        customer.insert()
        frappe.db.commit()
    except Exception as e:
        return error(message=str(e))
    return success(
        message="Coustomer Create successfully"
    )
@frappe.whitelist()
def update_customer(customer_id:str, **data):
    """Update Existing Customer"""
    try:
        check_permission_update(customer_id)
        data["customer_name"]=validate_customer_name(data.get("customer_name"))
        data["address"]=validate_customer_address(data.get("address"))
        data["phone"]=validate_customer_phone(data.get("phone"))
        customer=frappe.get_doc("Customer", customer_id)
        customer.update(data)
        customer.save()
        frappe.db.commit()
    except Exception as e:
        return error(message=(str(e)))
    return success(
        message="Customer updated successfully",
        data=customer
    )
@frappe.whitelist()
def delete_customer(customer_id:str):
    """Delete Existing Customer"""
    try:
        check_permission_delete(customer_id)
        frappe.delete_doc("Customer", customer_id)
        frappe.db.commit()
    except Exception as e:
        return error(message=(str(e)))
    return success(
        message="Customer deleted successfully"
    )