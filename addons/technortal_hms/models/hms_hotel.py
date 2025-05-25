from odoo import api, fields, models

class HmsHotel(models.Model):
    _name = 'hms.hotel'
    _description = 'HmsHotel'

    name = fields.Char()
    room_ids = fields.One2many('hms.room','hotel_id')

