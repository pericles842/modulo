from datetime import  datetime, date
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError 

class form(models.TransientModel):
    _name = 'form.wizard'

    current_date=fields.Date(string="Current Date",required=True)
    final_date=fields.Date(string="Final Date", required=True )
    form_form_ids = fields.Many2many('form.form', string='form.form')
    
    def event_wizard(self):
        docs= self.env['form.form'].search([])
        for date in docs:
            data={}
            if date.registration_date >= self.current_date and self.final_date:
                data['docs'] = date
        print(data)
        return self.env.ref('form_inheritance.action_form_report').report_action(self, data = data)

    @api.onchange('current_date','final_date')
    def validation_one(self):
        if self.current_date:
            if str(self.final_date) < str(self.current_date) or str(self.current_date) > str(self.final_date):
                self.current_date = date.today()
                self.final_date = date.today()
                raise ValidationError('La fecha de inicio no puede ser menor a la fecha final')
            # elif str(self.final_date)> str(date.today()):
            #     raise ValidationError('No existen registros de esta fecha :'+ str(self.final_date))