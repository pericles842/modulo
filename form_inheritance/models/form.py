from odoo import api, fields, models

class form(models.Model):
    _inherit = 'form.form'

    tlf = fields.Integer(string='Phone')
    gmail = fields.Char(string='Gmail')
    form_list_ids=fields.One2many('form.subjet.list', 'form_subjet_id', string="Name")
    subjet_form_ids=fields.One2many('form.subjet.list', 'subjet_form_id', string="Subjets")