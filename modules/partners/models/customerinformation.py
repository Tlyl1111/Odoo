from odoo import models, fields

class CustomerInformation(models.Model):
    _name = 'customer.information'
    _description = 'Customer Information'

    cus_code = fields.Char(string='Customer Code', required=True)
    cus_name = fields.Char(string='Customer Name', required=True)
    cus_address = fields.Char(string='Customer Address', required=True)
    cus_phone = fields.Char(string='Customer Phone', required=True)
    cus_email = fields.Char(string='Customer Email', required=True)

    def name_get(self):
        result = []
        for rec in self:
            # Customize the name here as you want it to appear
            name = '%s' % (rec.cus_name)
            result.append((rec.id, name))
        return result