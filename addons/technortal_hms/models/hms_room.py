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

    def action_view_booking(self):
        return {
            "type":"ir.actions.act_window",
            "name":f"{self.name}'s booking",
            "view_mode":"list,form",
            "res_model":"hms.booking",
            "domain":[('room_id','=',self.id),('hotel_id','=',self.hotel_id.id)]
        }
