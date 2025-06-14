from odoo import api, fields, models

class HmsHotel(models.Model):
    _name = 'hms.hotel'
    _description = 'HmsHotel'

    name = fields.Char()
    tags = fields.Many2many('res.partner.category')
    room_ids = fields.One2many('hms.room','hotel_id')
    active = fields.Boolean('Active', default=True)
    currency_id = fields.Many2one('res.currency',required=True)