from odoo import api, fields, models
from odoo.exceptions import Warning #inportaciones de odoo del nucleo de odoo

class Book(models.Model):
    _name = 'library.book' #identificador del modelo 
    
    _description = 'Book' # nombre para los registros del modelo 
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Active?', default=True) #activar registros  y para saber si aun ahi libros
    date_published = fields.Date() # fecha de publicacion del libro
    image = fields.Binary('Cover')  # imagen de portada del libro 
    publisher_id = fields.Many2one('res.partner', string='Publisher') #direccion id 
    author_ids = fields.Many2many('res.partner', string='Authors') #lista de autores
    
    
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