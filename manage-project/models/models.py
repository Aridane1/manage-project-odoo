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
    @api.model
    def create(self, vals):
        new_record = super(empresa_contratadora, self).create(vals)
        self.env['registro.creacion.modificacion'].create({
            'creador_id': self.env.uid,
            'nombre_empresa': new_record.name,
            'tipo_accion': 'creacion',
        })
        return new_record

    def write(self, vals):
        result = super(empresa_contratadora, self).write(vals)
        for record in self:
            self.env['registro.creacion.modificacion'].create({
                'creador_id': self.env.uid,
                'nombre_empresa': record.name,
                'tipo_accion': 'modificacion',
            })
        return result


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
    class RegistroCreacionModificacion(models.Model):
        _name = 'registro.creacion.modificacion'
        _description = 'Registro de Creación y Modificación de Empresas'

        creador_id = fields.Many2one('res.users', string='Creado por', readonly=True)
        nombre_empresa = fields.Char(string='Nombre de la Empresa', readonly=True)
        fecha_hora_creacion = fields.Datetime(string='Fecha/Hora de Creación', default=fields.Datetime.now, readonly=True)
        tipo_accion = fields.Selection([('creacion', 'Creación'), ('modificacion', 'Modificación')], string='Tipo de Acción', readonly=True)


    # show_business_type = fields.Boolean(
    #     'Mostrar tipo de negocio',
    #     config_parameter='proyecto_javier.show_business_type',
    #     help="Casilla de verificación para mostrar/ocultar algunos campos en formularios y vistas"
    # )