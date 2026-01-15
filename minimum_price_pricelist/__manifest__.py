# -*- coding: utf-8 -*-

{
    'name': 'Pricelist Update',
    'version': '18.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Pricelist custom logic',
    'description': """
        This module is to add a custom logic on the pricelist workflow in sales.
    """,
    'author': 'Prayag',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_pricelist_item_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
