{
    'name': 'Orders',
    'version': '1.0',
    'summary': 'Orders Summary',
    'sequence': 10,
    'description': 'Orders Description',
    'category': 'Tools',
    'website': 'https://mywebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'view/orders.xml',
        'view/order_menu.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
