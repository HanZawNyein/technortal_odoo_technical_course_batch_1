from odoo import api, fields, models

class BookingPaymentWizard(models.TransientModel):
    _name = 'booking.payment.wizard'
    _description = 'BookingPaymentWizard'

    currency_id = fields.Many2one('res.currency', string='Currency')
    price_unit = fields.Monetary('Price')


