# -*- coding: utf-8 -*-
{
    'name': "barcode_custom",

    'summary': """
        Modify the barcode to be in format 00product_barcode99lot_number""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Guillaume Dauphin",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'purchase', 'stock_barcode'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}