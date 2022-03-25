{
    'name':'Form Inheritance',
    'description':'Formulario de gestion.',
    'author':'louis_sarmiento',
    'depends':['form_app'],
    'data':[
        'security/ir.model.access.csv',
        'views/form_search.xml',
        'views/form.xml',
        'views/form_teachers.xml',
        'views/form_subjets.xml',
        'report/form_form_report.xml',
        'wizard/view_form.fom.xml'
        
    ],
    'css': ['static/src/css/my_style.css'],
    'application': False,
}