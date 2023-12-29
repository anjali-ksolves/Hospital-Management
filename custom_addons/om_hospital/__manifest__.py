
{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Anjali',
    'summary': 'Hospital Management System',
    'description': """Hospital Management System""",
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/pharmacy.xml',
        'views/female_patient_view.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'sequence': -100,
}
