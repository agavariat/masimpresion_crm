# -*- coding: utf-8 -*-

from odoo import api, models, fields

class FirstNameLastName(models.Model):
    _inherit = 'res.partner'

    sec = fields.Char(string='Sector')
    tamemp = fields.Char(string='Tamaño empresa')

class modelo76inf(models.Models):
    _description  =  'Modelo para Manipular Many2many'
    _name  =  'modelo.many2many'

    como = fields.Many2many('model.many2many', string="Linea de producto")
