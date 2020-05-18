# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api
import datetime


class ServiceAllocate(models.Model):
    """
    Allocated service with definition of all the template components
    """

    # model
    _name = 'service.allocate'
    _description = 'Allocate service'

    # fields
    # template service reference
    service_template_id = fields.Many2one('service.template',
                                          string='Template service',
                                          required=True,
                                          )
    # container service reference
    service_container_id = fields.Many2one('service.container',
                                           string='Container service',
                                           required=True,
                                           )
    # dedicated color
    service_color = fields.Char('Color',
                                related='service_template_id.base_color')

    # assigned vehicles
    vehicle_ids = fields.Many2many('fleet.vehicle', string='Vehicles')
    # assigned employee
    employee_ids = fields.Many2many('hr.employee', string='Team')
    # employee names
    employee_names = fields.Char('Employees', compute='_compute_emply_name', store=True)
    # assigned equipment
    equipment_ids = fields.Many2many('maintenance.equipment', string='Equipment')

    # locality reference
    locality = fields.Char('Locality')

    # scheduled start time
    start_sched = fields.Datetime('Start scheduled', required=True)
    # scheduled start time
    stop_sched = fields.Datetime('Stop scheduled',
                                 compute='_compute_stop_sched', store=True)
    # effective start time
    start_real = fields.Datetime('Start real')
    # effective stop time
    stop_real = fields.Datetime('Stop real')

    # state of the service
    state = fields.Selection([('planned', 'Planned'),
                              ('confirmed', 'Confirmed'),
                              ('closed', 'Closed')
                              ],
                             string='State', required=True, default='planned')

    @api.depends('start_sched')
    def _compute_stop_sched(self):
        for service in self:
            if service.start_sched:
                slot = service.service_template_id.duration
                # avoid empty value of duration
                slot = slot if slot > 0 else 1
                service.stop_sched = (service.start_sched +
                                      datetime.timedelta(hours=slot))

        return

    @api.depends('employee_ids')
    def _compute_emply_name(self):
        for service in self:
            service.employee_names = ''
            for employee in service.employee_ids:
                service.employee_names = service.employee_names + ' ' + \
                    employee.name
        return

    # utility to filter container services to template's container services
    @api.onchange('service_template_id')
    def _get_template_container(self):
        """
        Extract list of container services associated to the template service
        """
        container_services = []
        # reset value to avoid errors
        self.service_container_id = [(5)]
        for glob_srv in self.service_template_id.service_container_ids:
            container_services.append(glob_srv.id)

        return {'domain': {'service_container_id': [('id', 'in', container_services)]}}
