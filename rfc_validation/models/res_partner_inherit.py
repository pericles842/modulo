

from odoo import  api, models,fields


class ResParther(models.Model):
    _inherit = 'res.partner'

    switch = fields.Boolean()
    
    rfc = fields.Char(string='RFC', required=True)
    nationality = fields.Selection( string="Nationality", selection=[('e', 'Foreign'), ('n', 'Nacional'),])

    @api.onchange('nationality')
    def _onchange_nationality(self):
        if self.nationality == 'e':
            print('SIRVE EXTRANGERO')
            print('SIRVE EXTRANGERO')
            print('SIRVE EXTRANGERO')
            print('SIRVE EXTRANGERO')
        elif self.nationality == 'n':
            print('SIRVE NACIONAL')
            print('SIRVE NACIONAL')
            print('SIRVE NACIONAL')
            print('SIRVE NACIONAL')