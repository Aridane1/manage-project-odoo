# -*- coding: utf-8 -*-

from odoo import models, fields, api

class empresa_contratadora(models.Model):
    _name = 'empresa_contratadora'
    _description = 'Empresas Contratadoras'

    name = fields.Char(string='Nombre', required=True)
    proyectos = fields.Many2many('project.project', string='Proyectos')
    cantidad_proyectos = fields.Integer(string='Número de Proyectos', compute='_compute_cantidad_proyectos')

    @api.depends('proyectos')
    def _compute_cantidad_proyectos(self):
        for empresa_contratadora in self:
            empresa_contratadora.cantidad_proyectos = len(empresa_contratadora.proyectos)


class ProjectProject(models.Model):
    _inherit = 'project.project'

    empresa_contratadora_id = fields.Many2one('empresa_contratadora', string='Empresa Contratadora')
    tasks_ids = fields.One2many('project.task', 'project_id', string='Tareas')

