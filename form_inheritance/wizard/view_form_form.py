from datetime import  datetime, date
from odoo import api, fields, models

class form(models.TransientModel):
    _name = 'form.wizard'

    current_date=fields.Date(string="Current Date")
    final_date=fields.Date(string="Final Date")