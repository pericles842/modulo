from odoo import api, fields, models
from odoo.exceptions import Warning #inportaciones de odoo del nucleo de odoo

class Book(models.Model):
    _name = 'library.book' #identificador del modelo 
    author_ids = fields.Many2many(
    'res.partner', string='Authors')
    _description = 'Book' # nombre para los registros del modelo
    _order = 'name, date_published desc'
    
    name = fields.Char(
        'Title',
        default=None,
        index=True,
        help='Book cover title',
        readonly=False,
        required=True,
        translate=False,
    )
    isbn = fields.Char('ISBN')
    book_type = fields.Selection(
        [('paper','Paperback'),
        ('hard','Hardcover'),
        ('electronic','Electronic'),
        ('other', 'Other')],
        'Type')
    notes = fields.Text('Internal Notes')
    descr = fields.Html('Description')
    # Campos numéricos:
    copies = fields.Integer(default=1)
    avg_rating = fields.Float('Average Rating', (3, 2))
    price = fields.Monetary('Price', 'currency_id')
    currency_id = fields.Many2one('res.currency') # price helper
    active = fields.Boolean('Active?', default=True) #activar registros  y para saber si aun ahi libros
    date_published = fields.Date() # fecha de publicacion del libro
    image = fields.Binary('Cover')  # imagen de portada del libro 
    publisher_id = fields.Many2one('res.partner', string='Publisher') #direccion id 
    author_ids = fields.Many2many('res.partner', string='Authors') #lista de autores
    target_field = fields.Char('Target Field')
    
    
    def button_check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check 

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('Please provide an ISBN for %s' % book.name)
            if book.isbn and not book._check_isbn():
                    raise Warning('%s is an invalid ISBN' % book.isbn)
        return True
    category_id = fields.Many2one('library.book.category', string='Category')

    publisher_country_id = fields.Many2one(
        'res.country',
        string='Publisher Country',
        compute='_compute_publisher_country',
        inverse='_inverse_publisher_country',
        search='_search_publisher_country',
    )

    @api.depends('publisher_id.country_id')
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id

    @api.depends('publisher_country_id')
    def _inverse_publisher_country(self):
        for book in self:
            if book.publisher_id:
                book.publisher_id.country_id = book.publisher_country_id

    def _search_publisher_country(self, operator, value):
        return [('publisher_id.country_id', operator, value)]

    publisher_country_related = fields.Many2one(
        'res.country',
        string='Publisher Country (related)',
        related='publisher_id.country_id',
    )

    _sql_constraints = [
        ('library_book_name_date_uq',
         'UNIQUE (name, date_published)',
         'Book title and publication date must be unique.'),
        ('library_book_check_date',
         'CHECK (date_published <= current_date)',
         'Publication date must not be in the future.'),
    ]

    @api.constrains('isbn')
    def _constrain_isbn_valid(self):
        for book in self:
            if book.isbn and not book._check_isbn():
                raise ValidationError(
                    '%s is an invalid ISBN' % book.isbn)
