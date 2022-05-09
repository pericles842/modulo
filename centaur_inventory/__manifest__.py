{
    'name':'centaur_inventory',
    'description':'Inventario Basico',
    'author':'louis',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/centaur_inventory.xml',
        'views/sequence_centaur.xml',
        'views/search_centaur_inventory.xml',
        'views/sales_history.xml',
        'views/search_default.xml',
        'views/centaur_groups.xml'
    ],
    'application': True, 
}