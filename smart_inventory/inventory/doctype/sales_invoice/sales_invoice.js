// Copyright (c) 2025, Adminstrtor and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sales Invoice", {
	quantity:function(frm){
        grand_total(frm);
    },
    discount:function(frm){
        clac_discount(frm);
    }
});
function grand_total(frm){
   let qty= frm.doc.quantity
   let price = frm.doc.price
     frm.set_value('grand_total', qty * price);
}
function clac_discount(frm){
    let discount = frm.doc.discount || 0;
    let total = frm.doc.grand_total;
    let amount_after_discount=total - (total * discount/100)
    frm.set_value("amount_after_discount", (amount_after_discount))
}
