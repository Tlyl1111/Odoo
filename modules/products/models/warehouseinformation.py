from odoo import models, fields

class WarehouseInformation(models.Model):
    _name = 'warehouse.information'
    _description = 'Warehouse Information'
    _order = 'wh_name'

    #organization_id = fields.Many2one('res.partner', string='Organization', required=True)
    wh_code = fields.Char(string='Warehouse Code', required=True)
    wh_name = fields.Char(string='Warehouse Name', required=True)

    wh_type = fields.Selection([
        ('depot', 'Depot'),
        ('transit', 'Transit'),
    ], string='Warehouse Type', required=True)

    wh_address = fields.Char(string='Address', required=True)
    longitude = fields.Char(string='Longitude', required=True)
    latitude = fields.Char(string='Latitude', required=True)



    def name_get(self):
        result = []
        for rec in self:
            # Customize the name here as you want it to appear
            name = '%s' % (rec.wh_name)
            result.append((rec.id, name))
        return result

    # Thêm các trường và logic bổ sung nếu cần
