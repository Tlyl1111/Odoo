from odoo import fields, models

class DemoCusInformation(models.Model):

	_name = 'democus.information'
	_description = 'Cus Management'

	code = fields.Char(string='Cus Code')
	name = fields.Char(string='Customer')