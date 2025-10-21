import frappe 
import csv
def execute():
    file_path=frappe.get_site_path("private", "files", "products-100.csv")
    with open(file_path,mode="r", encoding="utf-8")as f:
        reader_product=csv.DictReader(f)
        for row in reader_product:
            name=row.get("Name")
            price=row.get("Price")
            if frappe.db.exists("Products",name):
                doc=frappe.get_doc("Products",name)
                doc.price=price
                doc.save()
                

