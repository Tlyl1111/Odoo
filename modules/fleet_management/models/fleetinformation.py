from odoo import api, fields, models

class FleetInformation(models.Model):

	_name = 'fleet.information'
	_description = 'Fleet Management'

	code = fields.Char(string='Vehicle Code')
	name = fields.Char(string='Vehicle Name')
	type = fields.Char(string='Type')
	license = fields.Char(string='License Plate')
	driver = fields.Char(string='Default Driver')
	driver_name = fields.Char(string='Default Driver Name')
	zone = fields.Integer(string='Zones')
	active = fields.Binary(string='Active')