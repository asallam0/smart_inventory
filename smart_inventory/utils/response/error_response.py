import frappe

def send(message=None, data=None,status_code=500):
    frappe.response.update({
        "message": {
            "success": False,
            "error": message,
            "data": data,
           
        },
        "status_code": status_code
    })
