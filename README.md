THIS APP IS UNDER DEVELOPMENT!!!

## Nav Gov Hu Invoice Connector

It is connecto to online invoice system of hungarion tax authority.

#### License

MIT

## Leírás:
    - nincs batch számla feldolgozás
    - nincs tömörített számla feldolgozás

## Frappe/ErpNext:
- BDD test futattása ki kellett egészíŧeni a frappe/frappe/commands/utils.py:

        @click.command('run-bdd-tests')
        @click.option('--app', help="For App", default='frappe')
        @click.option('--feature', help="Run only the selected feature file")
        @pass_context
        def run_bdd_tests(context, app, feature=None):
            "Run BDD tests"
            site = get_site(context)
            app_base_path = os.path.abspath(os.path.join(frappe.get_app_path(app), '..'))
            frappe.init(site=site)
            os.chdir(app_base_path)
        
            formatted_command = 'behave '
        
            if feature:
                formatted_command += f' -i {feature} '
        
            click.secho("Running Behave...", fg="yellow")
            frappe.commands.popen(formatted_command, cwd=app_base_path, raise_err=True)
    

- majd PyCharm-ba új virtual environmentet kellett felvenni a következő beállításokkal:
    - script path: '/home/frappe/frappe-bench/apps/frappe/frappe/utils/bench_helper.py'
    - parameters: 'frappe --site erp.dev.pensav.hu run-bdd-tests --app nav_gov_hu_invoice_connector'
    - projects: 'frappe'
  
Known Issues:
  Nav Gov Hu User:
    - nagyon érzékeny a első és utolsó szóközökre
    - ha egyszer el lett mentve a user törölni kell és újat lérehozni
    - a password mentés módosításkor nem jó
    - cache-t kell üríteni user módosítás után
  Nav Gov Hu Settings:
    - default user beállítás után cache ürítés kell (néha bench újraindítás)

## INSTALLATION
sudo bench get-app https://github.com/tmsblzs/erpnext-nav-gov-hu-invoice-connector.git --branch develop

sudo bench --site [site] install-app [app-name] 

## SETUP
### NAVGOVHUUSERLIST
    - add new user
### NAVGOVHUUSER
    - set login, password, xml signing signature, exchange key
### NAVGOVHUSETTINGS
    - api url:
      for test: https://api-test.onlineszamla.nav.gov.hu
      for production: https://api.onliszamla.nav.gov.hu
    - version:
        type 'v3'
    - default user:
        select navgovhuuser
