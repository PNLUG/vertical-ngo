ToDo list


**Models**
    * service template
        * DEV limit to 1 Container Service for off_duty type service
        * DEV management of working/holiday calendar
    * service rule
        * DEV complete rule method management
    * calendar
        * DEV check module
    * demo data
        * FIX content


**Views**
    * service template form
        * FIX custom css loading
        * FIX eliminate self.id from next list
        * FIX on deploy off_duty set to readonly
        * FIX auto select template on generation form
        * FIX layout
    * service allocate tree
        * FIX check rule button position
        * FIX direct call of rule method for overlap check
    * service allocate form
        * FIX direct call of rule method for overlap check
    * service allocate calendar
        * DEV text format
        * DEV lock action on empty cells
        * DEV check/alert template expected fulfillment
        * FIX employee name display (newline separated)
        * FIX element dedicated color (web_calendar)
    * service allocate timeline
        * DEV try add another level of group (ie. locality)
        * DEV check UIX
        * DEV check/alert template expected fulfillment
        * FIX show computed field (employee_names)
        * FIX element dedicated color (web_timeline)
    * service rule
        * DEV add profile reference to employee, equipment, vehicle
        * FIX on deploy lock edit option
        * FIX optimize double_assign method
    * service profile
        * FIX filter available fields for selected rule
        * DEV create check for rule-field assignment (association, mandatory)
    * reporting
        * DEV all


**Security**
    * fix model authorizations


**Readme**
oca-gen-addon-readme --repo-name vertical-ngo --branch 12.0 --addon-dir ~/odoo-dev/odoo12/OCA/addons-custom-sp/service_planner/
