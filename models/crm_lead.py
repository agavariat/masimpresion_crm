# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import ValidationError

class lead(models.Model):
    _inherit = "crm.lead"

    tamemp = fields.Selection(
        [
            ('1', 'Grande'),
            ('2', 'Mediana'),
            ('3', 'Pequeña'),
            ('4', 'Empresa Personal'),
        ], "Tamaño de Empresa",
    )
    linea = fields.Many2many('model.manipulate.many2many', string="Linea de producto")
    sec = fields.Selection(
        [
            ('1', 'Almacenes por Departamento'),
            ('2', 'Belleza y Cosmeticas'),
            ('3', 'Alimentos'),
            ('4', 'Bebidas'),
        ], "Sector",
    )
    client = fields.Selection(
        [
            ('1', 'Almacenes por Departamento'),
            ('2', 'Belleza y Cosmeticas'),
            ('3', 'Alimentos'),
            ('4', 'Bebidas'),
        ], "Clase de Cliente",
    )
    com = fields.Selection(
        [
            ('1', 'Almacenes por Departamento'),
            ('2', 'Belleza y Cosmeticas'),
            ('3', 'Alimentos'),
            ('4', 'Bebidas'),
        ], "Como se contacto",
    )