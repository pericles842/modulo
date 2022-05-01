{
    'name':'centaur_inventory',
    'description':'Inventario Basico',
    'author':'louis',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/centaur_inventory.xml',
        'views/sequence_centaur.xml',
        'views/sales_history.xml'
    ],
    'application': True, 
}