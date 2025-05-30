# Odoo Custom Receipt Fields Transfer

This module automatically transfers custom fields from receipts to internal transfers in Odoo 16.

## Custom Fields Supported
- Consignee (x_studio_consignee)
- Condition of Goods (x_studio_condition_of_goods)
- Destination City (x_studio_destination_city)
- Please Specify (x_studio_please_specify)

## Installation
1. Copy the `custom_receipt_fields_transfer` folder to your Odoo addons directory
2. Update the app list in Odoo
3. Install the module from Apps menu

## How it Works
When you validate a receipt in Odoo, if an internal transfer is created, this module automatically copies the custom field values from the receipt to the internal transfer.

## Compatibility
- Odoo 16.0
- Requires web_studio module
EOF

## Deploy to Odoo SH

1. Go to your Odoo SH dashboard
2. Connect your GitHub repository to your Odoo SH project
3. The module will be automatically deployed
4. Go to Apps in your Odoo instance
5. Update the app list
6. Search for "Custom Receipt Fields Transfer"
7. Install the module


## Verification

After installation, test the functionality:

1. Create a receipt with your custom fields filled
2. Validate the receipt
3. Check if an internal transfer was created
4. Verify that the custom fields were copied to the internal transfer
