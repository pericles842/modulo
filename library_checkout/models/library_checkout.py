from odoo import api, exceptions, fields, models

class Checkout(models.Model):
    _name = 'library.checkout'
    _description = 'Checkout Request'
    
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
    # to add in the class Checkout:

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