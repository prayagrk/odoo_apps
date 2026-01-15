# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductPriceListItem(models.Model):
    _inherit = "product.pricelist.item"
    _description = "Product Pricelist Item inherited for custom logic"

    minimum_price = fields.Float(string="Minimum Price",
                                 help="Minimum price for each product while using the pricelist.")
