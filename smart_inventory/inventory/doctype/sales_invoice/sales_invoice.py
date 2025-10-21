# Copyright (c) 2025, Adminstrtor and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SalesInvoice(Document):
    def before_save(self):
        quantity = self.quantity
        price = self.price
        self.grand_total = quantity * price
        
    def on_submit(self):
        if self.workflow_state == "Approved":
            item = self.item
            doc = frappe.get_doc("Item",item)
            doc.stock_quantity -= self.quantity
            doc.save()

	
