# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


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
    # container service reference
    service_container_ids = fields.Many2many('service.container',
                                             string='Container service',
                                             required=True)

    # standard duration
    duration = fields.Integer('Duration', required=True, default=1)
    # duration uom
    duration_uom_id = fields.Many2one('uom.uom',
                                      string='Unit of Measure')

    # off-duty services identification to manage rest/maintenance conditions
    off_duty = fields.Boolean('Off Duty', default=False,
                              help='Check if it is a technical '
                                   'service to manage rest/maintenance conditions')

    # expected vehicles
    exp_vehicle_ids = fields.Many2many('expected.vhcl_type',
                                       string='Vehicles')
    # expected skills
    exp_skill_ids = fields.Many2many('expected.skill',
                                     string='Operator Skills')
    # expected equipment category
    exp_eqp_cat_ids = fields.Many2many('expected.eqpmnt_cat',
                                       string='Equipment Category')

    # product reference used to valorize
    product_id = fields.Many2one('product.product',
                                 string='Product reference')

    # identification color
    base_color = fields.Char('Color')

    # Service Template to generate on Service completion
    next_template_id = fields.Many2one(
        'service.template',
        string='Next Service',
        help='Service Template to insert after the end of this one')

    @api.multi
    def write(self, values):
        """
        Add control for fields value on record changes
        """
        if ('duration' in values
                and values['duration'] <= 0):
            raise ValidationError(_('Enter a value for Duration'))

        if ('service_container_ids' in values
                and len(values['service_container_ids'][0][2]) == 0):
            raise ValidationError(_('Set a Container Service'))

        ServiceTemplate_write = super(ServiceTemplate, self).write(values)
        return ServiceTemplate_write

    @api.model
    def create(self, values):
        """
        Add control for fields value on new records
        """
        if ('duration' in values
                and values['duration'] <= 0):
            raise ValidationError(_('Enter a value for Duration'))
        if ('service_container_ids' in values
                and len(values['service_container_ids'][0][2]) == 0):
            raise ValidationError(_('Set a Container Service'))
        ServiceTemplate_create = super(ServiceTemplate, self).create(values)
        return ServiceTemplate_create
