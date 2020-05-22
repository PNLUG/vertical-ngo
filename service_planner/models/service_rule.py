# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ServiceRule(models.Model):
    """
    Definition of the rules available as specific method.
    This model if filled through xls data file.
    """

    # model
    _name = 'service.rule'
    _description = 'Rule to manage services'

    # fields
    # method of the rule
    method = fields.Char('Method')
    # rule description
    description = fields.Char('Description')
    # method fields
    field_ids = fields.Many2many('service.rulefield', string='Field')

    # define record name to display in form view
    _rec_name = 'description'

    def double_assign(self, resource, obj_id):
        """
        Check if a resource has more than one shift assigned at same time
        @param  resource    string: [employee, vehicle, equipment] type of the resource
        @param  obj_id      int:    id of the object
        """
        # _TODO_
        return True

    def rule_call(self, rule):
        """
        Call requested rule
        @param  rule    obj: form select element with name of the rule to call:
                             has to be in rule_id selection
        @return    rule elaboration
        """

        # _TODO_ check if in rule_id
        rule_name = rule['rule_name']
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, rule_name, lambda: "Invalid rule")
        # Call the method as we return it

        result = method()
        return result

    def _rule_method_template(self):
        """
        Rules definition template
        @param  _todo_
        @return _todo_
        """
        return 0

    def hour_active_week(self):
        """
        Calculate the total of active hours of a resource in a week.
        By active hours is meant work+on call
        _todo_ define/set active shift
        """
        return 42

    def hour_rest_week(self):
        """
        Calculate the total of rest hours of a resource in a week.
        By active hours is meant not work or on call
        _todo_ define/set active shift
        """
        return 8
