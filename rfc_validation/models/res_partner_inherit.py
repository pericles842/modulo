from odoo import  api, models,fields
from odoo.exceptions import UserError, ValidationError


class ResParther(models.Model):
    _inherit = 'res.partner'

    switch = fields.Boolean(False)
    
    rfc = fields.Char(string='RFC')
    nationality = fields.Selection(  selection=[('e', 'Foreign'), ('n', 'Nacional')], default="e" )
    fiscal_id = fields.Char(string='Fiscal ID')


    @api.onchange('rfc')
    def _onchange_rfc(self):
        if self.rfc :
            records = self.env['res.partner'].search([['rfc', '=', self.rfc]])
            for i in records:
                if i.id != self.id:
                    raise ValidationError('rfc ya existe')

    @api.onchange('rfc')
    def _onchange_nationality(self):
        if self.nationality == 'e':
            if self.company_type == 'company' or self.company_type == 'person':
                if not self.rfc :
                    self.rfc = 'XEXX010101000'
                else:
                    if self.rfc != 'XAXX010101000' or self.rfc !=  'XEXX010101000':
                        raise ValidationError ('EL rfc extranjero no puede ser direfente a XAXX010101000 o XEXX010101000' )
        elif self.nationality == 'n' and self.company_type == 'person':
            self.rfc = str(self.rfc.upper())
            if len(self.rfc) != 13:
                raise ValidationError('El numero de caracteres debe ser 13')
        elif self.nationality == 'n' and self.company_type == 'company':
            self.rfc = str(self.rfc.upper())
            if len(self.rfc) != 12:
                raise ValidationError('El numero de caracteres debe ser 12')