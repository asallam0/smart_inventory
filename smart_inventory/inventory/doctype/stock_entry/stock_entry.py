# Copyright (c) 2025, Adminstrtor and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StockEntry(Document):
    def before_save(self):
        for item in self.items:
            item_doc = frappe.get_doc("Item", item.item)

            if self.entry_type == "Stock In":
                item_doc.stock_quantity += item.quantity
            elif self.entry_type == "Stock Out":
                item_doc.stock_quantity -= item.quantity

            item_doc.save()
