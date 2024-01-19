from odoo import models, fields

class VehicleType(models.Model):
    _name = 'vehicle.type'
    _description = 'Vehicle Type'
    _order = 'type_name'

    #organization_id = fields.Many2one('res.partner', string='Organization', required=True)
    type_code = fields.Char(string='Type Code', required=True)
    type_name = fields.Char(string='Type Name', required=True)
    palletized_time = fields.Integer(string='Palletized Time (minute)', required=True)
    non_palletized_time = fields.Integer(string='Non-Palletized Time (minutes)', required=True)

    def name_get(self):
        result = []
        for rec in self:
            # Customize the name here as you want it to appear
            name = '%s' % (rec.type_name)
            result.append((rec.id, name))
        return result

    # Thêm các trường và logic bổ sung nếu cần
