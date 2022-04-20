from odoo import api, fields, models
from datetime import date

class AccountMove(models.Model):
    _inherit = "account.move"


    button = fields.Boolean('Credit', default=False)
    num_sequence = fields.Char('0001', readonly=True, default='Num')

    @api.model
    def create(self, vals):
        if vals.get('num_sequence', 'Num') == 'Num':
            vals['num_sequence'] = self.env['ir.sequence'].next_by_code('account.sequence') or 'Num'
        result = super(AccountMove, self).create(vals)
        return result

    @api.onchange('button')
    def button_check(self):
        if self.button == True and self.state =='draft':
            self.name = self.num_sequence
        else:
            self.button = False


    @api.model
    def create(self,vals):
        rec = super(AccountMove,self).create(vals)
        if rec:
            value = {
                        "date": date.today(),
                        "total": rec.amount_total,
                    }
            self.env['account.histories'].create(value)
        return rec
