from datetime import  datetime, date
from odoo import api, fields, models

class form(models.TransietModel ):
    _name='form.wizard'
    _inherit = 'form.form'

    current_date=fields.Date(string="Current Date")
    final_date=fields.Date(string="Final Date")


    def button_send(self):
        return self.current_date
