import frappe
@frappe.whitelist(allow_guest=True)
def get_item(item_name):
    try:

        item = frappe.get_doc("Item",item_name)
        return{
        "name":item.name1,
        "price":item.price,
        "stock":item.stock_quantity
    }
    except Exception as e:
        frappe.throw(f"Error fetching customer: {e}")
@frappe.whitelist(allow_guest=True)
def create_item(code,name,price):
    doc=frappe.get_doc({
        "doctype":"Item",
        "code":code,
        "name1":name,
        "price":price,

    
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
    return {"message": f"Item {name} created successfully!"}
@frappe.whitelist(allow_guest=True)
def delete_item(name):
    try:
        if name :
            frappe.delete_doc("Item",name,ignore_permissions=True)
            frappe.db.commit()
        else:
              frappe.throw(f"Item '{name}' not found")
    except Exception as e:
          frappe.throw(f" Error deleting customer: {e}")
    return {"message": f"Item {name} delete successfully!"}
@frappe.whitelist(allow_guest= True)
def update_item(name,price):
    try:
        if not frappe.db.exists("Item",name):
            frappe.throw(f"Item {name}' not found")
        doc = frappe.get_doc("Item",name)
        if name:
            doc.name1 =name
        if price:
            doc.price = price
        doc.save(ignore_permissions=True)
        frappe.db.commit()
    except Exception as e :
         frappe.throw(f"Error updating Item: {e}")
    



   

