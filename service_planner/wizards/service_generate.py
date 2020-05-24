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
        container_list = []
        # reset value to avoid errors
        self.service_container_id = [(5)]
        for container_service in self.service_template_id.service_container_ids:
            container_list.append(container_service.id)

        return {'domain': {'service_container_id': [('id', 'in', container_list)]}}

    def generate_service(self):
        """
        Generate a series of allocate services based on the selected template with
        start date inside the period limits
        """

        service_template = self.service_template_id
        date_pointer = self.date_init
        interval_set = self.interval

        while True:
            interval_set = (interval_set if interval_set > service_template.duration
                            else service_template.duration)

            date_pointer = date_pointer + datetime.timedelta(hours=interval_set)
            if(date_pointer > self.date_stop):
                break

            new_service = {
                "service_template_id"   : self.service_template_id.id,
                "service_container_id"  : self.service_container_id.id,
                "scheduled_start"       : date_pointer,
                }
            self.env['service.allocate'].create(new_service)

            # generate next service if present
            if service_template.next_service_id:
                # calculate end of the original service
                next_strt = (date_pointer +
                             datetime.timedelta(hours=service_template.duration))
                # get next service template
                next_serv = service_template.next_service_id.id
                # get first container of the next service template
                next_cont = service_template.next_service_id.service_container_ids[0].id

                new_service = {
                    "service_template_id"   : next_serv,
                    "service_container_id"  : next_cont,
                    "scheduled_start"       : next_strt,
                    }
                self.env['service.allocate'].create(new_service)
        return
