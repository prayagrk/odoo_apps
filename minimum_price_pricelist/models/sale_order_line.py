# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _description = "Sale Order Line inherited for custom logic"

    pricelist_price = fields.Float(string="PriceList Price", readonly=True)

    def _get_display_price(self):
        """
        Adding custom logic to display pricelist
        - Pick the max value from the price list calculation and price list minimum price.
        """
        price = super()._get_display_price()
        if (self.pricelist_item_id
                and self.pricelist_item_id.minimum_price
                and price < self.pricelist_item_id.minimum_price):
            return self.pricelist_item_id.minimum_price
        return price

    @api.onchange('product_id', 'product_uom_id')
    def _onchange_product_id(self):
        """ Function to store pricelist_price for the validation.  """
        for line in self:
            if line.product_id and line.order_id.pricelist_id:
                line.pricelist_price = line.price_unit

    @api.onchange('price_unit')
    def _onchange_unit_price(self):
        """  Function to show thw price change validation message. """
        if self.product_id and self.pricelist_price and self.price_unit != self.pricelist_price:
            return {
                'warning': {
                    'title': _("Price Change"),
                    'message': "You are updating the pricelist price."
                }
            }
