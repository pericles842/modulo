from datetime import  datetime, date
from email.policy import default
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError 


class form(models.Model):
    _name = 'form.form'
    

    name = fields.Char(string='Name', required=True) #campo
    last_name = fields.Char(string='Last Name')
    registration_date= fields.Datetime(string='Registration Date',default=fields.Date.today() )
    ci = fields.Integer(string='C.I', required=True)
    nationality = fields.Selection([('v','V'),
                                    ('e','E')],default="v", string='nationality', readonly='1')
    sexo = fields.Selection([('male','Male'),
                             ('feminine','Feminine'),
                             ('other','Other')], string='Sexo')
    algo = fields.Selection([('civil','Civil'),
                              ('militar','Militar')], default='civil', string='Civil/Militar')
    degree = fields.Char(string='Degree') #grado
    force = fields.Char(string='Force') #fuerza
    date_of_birth = fields.Date(string='Date Of Birth',required=True) #Fecha de nacimiento
    age = fields.Integer(string='Age')

    @api.onchange('ci')
    def validate_id(self):
        lenn =str(self.ci)
        if len(lenn) != 1:
            if len(lenn) == 8 or len(lenn) == 7:
                if  self.ci < 79999999: 
                    self.nationality = 'v'
                elif self.ci > 80999999:
                    self.nationality = 'e'
            elif len(lenn) > 8 or len(lenn) < 7:
                raise ValidationError('The ID must contain 8 digits')
        
        
        

        



