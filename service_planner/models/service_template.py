# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ServiceTemplate(models.Model):
    """
    Model of a service with definition of the required components
    """

    # model
    _name = 'service.template'
    _description = 'Model of a service'

    # fields
    # name
    name = fields.Char('Name', required=True)
    # global service reference
    service_global_ids = fields.Many2many('service.global', string='Global service')

    # standard duration
    duration = fields.Integer('Duration', required=True, default=1)
    # duration uom
    duration_uom_id = fields.Many2one('uom.uom', string='Unit of Measure')

    # expected vehicles
    exp_vehicle_ids = fields.Many2many('expected.vehicle', string='Vehicles')
    # expected jobs
    exp_job_ids = fields.Many2many('expected.job', string='Jobs')
    # expected equipment
    exp_equipment_ids = fields.Many2many('expected.equipment', string='Equipment')

    # product reference used to valorize
    product_id = fields.Many2one('product.product', string='Product reference')

    # identification color
    base_color = fields.Char('Color')

    def generate_service(self):
        """
        _todo_
        """
        self.env['service.allocate'].generate_service(
            self.id,
            self.service_global_ids[0].id,
            '2020-05-15 08:00:00',
            '2020-05-20 23:59:59',
            8
            )
        return
