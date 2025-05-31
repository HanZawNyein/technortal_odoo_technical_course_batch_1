from odoo import api, fields, models,_


class HmsBooking(models.Model):
    _name = 'hms.booking'
    _description = 'HmsBooking'

    reference = fields.Char( default=lambda self: _('New'),readonly=True)
    description = fields.Text()
    hotel_id = fields.Many2one('hms.hotel', required=True)
    room_id = fields.Many2one('hms.room', required=True)
    type = fields.Selection([
        ('section', 'Section'),
        ('daily', 'Daily'),
    ], default='daily')
    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirm', 'Confirmed'),
         ('paid', 'Paid'),
         ('done', 'Done'),
         ('cancel', 'Cancelled')], default='draft')

    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirm'

    def action_paid(self):
        self.state = 'paid'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'