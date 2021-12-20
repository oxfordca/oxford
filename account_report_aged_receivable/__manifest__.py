# -*- coding: utf-8 -*-
{
    'name': "Personalización al Reporte Vencidas por Cobrar",

    'summary': """
        Nueva Columna (DÍAS DE EMISIÓN) y se modificó el Rango 
    """,

    'description': """
       Al lado derecho de la columna CUENTA, debe aparecer una columna (DÍAS DE
       EMISIÓN) que refleje los días transcurridos desde la emisión de la factura.
       - En los rangos presentes en el reporte, se deben incluir los rangos de 1-15
    """,

    'author': "Ing. Wilmer  Ibarra",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly ..
    'depends': ['base', 'account_reports'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],

    # only loaded in demonstration mode
    'demo': [

    ],
}
