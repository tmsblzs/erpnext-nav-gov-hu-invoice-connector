frappe.ui.form.on('Customer', {
    refresh: function(frm) {

        frm.add_custom_button(__('Check taxpayer'), function(){
            let tax_number = frm.doc.tax_id;

            frappe.call({
              method: "nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.events.click_check_taxpayer",
              args:{
                  'tax_number': tax_number
              },
              callback: function(res){
                    let data = JSON.parse(res.message)
                    let d = new frappe.ui.Dialog({
                          title: __("Are you sure to save tha customer with these data?"),
                          fields:[
                              {
                                  label: __('Name'),
                                  fieldname: 'name',
                                  fieldtype: 'Data',
                                  read_only: true,
                              }, {
                                  label: __('Short Name'),
                                  fieldname: 'short_name',
                                  fieldtype: 'Data',
                                  read_only: true,
                              }, {
                                  label: __('Tax Number'),
                                  fieldname: 'tax_number',
                                  fieldtype: 'Data',
                                  read_only: true,
                              }, {
                                  label: __('Type'),
                                  fieldname: 'incorporation',
                                  fieldtype: 'Data',
                                  read_only: true,
                              }
                          ],
                          primary_action_label: 'Yes',
                          secondary_action_label: 'No',
                          primary_action(values){
                              console.log('Yes');
                              d.hide();
                          },
                          secondary_action(values){
                              console.log('No')
                              d.hide();
                          }
                      });
                    d.set_values(data);
                    d.show();
                  }
            })
        }, __("NAV"));
    }
});