from odoo import api, fields, models 

class Histories (models.Model):
    _name='account.histories'
    _description='Extencion del historial'
    _author='louis'
    

    name_id = fields.Many2one('account.move', string='Name')
    date = fields.Date(string="Date")
    total = fields.Float(string="Total")
    num= fields.Char('N°', readonly=True, default='New')
    name = fields.Many2one('res.users', string='Name User', default=lambda self: self.env.user)


    @api.model
    def create(self, vals):
        if vals.get('num', 'New') == 'New':
            vals['num'] = self.env['ir.sequence'].next_by_code('account.increment')
        result = super(Histories, self).create(vals)
        return result


class AccountMove(models.Model):
    _inherit = "account.move"

    name_ids = fields.One2many('account.histories','name_id' )


    def assign(self,rec):
        dic = {

            'date' : rec.invoice_date_due , #campos del modelo accont move
            'total' : rec.amount_total,

        }
        self.env['account.histories'].create(dic)


    @api.model
    def create(self,vals):
        rec = super(AccountMove,self).create(vals)
        self.assign(rec)
        return rec  #traer un registro a un mdelo

