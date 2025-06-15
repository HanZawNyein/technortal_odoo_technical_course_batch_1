from odoo import api, fields, models

class BookingPaymentWizard(models.TransientModel):
    _name = 'booking.payment.wizard'
    _description = 'BookingPaymentWizard'

    currency_id = fields.Many2one('res.currency', string='Currency')
    price_unit = fields.Monetary('Price')

    def action_paid(self):
        context = self.env.context
        active_model = context.get('active_model')
        active_id = context.get('active_id')
        # recordset = self.env['hms.booking'].browse(active_id)
        recordset = self.env[active_model].browse(active_id)
        recordset._paid()
        # print(self.env.context)


