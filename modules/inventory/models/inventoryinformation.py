from odoo import api, fields, models

class InventoryInformation(models.Model):

	_name = 'inventory.information'
	_description = 'Inventory Management'

	code = fields.Char(string='Warehouse Code')
	name = fields.Char(string='Warehouse Name')
	type = fields.Char(string='Type')
	manager = fields.Char(string='Manager')