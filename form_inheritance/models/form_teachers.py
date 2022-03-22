import string
from odoo import api, fields, models

class subjet(models.Model):
    _inherit ='form.subjet'

    teachers_ids = fields.Many2many('form.teachers', string='Teachers')
    subjet_list_ids=fields.One2many('form.subjet.list', 'name_id')


class teachers(models.Model):
    _name='form.teachers'
    _description='teachers'

    name=fields.Char(string="Name")
    subjet_ids=fields.Many2many('form.subjet',  string="Subjets")

class formSubjetList(models.Model): 
    _name='form.subjet.list'
    _inherit='form.subjet'

    name_id=fields.Many2one('form.subjet', string='Name' )
    form_subjet_id=fields.Many2one('form.form', string="Name") 
 