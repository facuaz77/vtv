# -*- coding: utf-8 -*-
{
    'name': "VTV",

    'summary': """
        Verificacion Tecnica Vehicular""",

    'description': """
        Modulo diseñado para registrar los vehiculos que esten aptos para circular en la via publica
    """,

    'author': "Facundo Alaniz",
    'website': "https://buenosaires.gob.ar/tramites/verificacion-tecnica-vehicular-obligatoria",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/vtv_security.xml',
         'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    
    'application': [
        True
        ],
}