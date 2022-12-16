# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _


class QualityControlNotification(models.Model):
    _name = "quality.control.notification"
    _description = "quality.control.notification"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    product_family = fields.Char(
        string="Familia de producto",
        readonly=True
    )
    last_quantity = fields.Float(
        string="Cantidad Anterior",
        #readonly=True
    )
    actual_quantity = fields.Float(
        string="Cantidad Actual",
        #readonly=True
    )
    date = fields.Date(
        string="Fecha",
        readonly=True
    )
    notification = fields.Char(
        string="Notificación",
    )
