{
    'name': 'Library Website',
    'description': 'Create and check book checkout requests.',
    'author': 'Daniel Reis',
    'depends': ['library_checkout', 'website'],
    'data': [

    'security/ir.model.access.csv',
    'security/library_security.xml',
    'views/website_assets.xml',
    'views/checkout_template.xml',
    'views/library_member.xml',
    
    
 
    ],
}