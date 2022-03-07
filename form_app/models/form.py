from cgi import FieldStorage
from dataclasses import field
import string
from unicodedata import name
from odoo import api, fields, models 

class form(models.Model):
    _name = 'form.form'

    name = fields.Char(string='name') #campo