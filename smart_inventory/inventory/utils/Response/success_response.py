import frappe

def send(message=None, data=None, status_code=200):
    frappe.response.update({
        "message": {
            "success": True,
            "message": message,
            "data": data,
           
        },
        "status_code": status_code
    })
