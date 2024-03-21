# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class PurchaseOrderCustom(models.Model):
    _inherit = 'purchase.order'

    def _default_requester(self):
        employee = self.env['hr.employee'].sudo().search(
            [('user_id', '=', self.env.uid)], limit=1)
        if employee:
            return employee.id

    requester_id = fields.Many2one('hr.employee', string="Requested By", required=True, default=_default_requester,
                                   readonly=True, store=True, states={'draft': [('readonly', False)]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Draft'),
        ('confirmed', 'Confirmed by PO'),
        ('to approve', 'Recommended By Accountant'),
        ('purchase', 'Approved by FM'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='sent', track_visibility='onchange')

    @api.multi
    def button_confirm(self):
        self.write({'state': 'confirmed'})
        return {}

    @api.multi
    def button_recommend(self):
        self.write({'state': 'to approve'})
        return {}

    @api.multi
    def button_approve(self, force=False):
        self._add_supplier_to_product()
        self.write({'state': 'purchase', 'date_approve': fields.Date.context_today(self)})
        self.filtered(lambda p: p.company_id.po_lock == 'lock').write({'state': 'done'})
        return {}