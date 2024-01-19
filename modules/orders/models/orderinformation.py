from odoo import models, fields
import math
class OrderInformation(models.Model):
    _name = 'order.information'
    _description = 'Order Information'


    #organization_id = fields.Many2one('res.partner', string='Organization', required=True)
    od_code = fields.Char(string='Order Code', required=True)
    cus = fields.Many2one(
        'customer.information', string='Customer',
        help="Link"
    )
    place = fields.Char(string='Place', required=True)
    longitude = fields.Float(string='Longitude', required=True)
    latitude = fields.Float(string='Latitude', required=True)
    height = fields.Float(string='Height', required=True)
    weight = fields.Float(string='Weight', required=True)
    storage_time = fields.Float(String='Storage Time', required=True)
    order = fields.Date(String='Order Date', required=True)
    pick_up = fields.Date(String='Pick-up Date', required=True)
    delivery = fields.Date(String='Delivery Date', required=True)
    status = fields.Char(string='Status', required=True)





    def name_get(self):
        result = []
        for rec in self:
            # Customize the name here as you want it to appear
            name = '%s' % (rec.od_code)
            result.append((rec.id, name))
        return result

    # Thêm các trường và logic bổ sung nếu cần

    suggested_shelf_ids = fields.Many2many(
        'shelves.information',
        string='Suggested Shelves',
        compute='_compute_suggested_shelves'
    )

    suggested_warehouse_ids = fields.Many2many(
        'warehouse.information',
        string='Suggested Warehouses',
        compute='_compute_suggested_warehouses'
    )


    def _compute_suggested_shelves(self):
        for order in self:
            matching_shelves = self.env['shelves.information'].search([
                ('status', '=', 'empty'),
                ('height', '=', order.height),
                ('weight', '=', order.weight),
            ])
            order.suggested_shelf_ids = matching_shelves


    def _compute_suggested_warehouses(self):
        for order in self:
            warehouses = order.suggested_shelf_ids.mapped('wh_id')
            order.suggested_warehouse_ids = warehouses

    def create(self, vals):
        # When creating a new order, also calculate the routes
        order = super(OrderInformation, self).create(vals)
        order.calculate_routes()
        return order

    def calculate_routes(self):
        self.ensure_one()
        warehouse_model = self.env['warehouse.information']
        # Get all warehouses that are depots
        depots = warehouse_model.search([('wh_type', '=', 'depot')])
        for depot in depots:
            # Calculate the distance using the Haversine formula
            distance = self.haversine(self.latitude, self.longitude, depot.latitude, depot.longitude)
            # Here you can save the distance to a field or do something else with it

    def haversine(self, lat1, lon1, lat2, lon2):
        R = 6371  # radius of the Earth in kilometers
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lon = math.radians(lon2 - lon1)
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c  # in kilometers
        return distance