{
    'name': "Delivery validation",
    'summary': """This is the summary of this moduleeeee""",
    'description': """this is the discriptionn""",
    'version': '19.0.1.0',
    'license': 'LGPL-3',
    'sequence': 1,
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/warning.xml',
    ],
    'application': True,
    'auto_install': True,
    'installable': True,
}
