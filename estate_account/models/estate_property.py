from odoo import models, Command

class EstateProperty(models.Model):
    _inherit = 'estate.property'  # Inheriting from the 'estate.property' model to extend its functionality

    def action_sold(self):
        super(EstateProperty, self).action_sold()  # Call the parent method to mark the property as sold

        # Create an invoice for the buyer
        invoice = self.env['account.move'].create({
            'partner_id': self.buyer_id.id,  # Set the buyer as the invoice partner
            'move_type': 'out_invoice',  # Specify the invoice type as customer invoice
            'invoice_line_ids': [
                Command.create({
                    'name': 'Service fee (6% of selling price)',
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06,  # Calculate the service fee as 6% of the selling price
                }),
                Command.create({
                    'name': 'Administrative fees',
                    'quantity': 1,
                    'price_unit': 100.00,  # Fixed administrative fee
                }),
            ],
        })