# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _

import datetime


class StockMoveQualityControl(models.Model):
    _inherit = 'stock.move'
    _description = "stock.move"

    def _cron_stock_move_quality_control(self, product_domain, quantity, channel):
        domain = [
            ('state', '=', 'done'),
            ('location_id.usage', '=', 'production'),
        ] + product_domain
        stock_move_ids = self.search(domain)
        total_move = 0.0
        for stock_move_id in stock_move_ids:
            total_move += stock_move_id.product_qty

        channel_id = self.env['mail.channel'].search([('name', '=', channel)])

        last_notification_ids = self.env['quality.control.notification'].search(
            [('product_family', '=', product_domain[0][-1])])

        if not last_notification_ids:
            vals = {
                'product_family': product_domain[0][-1],
                'last_quantity': 0.0,
                'actual_quantity': total_move,
                'date': datetime.datetime.today(),
                'notification': "Notificación inicial",
            }
            last_notification = self.env['quality.control.notification'].create(
                vals)

            display_msg = """ Alerta inicial: <br/>"""
            display_msg += """<ul>"""
            display_msg += """<li>Familia de producto: """ + \
                str(vals['product_family']) + """</li>"""
            display_msg += """<li>Cantidad: """ + \
                str(vals['last_quantity']) + """ <i class="fa fa-long-arrow-right"></i> """ + \
                str(vals['actual_quantity']) + """</li>"""
            display_msg += """</ul>"""

            last_notification.message_post(body=display_msg)

        else:
            for last_notification_id in last_notification_ids[-1]:
                if quantity < total_move - last_notification_id.actual_quantity:
                    vals = {
                        'product_family': product_domain[0][-1],
                        'last_quantity': last_notification_id.actual_quantity,
                        'actual_quantity': total_move,
                        'date': datetime.datetime.today(),
                        'notification': "Alerta de Calidad familia %s" % (product_domain[0][-1]),
                    }
                    last_notification = self.env['quality.control.notification'].create(
                        vals)

                    display_msg = """ Alerta de Calidad generada: <br/>"""
                    display_msg += """<ul>"""
                    display_msg += """<li>Familia de producto: """ + \
                        str(vals['product_family']) + """</li>"""
                    display_msg += """<li>Cantidad: """ + \
                        str(vals['last_quantity']) + """ <i class="fa fa-long-arrow-right"></i> """ + str(
                            vals['actual_quantity']) + """</li>"""
                    display_msg += """</ul>"""

                    last_notification.message_post(body=display_msg)

                    # activity
                    activity = self.env['mail.activity'].search(
                        [('res_id', '=', last_notification.id), ('activity_type_id', '=', 4)])
                    if not activity:
                        for res_partner_id in channel_id.channel_last_seen_partner_ids:
                            user_id = self.env['res.users'].search([('partner_id','=',res_partner_id.partner_id.id)])
                            if user_id:
                                vals_activity = {
                                    'display_name': "Realizar control de Calidad",
                                    'summary': "Realizar control de Calidad",
                                    'note': display_msg,
                                    'date_deadline': datetime.datetime.today(),
                                    'user_id': user_id.id,
                                    'res_id': last_notification.id,
                                    'activity_type_id': 4,
                                    'res_model_id': self.env['ir.model'].search([('model', '=', 'quality.control.notification')]).id,
                                }
                                self.env['mail.activity'].create(vals_activity)

                   