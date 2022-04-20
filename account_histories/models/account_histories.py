from odoo import api, fields, models 

class Histories(models.Model):
    _name='account.histories'
    _description='Extencion del historial'
    _author='louis'


    name = fields.Many2one('res.users', string='Name User', default=lambda self: self.env.user)
    date = fields.Date(string="Date")
    total = fields.Monetary(string="Total")
    currency_id = fields.Many2one('res.currency', string='Currency')