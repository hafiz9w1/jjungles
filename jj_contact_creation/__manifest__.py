
{
    'name': 'Contacts Creation',
    'version': '16.0.0.0.1',
    'author': 'Hafiz Abbas',
    'email': 'hafizabbas9w1@gmail.com',
    'sequence': 2,
    'category': 'Technical',
    'Summary': 'Contact creation',
    'description': """
        Contact Creation
    """,
    'depends': [
        'sale_management',
    ],
    'assets': {
        'web.assets_backend': [
            'jj_contact_creation/static/src/js/res_partner.js',
            'jj_contact_creation/static/src/xml/res_partner.xml',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'wizard/contact_creation_views.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
