import string
from unicodedata import name
from odoo import api, fields, models

class form(models.Model):
    _inherit = 'form.form'

    tlf = fields.Integer(string='Phone')
    gmail = fields.Char(string='Gmail')

