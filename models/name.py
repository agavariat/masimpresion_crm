# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import ValidationError

class FirstNameLastName(models.Model):
    _inherit = 'res.partner'

    tamemp = fields.Selection(
        [
            ('1', '3 veces por semana'),
            ('2', '2 veces por mes'),
            ('3', '1 vez por mes'),
            ('4', '1 vez cada 2 meses'),
            ('5', '1 vez cada 6 meses'),
            ('6', '1 vez vez al año'),
            ('7', '2 veces vez al año'),
            ('8', '1 vez cada 2 años'),
            ('7', 'Ocacional'),
        ], "Frecuencia de recoleccion",
    )
    u_reco = fields.Date()
