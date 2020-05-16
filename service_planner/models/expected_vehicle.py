# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ExpectedVehicle(models.Model):
    """
    Vehicle element expected on a service
    """

    # model
    _name = 'expected.vhcl_type'
    _description = 'Service expected vehicle'

    # fields
    # minimum quantity
    min_qty = fields.Integer('Minimum quantity', required=True, default=1)
    # maximum quantity: 0 for no limit
    max_qty = fields.Integer('Maximum quantity', help="Value 0 means no limit")
    # vehicle
    vehicle_type_id = fields.Many2one('vehicle.type', string='Vehicle Type')

    # define record name to display in form view
    _rec_name = 'vehicle_type_id'
