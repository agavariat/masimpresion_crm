# -*- coding: utf-8 -*-

from odoo import api, models, fields

class FirstNameLastName(models.Model):
    _inherit = 'res.partner'

    tamemp = fields.Char(string='Tamaño empresa')
    linea = fields.Many2many('model.manipulate.many2many', string="Linea de producto")
    sec = fields.Selection(
            [
                ('1', 'Almacenes por Departamento'),
                ('2', 'Belleza y Cosmeticas'),
                ('3', 'Alimentos'),
                ('4', 'Bebidas'),
            ], "Sector",
        )

class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'
    name = fields.Char('Linea de producto')

class SelectionField(models.Model):
    _inherit = 'res.partner'
    _name = 'select'