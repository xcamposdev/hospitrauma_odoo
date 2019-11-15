# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class StockPicking(models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'

    def on_barcode_scanned(self, barcode):
        str00 = '00'
        str99 = '99'
        str_barcode = str(barcode)
        import pdb; pdb.set_trace()
        if str_barcode.find(str00) > -1 and str_barcode.find(str99) > -1:
            # If barcode has the format '00product99lot' encode product and lot in new line
            str_barcode = str(barcode)
            product_barcode = str_barcode[str_barcode.find(str00)+2:str_barcode.find(str99)]
            lot_barcode = str_barcode[str_barcode.find(str99)+2:]
            # find product using barcode and lot
            product = self.env['product.product'].search([('barcode', '=', product_barcode)])
            lot = self.env['stock.production.lot'].search([('name', '=', lot_barcode)])
            if len(product) > 1:
                # if more than one product, raise warning
                raise Warning('Several products have the same serial number. %s' % product.mapped('name'))
            if not product:
                raise Warning('Product not found.')
            if len(lot) > 1:
                # if more than one lot, raise warning
                raise Warning('Several lot have the same lot number.')
            if not lot:
                raise Warning('Lot not found.')
            # else add line
            self.move_line_ids += self.move_line_ids.new({
                'product_id': product.id,
                'product_uom_id': product.uom_id.id,
                'lot_id': lot.id,
                'location_id': self.location_id.id,
                'location_dest_id': self.location_dest_id.id,
                'qty_done': (product.tracking == 'none' and picking_type_lots) and qty or 1.0,
                'product_uom_qty': 0.0,
                'date': fields.datetime.now(),
            })
        else:
            # call super
            return super(StockPicking, self).on_barcode_scanned(barcode)


        
        