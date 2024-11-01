from odoo import fields, models


class ContactCreation(models.TransientModel):
    _name = 'contact.creation'
    _description = 'Contact Creation'

    name = fields.Char(
        string='Contact Name',
        help='Contact Name.',
    )

    def action_create_contact(self):
        """
        Create Contact
        """
        self.env['res.partner'].create({
            'name': self.name,
        })
