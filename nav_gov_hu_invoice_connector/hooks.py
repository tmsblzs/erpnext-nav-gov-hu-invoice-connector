from . import __version__ as app_version

app_name = "nav_gov_hu_invoice_connector"
app_title = "Nav Gov Hu Invoice Connector"
app_publisher = "tmsblzs"
app_description = "This apps helps to connect to online invoice system of hungarian tax authority."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "tmsblzs+github@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nav_gov_hu_invoice_connector/css/nav_gov_hu_invoice_connector.css"
# app_include_js = "/assets/nav_gov_hu_invoice_connector/js/nav_gov_hu_invoice_connector.js"

# include js, css files in header of web template
# web_include_css = "/assets/nav_gov_hu_invoice_connector/css/nav_gov_hu_invoice_connector.css"
# web_include_js = "/assets/nav_gov_hu_invoice_connector/js/nav_gov_hu_invoice_connector.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "nav_gov_hu_invoice_connector/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js = {
		"Customer": "public/js/customer.js",
		"Purchase Invoice": "public/js/invoice.js"
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nav_gov_hu_invoice_connector.install.before_install"
# after_install = "nav_gov_hu_invoice_connector.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "nav_gov_hu_invoice_connector.uninstall.before_uninstall"
# after_uninstall = "nav_gov_hu_invoice_connector.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nav_gov_hu_invoice_connector.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	# "Sales Invoice": {
	# 	"on_update": "nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.hook.sales_invoice.on_update"
	# }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nav_gov_hu_invoice_connector.tasks.all"
# 	],
# 	"daily": [
# 		"nav_gov_hu_invoice_connector.tasks.daily"
# 	],
# 	"hourly": [
# 		"nav_gov_hu_invoice_connector.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nav_gov_hu_invoice_connector.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nav_gov_hu_invoice_connector.tasks.monthly"
# 	]
# }

scheduler_events = {
	# "all": [
	# 		"nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.hook.scheduler_tasks.every_five_minutes"
	# 	]
	#
	# "cron": {
	# 	"*/5 * * * *": [
	# 		"nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.hook.scheduler_tasks.every_five_minutes"
	# 	]
	# }
}

# Testing
# -------

# before_tests = "nav_gov_hu_invoice_connector.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nav_gov_hu_invoice_connector.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nav_gov_hu_invoice_connector.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"nav_gov_hu_invoice_connector.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
