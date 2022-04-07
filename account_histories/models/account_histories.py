from odoo import api, fields, models 

class histories (models.Model):
    _name='account.histories'
    _description='Extencion del historial'
    _author='louis'
    

    name_id = fields.Many2one('account.move', string='Name')
    date = fields.Date(string="Date")
    total = fields.Integer(string="Total")
    num = fields.Integer(string="N°", compute= lambda x : ++1)
    name = fields.Many2one('res.users', string='Name User', default=lambda self: self.env.user)



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

