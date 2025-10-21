import frappe

def execute():
    
    customers = frappe.get_all("Customer", filters={"address": ["in", ["", None]]}, fields=["name"])

    for c in customers:
        frappe.db.set_value("Customer", c.name, "address", "Unknown")

    frappe.db.commit()
    
