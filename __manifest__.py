# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2018-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Tintuk Tomin(<https://www.cybrosys.com>)
#    you can modify it under the terms of the GNU AGPL (v3), Version 3.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AGPL (AGPL v3) for more details.
#
##############################################################################

{
    'name': 'Campos mas impresion',
    'version': '12.0.1.0.0',
    'summary': """este modulo agregas campos de personalizacion para masimpresion.""",
    'description': "",
    'category': "Human Resource",
    'author': 'Andres Gaviria',
    'company': 'Intresco S.A.S',
    'website': "https://www.intresco.co",
    'depends': ['base','contacts'],
    'data': [
             'views/name_view.xml'
             'data/severalfields.xml'
             ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
