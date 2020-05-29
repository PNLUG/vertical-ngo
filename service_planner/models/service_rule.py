# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, _
from odoo.exceptions import UserError


class ServiceRule(models.Model):
    """
    Definition of the rules available as specific method.
    This model if filled through xls data file.
    """

    # model
    _name = 'service.rule'
    _description = 'Rules to manage Services'

    # fields
    # method of the rule
    method = fields.Char('Method')
    # rule description
    description = fields.Char('Description')
    # method's fields
    field_ids = fields.Many2many('service.rulefield', string='Fields')
    # define if rule is used
    is_active = fields.Boolean('Active', default=True,
                               help='Set if the rule had to be evaluated')

    # define record name to display in form view
    _rec_name = 'description'

    def double_assign(self, resource_type, obj_id):
        """
        Check if a resource has more than one shift assigned at same time
        @param  resource_type    string: type of the resource
                                        [all, employee, vehicle, equipment]
        @param  obj_id          int:    id of the service; -1 to check all services
        """
        # _TODO_ optimize

        rule_result = True
        rule_msg = ''

        # select service to check
        if obj_id > 0:
            allocate_ids = self.env['service.allocate'].search([('id', '=', obj_id)])
        else:
            allocate_ids = self.env['service.allocate'].search([])

        # get the service data
        for service in allocate_ids:
            date_ini = service.scheduled_start
            date_fin = service.scheduled_stop

            if resource_type in ('employee', 'all') :
                for employee in service.employee_ids:
                    all_services = self.env['service.allocate'] \
                                       .search([('id', '!=', service.id),
                                                ('scheduled_start', '<', date_fin),
                                                ('scheduled_stop', '>', date_ini),
                                                ('state', '!=', 'closed')
                                                ])
                    for service_double in all_services:
                        if employee in service_double.employee_ids:
                            rule_result = False
                            rule_msg += (('Shift %s/%s: %s\n') % (service.id,
                                                                  service_double.id,
                                                                  employee.name))

            if resource_type in ('equipment', 'all'):
                for equipment in service.equipment_ids:
                    all_services = self.env['service.allocate'] \
                                       .search([('id', '!=', service.id),
                                                ('scheduled_start', '<', date_fin),
                                                ('scheduled_stop', '>', date_ini),
                                                ('state', '!=', 'closed')
                                                ])
                    for service_double in all_services:
                        if equipment in service_double.equipment_ids:
                            rule_result = False
                            rule_msg += (('Shift %s/%s: %s\n') % (service.id,
                                                                  service_double.id,
                                                                  equipment.name))

            if resource_type in ('vehicle', 'all'):
                for vehicle in service.vehicle_ids:
                    all_services = self.env['service.allocate'] \
                                       .search([('id', '!=', service.id),
                                                ('scheduled_start', '<', date_fin),
                                                ('scheduled_stop', '>', date_ini),
                                                ('state', '!=', 'closed')
                                                ])
                    for service_double in all_services:
                        if vehicle in service_double.vehicle_ids:
                            rule_result = False
                            rule_msg += (('Shift %s/%s: %s\n') % (service.id,
                                                                  service_double.id,
                                                                  vehicle.name))

        if not rule_result:
            raise UserError(_('Elements with overlapped shift:')+'\n'+rule_msg)
        return rule_result

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
