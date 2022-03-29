from datetime import  datetime, date
import string
from odoo import api, fields, models

class form(models.Model):
    _inherit = 'form.form'

    tlf = fields.Integer(string='Phone')
    gmail = fields.Char(string='Gmail')
    form_list_ids=fields.One2many('form.subjet.list', 'form_subjet_id', string="Name")
    subjet_form_ids=fields.One2many('form.subjet.list', 'subjet_form_id', string="Subjets")
    current_date=fields.Date(string="Current Date")
    final_date=fields.Date(string="Final Date")
    
    @api.model
    def event_wizard(self):
        print('que paso zs')