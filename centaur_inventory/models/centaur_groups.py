from odoo import api, fields, models


class CentaurGroups(models.Model):
    _name = 'centaur.groups'
    _description = 'grupo de franelas'

    grup = fields.Char(string='Grupos')
    
    groups_ids = fields.One2many('centaur.inventory', 'groups_id', string='Grupos')

