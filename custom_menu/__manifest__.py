# -*- coding: utf-8 -*-
{
    'name': "Custom Menus",

    'summary': """
        Hide Unwanted Menus""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Xero1",
    'website': "http://www.xero1.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','om_account_budget','om_account_asset','account','hr_holidays','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}