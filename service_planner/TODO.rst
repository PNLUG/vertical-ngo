ToDo list


**Model**
    * expected_*
        * FIX filter view only to associated record
    * service allocate
        * DEV check template expected fulfillment
    * service template
        * DEV configuration of next service
        * DEV limit to 1 Container Service for off_duty type service


**View**
    * service template form
        * FIX custom css loading
        * FIX filter view of expected_* only to associated
        * FIX eliminate self.id from next list
    * service allocate calendar
        * FIX employee name display (newline separated)
        * DEV text format
        * DEV lock action on empty cells
        * FIX element dedicatd color (web_calendar)
    * service allocate timeline
        * DEV try add another level of group (ie. locality)
        * DEV check use
        * FIX show computed field (employee_names)
        * FIX element dedicated color (web_timeline)
    * service allocate tree
        * FIX service color string
    * service rule
        * DEV add profile reference to employee, equipment, vehicle
        * DEV complete rule method

**Security**
    * fix model authorizations

**Readme**
oca-gen-addon-readme --repo-name vertical-ngo --branch 12.0 --addon-dir ~/odoo-dev/odoo12/OCA/addons-custom-sp/service_planner/
