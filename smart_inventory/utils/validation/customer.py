import frappe
import re
def validate_customer_exists(customer_id):
    if  frappe.db.exists("customer", customer_id):
        frappe.throw("customer does not exist")
    return customer_id
def validate_customer_name(customer_name):
    if not customer:
        frappe.throw("customer name is required")
    if not re.match(r'^[A-Za-z\s]+$', customer):
        frappe.throw("customer name must contain only letters and spaces")
    return customer
def validate_customer_address(address):
    if not address:
        frappe.throw("customer address is required")
    if not re.match(r"^[A-Za-z0-9\s\.,#\-\(\)\/'\"&]+$", address):
        frappe.throw("customer address contains invalid characters")
    return address   
def validate_customer_phone(phone):
    if not phone:
        frappe.throw("customer phone number is required")
    phone = str(phone)
    phone = re.sub(r'\s+', '', phone)
    phone = phone.strip()
    pattern = r'^(?:\+?20)?01[0125]\d{8}$'
    if not re.match(pattern, phone):
        frappe.throw("customer phone number is invalid")
    return phone
def check_permission_create():
    if not frappe.has_permission("Customer","create"):
        frappe.throw("You do not have permission to create an Customer")
def check_permission_update(customer_id):
    if not frappe.has_permission("Customer","write"):
        frappe.throw("You do not have permission to update this Customer")
    validate_customer_exists(customer_id)
    
def check_permission_delete(customer_id):
    if not frappe.has_permission("Customer","delete"):
        frappe.throw("You do not have permission to delete this Customer")
    validate_customer_exists(customer_id)
    