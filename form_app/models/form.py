from dataclasses import field
from datetime import  datetime, date
from odoo import api, fields, models 


class form(models.Model):
    _name = 'form.form'

    name = fields.Char(string='Name', required=True) #campo
    last_name = fields.Char(string='Last Name')
    registration_date= fields.Datetime(string='Registration Date',default=fields.Date.today() )
    ci = fields.Integer(string='C.I')
    nationality = fields.Selection([('v','V'),
                                    ('e','E')],'nationality')
    sexo = fields.Selection([('male','Male'),
                             ('feminine','Feminine'),
                             ('other','Other')], string='Sexo')
    algo = fields.Selection([('civil','Civil'),
                              ('militar','Militar')], 'Civil/Militar')
    degree = fields.Char(string='Degree') #grado
    force = fields.Char(string='Force') #fuerza
    date_of_birth = fields.Date(string='Date Of Birth',required=True) #Fecha de nacimiento
    age = fields.Integer(string='Age')

        



