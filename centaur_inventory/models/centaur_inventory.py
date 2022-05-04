from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from random import randint
from datetime import  datetime, date

class CentaurInventory(models.Model):
    _name = 'centaur.inventory'
    _description = 'inventario'

    name = fields.Char(default="Producto", copy="1", readonly="1")
    
    groups = fields.Selection(string='Grupo',
                             selection=[
                              ('f', 'Franelas'),
                              ('s', 'Short'),
                              ('p', 'Pantalones')])
    size = fields.Selection(string='Talla',
                            selection=[
                                ('s', 'S'),
                                ('m', 'M'),
                                ('l', 'L')])
    serial = fields.Integer(string='Serial',
                             required=True,
                             default=randint(100,1000))
    product_date = fields.Date(string='Fecha de producto',
                                default=date.today(),
                                readonly="1")
    state = fields.Selection(string='Estado',
                             selection=[
                            ('unsold', 'No vendido'),
                            ('sale', 'Vendido')],
                            default='unsold')
    
    description = fields.Char(string='Descripcion')
    sale = fields.Boolean(string='Vendido',
                        default = False)
    total = fields.Integer(string='Precio')
    note = fields.Text(string='Nota')
    



    @api.onchange('sale')
    def _sale_date(self):
        if self.sale == True:
            print('bandera1')
            print('bandera1')
            print('bandera1')
            print('bandera1')
            print('bandera1')
            self.state = 'sale'
        elif self.sale == False:
            print('bandera2')
            print('bandera2')
            print('bandera2')
            print('bandera2')
            self.state = 'unsold'


    @api.model
    def create(self, vals):
        if vals.get('name', 'Producto') == 'Producto':
            vals['name'] = self.env['ir.sequence'].next_by_code('account.sequence')
        result = super(CentaurInventory, self).create(vals) 
        return result 


    @api.onchange('serial')
    def _validation_serial(self):
        if self.serial:
            contact = self.env['centaur.inventory'].search([['serial', '=', self.serial]])
            if contact:
                for c in contact:
                    if c.id != self.id:
                         self.serial = randint(100,1000)

    @api.onchange('serial')
    def _onchange_serial(self):
        if self.serial:
            if self.serial != 0:
                if self.serial < 100  or self.serial > 1000:
                    raise ValidationError('El serial debe ser de 3 digitos')
        elif self.serial == 0:
            raise ValidationError('el serial no puede quedar en 0')


