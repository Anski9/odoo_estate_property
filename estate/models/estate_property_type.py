from odoo import models, fields, api

class EstatePropertyType(models.Model):  # Creating a new model for the real estate property types
    _name = 'estate.property.type'
    _description = 'Real estate property type'
    _order = 'sequence, name'

    name = fields.Char(string='Type', required=True)
    sequence = fields.Integer('Sequence', default=10)
    
    # One2many relation to the properties of this type
    property_ids = fields.One2many(
        'estate.property', 
        'property_type_id'
    )
    # One2many relation to the offers on properties of this type
    offer_ids = fields.One2many(
        'estate.property.offer', 
        'property_type_id',
        string='Offers'
    )
    # Computed field to store the number of offers on properties of this type
    offer_count = fields.Integer(
        string='Number of offers',
        compute='_compute_offer_count',
        store=True
    )
    # Compute the number of offers based on the offer_ids
    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    # SQL constraint to ensure the uniqueness of the type name
    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'The type name must be unique.')
    ]