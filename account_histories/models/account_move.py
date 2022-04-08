# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def create(self,vals):
        rec = super(AccountMove,self).create(vals)
        if rec:
            value = {
                        "date": date.today(),
                        "total": rec.amount_total,
                    }
            self.env['account.histories'].create(value)
        return rec


