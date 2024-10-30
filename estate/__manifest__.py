{
    'name': 'Estate Module',
    'summary': 'A module for managing real estate properties',
    'category': 'Real Estate',
    'author': 'Anski9',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_kanban_view.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_resusers_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
}