from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Banking and Payments"),
			"items": [
				{
					"type": "doctype",
					"label": _("Auto Update Bank Transaction Dates"),
					"name": "Bank Statement",
					"description": _("Auto Update bank payment dates with journals.")
				},
			]
		},
	]
