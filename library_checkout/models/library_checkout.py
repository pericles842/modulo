from odoo import api, exceptions, fields, models

class Checkout(models.Model):
    _name = 'library.checkout'
    _description = 'Checkout Request'
    _inherit = ['mail.thread', 'mail.activity']

    checkout_date = fields.Date(readonly=True)
    close_date = fields.Date(readonly=True)
    member_id = fields.Many2one(
        'library.member',
        required=True)
    user_id = fields.Many2one(
        'res.users',
        'Librarian',
        default=lambda s: s.env.uid)
    request_date = fields.Date(
        default=lambda s: fields.Date.today())
    line_ids = fields.One2many(
        'library.checkout.line',
        'checkout_id',
        string='Borrowed Books',) 


    def _default_stage(self):
        Stage = self.env['library.checkout.stage']
        return Stage.search([], limit=1)

    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)

    stage_id = fields.Many2one(
        'library.checkout.stage',
        default=_default_stage,
        group_expand='_group_expand_stage_id')
    state = fields.Selection(related='stage_id.state') 

    @api.onchange('member_id')
    def onchange_member_id(self):
        today = fields.Date.today()
        if self.request_date != today:
            self.request_date = fields.Date.today()
            return {
            'warning': {
            'title': 'Changed Request Date',
            'message': 'Request date changed to today.',
        }
    }

    def create(self, vals):
        # Code before create: should use the `vals` dict
        if 'stage_id' in vals:
            Stage = self.env['library.checkout.stage']
            new_state = Stage.browse(vals['stage_id']).state
            if new_state == 'open':
                vals['checkout_date'] = fields.Date.today()
        new_record = super().create(vals)
        # Code after create: can use the `new_record` created
        if new_record.state == 'done':
            raise exceptions.UserError(
            'Not allowed to create a checkout in the done state.')
        return new_record 
                                #error falta xd
    def write(self, vals):
        # Code before write: can use `self`, with the old values
        if 'stage_id' in vals:
            Stage = self.env['library.checkout.stage']
            new_state = Stage.browse(vals['stage_id']).state
            if new_state == 'open' and self.state != 'open':
                vals['checkout_date'] = fields.Date.today()
            if new_state == 'done' and self.state != 'done':
                vals['close_date'] = fields.Date.today()
        super().write(vals)
        # Code after write: can use `self`, with the updated values
        return True




class CheckoutLine(models.Model):
    
    _name = 'library.checkout.line'
    _description = 'Borrow Request Line'

    checkout_id = fields.Many2one('library.checkout')
    book_id = fields.Many2one('library.book')    