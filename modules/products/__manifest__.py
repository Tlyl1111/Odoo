{
    'name': 'Warehouse',
    'version': '1.0',
    'summary': 'Warehouse Summary',
    'sequence': 10,
    'description': 'Warehouse Description',
    'category': 'Tools',
    'website': 'https://mywebsite.com',
    'depends': ['base'],
    'data': [

        'security/ir.model.access.csv',
        'view/create_warehouse.xml',
        'view/warehouse_menu.xml',
        'view/shelves.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
