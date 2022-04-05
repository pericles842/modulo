from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class form(models.Model):
    _inherit = 'form.form'

    tlf = fields.Integer(string='Phone')
    gmail = fields.Char(string='Gmail')
    form_list_ids=fields.One2many('form.subjet.list', 'form_subjet_id', string="Name")
    subjet_form_ids=fields.One2many('form.subjet.list', 'subjet_form_id', string="Subjets")
    form_wizard_ids = fields.Many2many('form.wizard', string='form_wizard')

    @api.model
    def action_wizard(self):
        act_window_server={
        "type":"ir.actions.act_window",
        "name":"Incripcion",
        "res_model":"form.wizard",
        "view":"view_form_wizard",
        "action_id":"view_form_wizard",
        "view_mode":"form",
        "context":{'form_wizard_ids': self.id},
        "target":"new"
        }
        return act_window_server