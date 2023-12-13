# -*- coding: utf-8 -*-
# from odoo import http


# class Manage-project(http.Controller):
#     @http.route('/manage-project/manage-project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manage-project/manage-project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manage-project.listing', {
#             'root': '/manage-project/manage-project',
#             'objects': http.request.env['manage-project.manage-project'].search([]),
#         })

#     @http.route('/manage-project/manage-project/objects/<model("manage-project.manage-project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manage-project.object', {
#             'object': obj
#         })
