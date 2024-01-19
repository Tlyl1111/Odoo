from odoo import models, fields

class MyModel1(models.Model):
    _name = 'my.module.model1'
    _description = 'My Model1'

    name = fields.Char('Name')
    type = fields.Char('Type')
