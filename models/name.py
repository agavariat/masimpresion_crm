# -*- coding: utf-8 -*-

from odoo import api, models, fields

class FirstNameLastName(models.Model):
    _inherit = 'res.partner'

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
     como = fields.Selection(
            [
                ('1', 'Asesor Comercial'),
                ('2', 'Facebook'),
                ('3', 'Instagram'),
                ('4', 'Web'),
            ], "Como se Contacto",
        )
    ccli = fields.Selection(
            [
                ('1', 'Actual'),
                ('2', 'Prospecto'),
                ('3', 'otro'),
            ], "Como se Contacto",
        )

class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'
    name = fields.Char('Linea de producto')

class SelectionField(models.Model):
    _inherit = 'res.partner'
    _name = 'select'

class Selection1Field(models.Model):
    _inherit = 'res.partner'
    _name = 'select1'