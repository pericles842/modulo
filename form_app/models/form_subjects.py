import string
from odoo import api, fields, models

class career(models.Model):
    _name = 'form.career'
    _description='Carreras'

    name=fields.Char(string='Career')
    subjet_ids= fields.One2many('form.subjet', 'career_id', string='subjet' )
    form_ids = fields.One2many('form.form','career_id', string='form') 


class subjet(models.Model):
    _name = 'form.subjet'
    _description='Asingnaturas' 

    section = fields.Selection([('a','A'),
                                ('b','B'),
                                ('c','C')], string='Section')
    code = fields.Char(string='Code')
    name= fields.Char(string='Name')
    credit_units = fields.Integer(string='Credit Units') 
    career_id = fields.Many2one('form.career', string="Career")
