# -*- coding: utf-8 -*-

from odoo import api, models, fields

class FirstNameLastName(models.Model):
    _inherit = 'res.partner'

    tamemp = fields.Char(string='Tamaño empresa')
    linea = fields.Many2many('model.manipulate.many2many', string="Linea de producto")
    field_sec = fields.Selection([('almacenes_por_departamento', 'Almacenes por Departamento'),('belleza_cosmeticas', 'Belleza y Cosmeticas')])

class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'

    name = fields.Char('linea1')
    field_sec = fields.Selection([('almacenes_por_departamento', 'Almacenes por Departamento'),('belleza_cosmeticas', 'Belleza y Cosmeticas')])