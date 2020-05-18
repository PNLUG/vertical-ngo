# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FleetVehicle(models.Model):
    """
    Add Partner reference to Employee
    """

    _inherit = 'hr.employee'

    # Partner reference
    partner_id = fields.Many2one('res.partner',
                                 'Reference Partner',
                                 help='Partner\'s Employee that works for the company')
