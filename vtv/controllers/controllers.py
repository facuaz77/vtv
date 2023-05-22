# -*- coding: utf-8 -*-
# from odoo import http


# class Vtv(http.Controller):
#     @http.route('/vtv/vtv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vtv/vtv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vtv.listing', {
#             'root': '/vtv/vtv',
#             'objects': http.request.env['vtv.vtv'].search([]),
#         })

#     @http.route('/vtv/vtv/objects/<model("vtv.vtv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vtv.object', {
#             'object': obj
#         })
