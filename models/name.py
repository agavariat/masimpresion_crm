# -*- coding: utf-8 -*-

from odoo import api, models, fields

class FirstNameLastName(models.Model):
    _inherit = 'res.partner'

    
    sec = fields.Selection(
        [
            ('1', 'Almacenes por Departamento'),
            ('2', 'Belleza y Cosmeticas'),

        ], "Sector",
    )
    com = fields.Selection(
        [
            ('1', 'FaceBook'),
            ('2', 'Acesor Comercial'),
        ], "Sector",
    )
    tip = fields.Selection(
        [
            ('1', 'Actual'),
            ('2', 'Prospecto'),
            ('3', 'Otro'),
        ], "Sector",
    )
    tamemp = fields.Char(string='Tamaño empresa')
    linea = fields.Many2many('model.manipulate.many2many', string="Linea de producto")

class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'

    name = fields.Char('linea1')
    field_sec = fields.Selection([('almacenes_por_departamento', 'Almacenes por Departamento'),('belleza_cosmeticas', 'Belleza y Cosmeticas')])