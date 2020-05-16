# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class VehicleType(models.Model):
    """
    A classification of vehicle based on functionality
    eg. tow truck, ambulance, trailer, boat
    """

    _name = 'vehicle.type'
    _description = 'Classification of vehicle, eg. tow truck, ambulance, trailer, boat'

    # fields
    # name
    name = fields.Char('Type', help='Eg. tow truck, ambulance, trailer, boat')


class FleetVehicle(models.Model):
    """
    Add field for type management to vehicle
    """

    _inherit = 'fleet.vehicle'

    # type of vehicle
    vehicle_type_id = fields.Many2one('vehicle.type',
                                      'Vehicle Type',
                                      help='Eg. tow truck, ambulance, trailer, boat')
