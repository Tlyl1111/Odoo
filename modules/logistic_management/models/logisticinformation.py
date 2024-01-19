from odoo import api, fields, models

class LogisticInformation(models.Model):

	_name = 'logistic.information'
	_description = 'Logistic Management'

	code = fields.Char(string='Order Code')
	customer = fields.Char(string='Customer')
	warehouse = fields.Char(string='Warehouse')
	status = fields.Char(string='Order Status')