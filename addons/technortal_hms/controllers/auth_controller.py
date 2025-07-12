from odoo import http
from odoo.http import request


class AuthController(http.Controller):
    @http.route('/api/info', type='json', auth='public')
    def api_info(self, *args, **kwargs):
        return {"message": "info."}

    @http.route('/api/login', type='json', auth='none', csrf=False, cors="*")
    def api_login(self, **kwargs):
        try:
            login = kwargs.get('login')
            password = kwargs.get('password')

            credential = {'login': login, 'password': password, 'type': 'password'}
            auth_info = request.session.authenticate(request.session.db, credential)
            return {"message": "Login Success.", "uid": auth_info}
        except Exception as e:
            return {"message": f"{e}"}

    @http.route('/api/partners', type='json', auth='user')
    def api_partners(self,limit=10,offset=0,order="id asc",*args, **kwargs):
        data = {
            "partners": request.env['res.partner'].search_read([], fields=['id', 'name'],
                                                               limit=limit, offset=offset,
                                                               order=order)
        }
        return data
