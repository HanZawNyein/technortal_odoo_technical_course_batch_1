from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class HmsBooking(models.Model):
    _name = 'hms.booking'
    _description = 'HmsBooking'
    _rec_name = 'reference'
    _inherit =['mail.thread','mail.activity.mixin']

    reference = fields.Char( default=lambda self: _('New'),readonly=True,copy=False)
    description = fields.Text()
    hotel_id = fields.Many2one('hms.hotel', required=True,tracking=True)
    room_id = fields.Many2one('hms.room', required=True,tracking=True)
    type = fields.Selection([
        ('section', 'Section'),
        ('daily', 'Daily'),
    ], default='daily')
    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirm', 'Confirmed'),
         ('paid', 'Paid'),
         ('done', 'Done'),
         ('cancel', 'Cancelled')], default='draft',tracking=True)
    partner_id = fields.Many2one('res.partner')
    confirm_partner_id = fields.Many2one('res.partner',readonly=True)
    #,default=lambda self: self.env.user.partner_id.id)

    # @api.model
    # def create(self, values):
    #     # Add code here
    #     # values['reference']='B10000000'
    #     if (not values.get('reference')) or values.get('reference') == _('New'):
    #         values['reference'] = self.env['ir.sequence'].next_by_code('hms.booking') or _('New')
    #     return super(HmsBooking, self).create(values)

    def action_draft(self):
        # self.state = 'draft'
        self._available_state('draft')

    def action_confirm(self):
        self.reference = self.env['ir.sequence'].next_by_code('hms.booking') or _('New')
        self.confirm_partner_id = self.env.user.partner_id.id
        # self.state = 'confirm'
        self._available_state('confirm')

    def action_paid(self):
        # self.state = 'paid'
        self._available_state('paid')

    def action_done(self):
        # self.state = 'done'
        self._available_state('done')

    def action_cancel(self):
        # self.state = 'cancel'
        self._available_state('cancel')

    def _available_state(self,new_state):
        states = [('draft','confirm'),('confirm','cancel'),('confirm','paid'),('paid','done')]
        if (self.state,new_state) not in states:
            raise ValidationError(_(f"{self.state} to {new_state} is not available."))
        self.state = new_state