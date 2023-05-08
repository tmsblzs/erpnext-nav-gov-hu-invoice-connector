I use generateDs to generate python classes from OSA schemas xsds.
Use the following command:
Command line options:
  ('-o', 'online_invoice.py')
  ('-c', 'catalog.xml')
  ('-s', 'invoice_subclass')
  ('--external-encoding', 'utf-8')
  ('--export', 'write etree literal')
  ('--output-directory', 'generatedDS')

Command line arguments:
  onlineInvoice.xsd

Command line:
generateDS -o "online_invoice.py" -c "catalog.xml" -s "invoice_subclass" --external-encoding="utf-8" --export="write etree literal" --output-directory="generatedDS" onlineInvoice.xsd

Then split it to several files. 