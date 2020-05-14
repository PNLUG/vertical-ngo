# Copyright 2019 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name":     "Vertical NGO - Service Plan",
    "summary":  "Management of service planning.",
    "version":  "12.0.1.0.0",

    "author":   "Associazione PNLUG - Gruppo Odoo, Odoo Community Association (OCA)",
    "website":  "https://gitlab.com/PNLUG/",
    "license":  "AGPL-3",

    "category": "Logistics",

    "depends": [
        'fleet',
        'maintenance',
        'hr',
        'product',
        'web_timeline',
        'web_widget_color',
        ],
    "data": [
        'security/ir.model.access.csv',
        'wizards/service_generate.xml',
        'views/service_menu.xml',
        'views/service_view.xml',
        ],
    "css": [
        'static/src/css/service_planner.css',
        ],
    'installable': True,
}
