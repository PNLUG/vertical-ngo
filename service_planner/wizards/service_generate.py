# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api
import datetime


class ServiceGenerateWizard(models.TransientModel):
    _name = 'service.generate'
    _description = 'Generate a list of services'

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

    # scheduled start time
    date_init = fields.Datetime('Start date', required=True)
    # scheduled start time
    date_stop = fields.Datetime('Stop date', required=True)
    # standard duration
    interval = fields.Integer('Interval', required=True, default=8)

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

    def generate_service(self):
        """
        _todo_
        """

        serv_tmplt = self.service_template_id
        date_pointer = self.date_init
        interval_set = self.interval

        while True:
            interval_set = (interval_set if interval_set > serv_tmplt.duration
                            else serv_tmplt.duration)

            date_pointer = date_pointer + datetime.timedelta(hours=interval_set)
            if(date_pointer > self.date_stop):
                break

            new_service = {
                "service_template_id"   : self.service_template_id.id,
                "service_container_id"     : self.service_container_id.id,
                "start_sched"            : date_pointer,
                }
            self.env['service.allocate'].create(new_service)

        return
