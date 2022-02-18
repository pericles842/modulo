from odoo import http

class Books(http.Controller):
                                                # @http.route
                                                #importante, ya que declara el punto final 
                                                # de URL que estará vinculado al método de clase
    @http.route('/library/books', auth='user') # agregar el acceso anonimo , public 
    def list(self, **kwargs):
        Book = http.request.env['library.book']
        books = Book.search([])
        return http.request.render( #renderizar la plantilla de  odoo
             'library_app.book_list_template', {'books': books})