from odoo import api, fields, models

class HmsHotel(models.Model):
    _name = 'hms.hotel'
    _description = 'HmsHotel'

    name = fields.Char()

