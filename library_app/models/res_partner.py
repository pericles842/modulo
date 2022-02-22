from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'
    book_ids = fields.Many2many(
    'library.book', string='Authored Books')

    published_book_ids = fields.One2many(
        'library.book',  # modelo relacionado
        'publisher_id',  # campo para "esto" en el modelo relacionado
        string='Published Books')

    book_ids = fields.Many2many(
        'library.book', string='Authored Books')
