from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    def _action_done(self):
        """Override to copy custom fields to any created internal transfers"""
        custom_fields_data = {}
        for picking in self:
            if picking.picking_type_id.code == 'incoming':  # Only for receipts
                custom_fields_data[picking.id] = {
                    'x_studio_consignee': picking.x_studio_consignee,
                    'x_studio_condition_of_goods': picking.x_studio_condition_of_goods,
                    'x_studio_destination_city': picking.x_studio_destination_city,
                    'x_studio_please_specify': picking.x_studio_please_specify,
                }
        
        result = super()._action_done()
        
        for picking in self:
            if picking.id in custom_fields_data:
                internal_transfers = self.env['stock.picking'].search([
                    ('origin', '=', picking.name),
                    ('picking_type_id.code', '=', 'internal'),
                    ('state', 'in', ['waiting', 'confirmed', 'assigned'])
                ])
                
                for transfer in internal_transfers:
                    transfer.write(custom_fields_data[picking.id])
        
        return result
    
    @api.model
    def _create_backorder(self, backorder_moves):
        """Override to copy custom fields to backorders"""
        backorders = super()._create_backorder(backorder_moves)
        
        for backorder in backorders:
            if backorder.backorder_id:
                backorder.write({
                    'x_studio_consignee': backorder.backorder_id.x_studio_consignee,
                    'x_studio_condition_of_goods': backorder.backorder_id.x_studio_condition_of_goods,
                    'x_studio_destination_city': backorder.backorder_id.x_studio_destination_city,
                    'x_studio_please_specify': backorder.backorder_id.x_studio_please_specify,
                })
        
        return backorders

class StockMove(models.Model):
    _inherit = 'stock.move'
    
    def _create_extra_move(self):
        """Override to handle custom fields when creating extra moves that generate internal transfers"""
        result = super()._create_extra_move()
        
        if self.picking_id and self.picking_id.picking_type_id.code == 'incoming':
            if result and result.picking_id:
                result.picking_id.write({
                    'x_studio_consignee': self.picking_id.x_studio_consignee,
                    'x_studio_condition_of_goods': self.picking_id.x_studio_condition_of_goods,
                    'x_studio_destination_city': self.picking_id.x_studio_destination_city,
                    'x_studio_please_specify': self.picking_id.x_studio_please_specify,
                })
        
        return result
