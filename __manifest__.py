# -*- coding: utf-8 -*-
{
    'name': "vit_portofolio",

    'summary': """
        Website Portofolio
    """,

    'description': """
        https://github.com/armannurhidayat
    """,

    'author': "Arman Nur Hidayat <vitraining>",
    'website': "https://github.com/armannurhidayat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'website'],

    # always loaded
    'data': [
        # 'views/menu.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/group.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}