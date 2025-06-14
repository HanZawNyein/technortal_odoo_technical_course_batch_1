from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HmsRoom(models.Model):
    _name = 'hms.room'
    _description = 'HmsRoom'

    name = fields.Char(required=True)
    hotel_id = fields.Many2one('hms.hotel', required=True)
    type = fields.Selection([
        ('normal', 'Normal'),
        ('vip', 'VIP'),
        ('vvip', 'VVIP')], default='normal')
    state = fields.Selection([('available', 'Available'), ('not_available', 'Not Available')],
                             default='available', compute="_compute_booking_ids")

    booking_ids = fields.One2many('hms.booking', 'room_id')
    # price_unit = fields.Float()
    currency_id = fields.Many2one('res.currency', string='Currency',related='hotel_id.currency_id')
    price_unit = fields.Monetary(currency_field='currency_id', string='Price')

    _sql_constraints = [
        ('hms_room_name_unique', 'unique(name)', 'Room name already exists.')
    ]

    def action_view_booking(self):
        return {
            "type": "ir.actions.act_window",
            "name": f"{self.name}'s booking",
            "view_mode": "list,form",
            "res_model": "hms.booking",
            "domain": [('id', 'in', self.booking_ids.ids)]
            # "domain": [('room_id', '=', self.id), ('hotel_id', '=', self.hotel_id.id)]
        }

    @api.depends('booking_ids.state')
    def _compute_booking_ids(self):
        if 'paid' in self.booking_ids.mapped('state'):  # ['done','cancel,'paid']
            self.state = 'not_available'
        else:
            self.state = 'available'

    # @api.constrains('name')
    # def _check_name(self):
    #     if self.name in self.search([('id','!=',self.id)]).mapped('name'):
    #         raise ValidationError(_("Name should be unique."))
