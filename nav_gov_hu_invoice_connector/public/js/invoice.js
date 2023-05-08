frappe.ui.form.on('Purchase Invoice', {
    refresh: function(frm) {

        frm.add_custom_button(__('Check purchase invoices'), function(){
            frappe.call({
              method: "nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.invoice.check_invoices",
              // callback: function(res){
              //     show_dialog(res.message);
              // }
            })
        }, __("NAV"));
    }
});
