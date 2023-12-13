# -*- coding: utf-8 -*-
{
    'name': "manage-project",

    'summary': """
        Módulo de gestión de proyectos""",

    'description': """
        Gestión de los proyectos de tu empresa
    """,

    'author': "Aridane",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'reports/empresas_report.xml',
        'reports/empresas_report_view.xml',
        'data/project_category_state.xml'
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'application':'True',

    'assets':{
        'web.assets_common':[
            'manage-project/static/src/scss/style1.scss',
        ],
    }
}
