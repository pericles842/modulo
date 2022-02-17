from odoo import fields, models #inportaciones de odoo del nucleo de odoo

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
        print("HOla")