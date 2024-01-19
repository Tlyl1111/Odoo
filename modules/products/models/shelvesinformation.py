from odoo import models, fields

class ShelvesInformation(models.Model):
    _name = 'shelves.information'
    _description = 'Shelves Information'

    shelve_code = fields.Char(string='Shelves Code', required=True)
    wh_id = fields.Many2one(
        'warehouse.information', string='Warehouse',
        help="Link"
    )

    weight = fields.Selection([
        ('w1000', '1000'),
        ('w1200', '1200'),
        ('w1500', '1500'),
    ], string='Weight', required=True)

    height = fields.Selection([
        ('h4', '4'),
        ('h6', '6'),
        ('h8', '8'),
        ('h10', '10'),
    ], string='Height', required=True)

    status = fields.Selection([
        ('empty', 'Empty'),
        ('full', 'Full'),
    ], string='Status')

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def name_get(self):
        result = []
        for rec in self:
            # Customize the name here as you want it to appear
            name = '%s' % (rec.shelve_code)
            result.append((rec.id, name))
        return result

    def _onchange_status(self):
        if self.status == 'full':
            return {
                'required': {'start_date', 'end_date'},
            }
        return {}