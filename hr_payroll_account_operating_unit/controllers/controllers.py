# -*- coding: utf-8 -*-
# from odoo import http


# class HrPayrollAccountOperatingUnit(http.Controller):
#     @http.route('/hr_payroll_account_operating_unit/hr_payroll_account_operating_unit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_payroll_account_operating_unit/hr_payroll_account_operating_unit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_payroll_account_operating_unit.listing', {
#             'root': '/hr_payroll_account_operating_unit/hr_payroll_account_operating_unit',
#             'objects': http.request.env['hr_payroll_account_operating_unit.hr_payroll_account_operating_unit'].search([]),
#         })

#     @http.route('/hr_payroll_account_operating_unit/hr_payroll_account_operating_unit/objects/<model("hr_payroll_account_operating_unit.hr_payroll_account_operating_unit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_payroll_account_operating_unit.object', {
#             'object': obj
#         })
