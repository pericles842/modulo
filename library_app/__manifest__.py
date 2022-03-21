{
'name': 'Library Management', #nombre de la APP 
'description': 'Manage library book catalogue and lending.', # descripcion 
'author': 'Louis', #autor del modulo 
'depends': ['base'], #dependencias de otros modulos en este caso modulo central 
'data': [
    'security/library_security.xml',
    'security/ir.model.access.csv', # se agregan los archivos xml
    'views/library_menu.xml',
    'views/book_view.xml',
    'views/book_list_template.xml',
    'reports/library_book_report.xml',
    'reports/library_book_sql_report.xml'

],
'demo':[
    'data/res.partner.csv',
    'data/library.book.csv',
    'data/book_demo.xml',
],
'application': True, #valor boleano que define si instalara o no 
}