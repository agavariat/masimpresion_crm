# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import ValidationError

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
            ('5', 'Centros Comerciales'),
            ('6', 'Ferreteria y Depósitos'),
            ('7', 'Funerarias y Exequial'),
            ('8', 'Joyerias'),
            ('9', 'Propiedad Raiz'),
            ('10', 'Calzado y Confección'),
            ('11', 'Graficos, publicidad y servicios'),
            ('12', 'Quimicos'),
            ('13', 'Restaurantes, Bares y Discotecas'),
            ('14', 'Calzado y Confección'),
            ('15', 'Graficos, publicidad y servicios'),
            ('16', 'Educativo'),
            ('17', 'Restaurantes, Bares y Discotecas'),
            ('18', 'Seguridad y Vigilancia'),
            ('19', 'Automotriz'),
            ('20', 'Turismo'),
            ('21', 'Salud'),
            ('22', 'Logistica y Distribución'),
            ('23', 'Otros')

        ], "Sector",
    )
    client = fields.Selection(
        [
            ('1', 'Actual'),
            ('2', 'Prospecto'),
            ('3', 'otro'),
        ], "Clase de Cliente",
    )
    com = fields.Selection(
        [
            ('1', 'Asesor Comercial'),
            ('2', 'Facebook'),
            ('3', 'Instagram'),
            ('4', 'Web'),
            ('5', 'Google'),
            ('6', 'Refrerido'),
            ('7', 'Frio'),
            ('8', 'Base de Datos'),
            ('9', 'Otro'),
        ], "Como se contacto",
    )
class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'
    name = fields.Char('Linea de producto')

class SelectionField(models.Model):
    _inherit = 'res.partner'
    _name = 'select'
