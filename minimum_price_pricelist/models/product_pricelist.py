# -*- coding: utf-8 -*-

from odoo import models


class ProductPriceList(models.Model):
    _inherit = "product.pricelist"
    _description = "Product Pricelist inherited for custom logic"

    def _compute_price_rule(
            self, products, quantity, currency=None, uom=None, date=False, compute_price=True):
        """
        Adding custom logic to compute price rule
        - Pick the max value from the price list calculation and price list minimum price.
        """
        result = super()._compute_price_rule(
            products, quantity=quantity, currency=currency, date=date, uom=uom, compute_price=compute_price)
        for product, (price, rule_id) in result.items():
            if rule_id:
                rule = self.env['product.pricelist.item'].browse(rule_id)
                if rule.minimum_price and price < rule.minimum_price:
                    result[product] = (rule.minimum_price, rule_id)
        return result

