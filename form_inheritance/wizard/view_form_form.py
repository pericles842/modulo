from datetime import  datetime, date
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError 

class form(models.TransientModel):
    _name = 'form.wizard'

    current_date=fields.Date(string="Current Date", default=date.today())
    final_date=fields.Date(string="Final Date", default=date.today())
    form_form_ids = fields.Many2many('form.form', string='form.form')
    
    @api.model
    def event_wizard(self,record):
        print('asdasd')

    @api.onchange('current_date','final_date')
    def validation_one(self):
        if self.current_date:
            if str(self.final_date) < str(self.current_date) or str(self.current_date) > str(self.final_date):    
                self.current_date = date.today()
                raise ValidationError('La fecha de inicio no puede ser menor a la fecha final')
            # elif str(self.final_date)> str(date.today()):
            #     raise ValidationError('No existen registros de esta fecha :'+ str(self.final_date))