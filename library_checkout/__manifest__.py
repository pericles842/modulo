{ 'name': 'Library Book Borrowing',
'description': 'Members can borrow books from the library.',
'author': 'Louis Sarmiento',
'depends': ['library_member'],
'data': [
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/checkout_view.xml',
],
}