{'name': 'Library Book Borrowing',
 'description': 'Members can borrow books from the library.',
 'author': 'Louis',
 'depends': [
     'library_member',
     'mail',
 ],
 'data': [
    'security/ir.model.access.csv',
    'data/library_checkout_stage.xml',
    'views/library_menu.xml',
    'views/checkout_view.xml',
    'views/checkout_kanban_view.xml'

    
 ],
}
