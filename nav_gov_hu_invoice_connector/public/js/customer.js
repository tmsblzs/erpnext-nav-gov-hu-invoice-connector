frappe.ui.form.on('Customer', {
    refresh: function(frm) {

        frm.add_custom_button(__('Check taxpayer'), function(){
            let tax_number = frm.doc.tax_id;

            frappe.call({
              method: "nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.customer.check_taxpayer",
              args:{
                  'tax_number': tax_number
              },
              callback: function(res){
                  show_dialog(res.message);
              }
            })
        }, __("NAV"));
    }
});

function click_yes(tax_number){
    frappe.call({
          method: "nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.api.customer.save_taxpayer",
          args:{
              'tax_number': tax_number
          },
          freeze: true,
          callback: function(res){
              let customer_id = res.message;
              let url = window.location.href.split("/")
              window.location.replace(`${url[0]}//${url[2]}/app/customer/${customer_id}`)
          }
    })
}

function show_dialog(json_str){
    let data = JSON.parse(json_str);
    let d = create_dialog();
    d.set_values(data)
        .then(r => d.show());
}

function create_dialog(){
    let d = new frappe.ui.Dialog({
          title: __("Are you sure to save this customer with these data?"),
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
              }, {
                  label: __('HQ Address'),
                  fieldname: 'hq_address',
                  fieldtype: 'Data',
                  read_only: true
              }
          ],
          primary_action_label: 'Yes',
          secondary_action_label: 'No',
          primary_action(values){
              click_yes(values.tax_number)
              d.hide();
          },
          secondary_action(values){
              d.hide();
          }
    });
    return d;
}
