# -*- coding: utf-8 -*-

from odoo import models, fields, api

class empresa_contratadora(models.Model):
    _name = 'empresa_contratadora'
    _description = 'Empresas Contratadoras'

    name = fields.Char(string='Nombre', required=True)
    proyectos = fields.Many2many('project.project', string='Proyectos')
    country_place = fields.Char(string="País", readonly=True, default=lambda self: self.env['ir.config_parameter'].sudo().get_param('employee_contract.country_place'))
    cantidad_proyectos = fields.Integer(string='Número de Proyectos', compute='_compute_cantidad_proyectos')
    show_country_field = fields.Boolean(compute='_compute_show_country_field', store=False)
    
    @api.depends('name') 
    def _compute_show_country_field(self):
        self.show_country_field = self.env['ir.config_parameter'].sudo().get_param('empresa_contratadora.show_country_place') == 'True'
    
    @api.depends('proyectos')
    def _compute_cantidad_proyectos(self):
        for empresa_contratadora in self:
            empresa_contratadora.cantidad_proyectos = len(empresa_contratadora.proyectos)


class ProjectProject(models.Model):
    _inherit = 'project.project'

    empresa_contratadora_id = fields.Many2one('empresa_contratadora', string='Empresa Contratadora')
    tasks_ids = fields.One2many('project.task', 'project_id', string='Tareas')
    country_place = fields.Char(related='empresa_contratadora_id.country_place', string="País", readonly=True)
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    country_place = fields.Selection(
        [('Chiquitistan', 'Chiquitistan'), ('Islandia', 'Islandia'), ('España', 'España')],
        string="Sede pais",
        config_parameter='employee_contract.country_place',
        help="Selecciona el código telefónico del país"
    )
    show_country_place = fields.Boolean(
        string="Mostrar campo País",
        config_parameter='empresa_contratadora.show_country_place',
    )

    # show_business_type = fields.Boolean(
    #     'Mostrar tipo de negocio',
    #     config_parameter='proyecto_javier.show_business_type',
    #     help="Casilla de verificación para mostrar/ocultar algunos campos en formularios y vistas"
    # )