# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ServiceCollector(models.Model):
    """
    Collector of service templates to calculate final values
    eg. amount of hours worked, number of rest shift in a month
    """

    # model
    _name = 'service.collector'
    _description = 'Collector of service templates'

    # fields
    # name
    name = fields.Char('Name')
    # description
    description = fields.Char('Description')
    # service template to collect
    service_template_ids = fields.Many2many('service.template',
                                            string='Collected Services')
