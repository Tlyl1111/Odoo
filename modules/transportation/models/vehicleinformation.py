from odoo import models, fields, api

class VehicleInformation(models.Model):
    _name = 'vehicle.information'
    _description = 'Vehicle Information'
    _order = 'vehicle_name'
    #organization_id = fields.Many2one('res.partner', string='Organization', required=True)
    license_plate = fields.Char(string='License Plate', required=True)
    #vehicle_type = fields.Selection([
    #    ('car', 'Car'),
    #    ('truck', 'Truck'),
        # Thêm các loại xe khác tùy vào nhu cầu
    #], string='Vehicle Type')
    vehicle_type_id = fields.Many2one(
        'vehicle.type', string='Vehicle Type',
        help="Link to the type of the vehicle based on the vehicle type name"
    )


    vehicle_name = fields.Char(string='Vehicle Name')
    vehicle_code = fields.Char(string='Vehicle Code', required=True)
    temperature_type = fields.Selection([
        ('ambient', 'Ambient'),
        ('chilled', 'Chilled'),
        ('frozen', 'Frozen'),
    ], string='Temperature Type')
    temp_zone = fields.Float(string='Temp Zone')
    volume = fields.Float(string='Volume (m³)', required=True)
    weight = fields.Float(string='Weight (kg)', required=True)
    start_time = fields.Float(string='Start Time (HH:mm)')
    stop_time = fields.Float(string='Stop Time (HH:mm)')
    lunch_start_time = fields.Float(string='Lunch Start Time (HH:mm)')
    lunch_stop_time = fields.Float(string='Lunch Stop Time (HH:mm)')
    mdp = fields.Char(string='MDP')
    cargo_area_length = fields.Float(string='Cargo Area Length (m)')
    cargo_area_width = fields.Float(string='Cargo Area Width (m)')
    cargo_area_height = fields.Float(string='Cargo Area Height (m)')
    speed = fields.Float(string='Speed', required=True)
    gross_weight = fields.Float(string='Gross Weight')
    real_weight = fields.Float(string='Real Weight')
    registration_date = fields.Date(string='Registration Date')
    rental_cost = fields.Float(string='Rental Cost')
    fixed_cost = fields.Float(string='Fixed Cost')
    cost_per_km = fields.Float(string='Cost per km')
    maximum_single_order_weight = fields.Float(string='Maximum Single Order Weight (kg)')
    maximum_single_order_volume = fields.Float(string='Maximum Single Order Volume (m³)')
    #default_driver_id = fields.Many2one('res.users', string='Default Driver')
    active = fields.Boolean(string='Active')
    sub_contractor = fields.Boolean(string='Sub-contractor')

    def name_get(self):
        result = []
        for rec in self:
            # Customize the name here as you want it to appear
            name = '%s' % (rec.vehicle_name)
            result.append((rec.id, name))
        return result

    # Thêm các trường khác nếu cần