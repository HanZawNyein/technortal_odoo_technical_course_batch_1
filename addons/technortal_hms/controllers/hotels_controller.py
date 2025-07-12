from odoo import http
from odoo.http import request


class HotelController(http.Controller):
    @http.route('/hotels', type='http', auth='public', website=True)
    def get_all_hotels(self, *args, **kwargs):
        hotel_ids = request.env['hms.hotel'].sudo().search([])
        context = {
            "hotel_ids": hotel_ids,
        }
        return request.render("technortal_hms.hms_hotel_template", context)

    @http.route('/rooms/<model("hms.hotel"):hotel_id>/<int:hotel_id_int>', type='http', auth='public', website=True)
    def get_all_rooms(self, hotel_id, hotel_id_int, *args, **kwargs):
        rooms_ids = request.env['hms.room'].search([('hotel_id', '=', hotel_id.id)])
        context = {
            "rooms_ids": rooms_ids,
        }
        return request.render("technortal_hms.hms_rooms_template", context)
