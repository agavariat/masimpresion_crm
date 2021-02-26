# -*- coding: utf-8 -*-

from odoo import api, models, fields

class FirstNameLastName(models.Model):
    _inherit = 'res.partner'

    tamemp = fields.Char(string='Tamaño empresa')
    linea = fields.Many2many('model.manipulate.many2many', string="Linea de producto")

class SeveralFields(models.Model):
    _description = 'Modelo para Manipular Many2many'
    _name = 'model.manipulate.many2many'

    name = fields.Char('linea1')

class SelectionField(models.Model):
    _inherit = 'res.partner'
    _name = 'select'

    sec = fields.Selection(
        [
            ('si', 'Si'),
            ('no', 'No'),

        ], "ACEPTA ENTREGARLE A UNIMINUTO LOS DATOS GENERALES SUYOS Y DEL MICRONEGOCIO CON FINES ACADÉMICOS",
    )