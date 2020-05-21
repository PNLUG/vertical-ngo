# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ServiceRuleClass(models.Model):
    """
    Collection of rules to assign to a resource
    """

    # model
    _name = 'service.ruleclass'
    _description = 'Class to group rules'

    # fields
    # name
    name = fields.Char('Name', required=True)
    # service template to collect
    rule_ids = fields.Many2many('service.rule', string='Rule')
