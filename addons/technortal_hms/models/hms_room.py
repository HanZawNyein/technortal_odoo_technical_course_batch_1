from odoo import api, fields, models


class HmsRoom(models.Model):
    _name = 'hms.room'
    _description = 'HmsRoom'

    name = fields.Char(required=True)
    hotel_id = fields.Many2one('hms.hotel',required=True)
    type = fields.Selection([
        ('normal', 'Normal'),
        ('vip', 'VIP'),
        ('vvip','VVIP')],default='normal')
