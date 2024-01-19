{
    'name': 'Transportation',
    'version': '1.0',
    'summary': 'Transportation Summary',
    'sequence': 10,
    'description': 'Transportation Description',
    'category': 'Tools',
    'website': 'https://mywebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/create_menu.xml',
        'views/transportation_menu.xml',
        'views/vehicle_type.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
