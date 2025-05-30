{
    'name': 'Custom Receipt Fields Transfer',
    'version': '16.0.1.0.0',
    'summary': 'Transfer custom fields from receipts to internal transfers',
    'description': """
        This module ensures that custom fields added to receipts are 
        automatically copied to internal transfers created during validation.
        
        Compatible with Odoo 16.0
        
        Custom Fields Supported:
        - Consignee (x_studio_consignee)
        - Condition of Goods (x_studio_condition_of_goods)
        - Destination City (x_studio_destination_city)
        - Please Specify (x_studio_please_specify)
    """,
    'category': 'Inventory/Inventory',
    'author': 'Company',
    'website': 'https://www.company.com',
    'depends': ['stock', 'web_studio'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
