# -*- coding: utf-8 -*-

from odoo import api, models, fields

class FirstNameLastName(models.Model):
    _inherit = 'res.partner'

    sec = fields.Char(string='Sector')
    tamemp = fields.Char(string='Tamaño empresa')

class SeveralFields(models.Model):
    _inherit = 'res.partner'
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'

    como = fields.Many2many('model.manipulate.many2many', string="Linea de producto")
