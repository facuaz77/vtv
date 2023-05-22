# -*- coding: utf-8 -*-




# class vtv(models.Model):
#     _name = 'vtv.vtv'
#     _description = 'vtv.vtv'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class recepcion(models.Model):
    _name = 'vtv.recepcion'
    _description = 'Aqui se tomara el turno, patente y el nombre del titular'
    
    name2 = fields.Char(string='Matricula', size=6, required=True )
    name = fields.Char(string='Nombre del titular', required=True)
    Nro_de_turno = fields.Integer(string='Numero de turno', size=3, required=True)
    fecha = fields.Date(string='Fecha del turno', required=True)
    
    
    recepcion_ids = fields.One2many('vtv.auto','recepcion_id', string='Autos',required=True)
    
    
 #Relaciones entre tablas
      
 
    
    
class auto(models.Model):
    _name = 'vtv.auto'
    _description = 'Se evalua las condiciones del auto'
    _order = 'name'
    
    name = fields.Char(string='Matricula', size=6, required=True )
    marca = fields.Char(string='Marca del auto', required=True)
    modelo = fields.Selection(selection='_get_modelo_options', string='Modelo', required=True)
    years = fields.Integer(string="Años del auto", compute='_compute_years', store=True)
    primera_seccion = fields.Selection(string='Primera seccion', selection=[('a','Aprobado'),('d','Desaprobado')],required=True)
    segunda_seccion= fields.Selection(string='Segunda seccion', selection=[('a','Aprobado'),('d','Desaprobado')], required=True)
    tercera_seccion= fields.Selection(string='Ultima seccion', selection=[('a','Aprobado'),('d','Desaprobado')], required=True)
    descripcion = fields.Text('Detalles a dar')
    
    recepcion_id = fields.Many2one('vtv.recepcion', string='Recepcion')
    
    
    #Aca se calcula los años que tiene el auto desde el año de su modelo
    @staticmethod
    def _get_modelo_options():
        current_year = date.today().year
        modelo_options = []
        for year in range(1950, current_year + 1):
            modelo_options.append((str(year), str(year)))
        return modelo_options
    
    
    @api.depends('modelo')
    def _compute_years(self):
        for auto in self:
            if auto.modelo:
                current_year = date.today().year
                auto.years = current_year - int(auto.modelo)
            else:
                auto.years = 0
    


#Relaciones entre tablas

    resultado_ids = fields.Many2many('vtv.resultados', string='Resultados',required=True)



    
class resultados(models.Model):
    
    _name = 'vtv.resultados'
    _description = 'Resultados del auto para verificar si esta apto para circular en via publica'
    order = 'fecha'
    #Con la matricula identificamos al usuario
    name3 = fields.Char(string='Matricula', size=6, required=True )
    fecha_De_realizacion = fields.Date(string='Fecha de la realizacion',required=True, default= fields.date.today(), help='Aqui pondras la fecha en la que se aprobo el auto')
    aprobado = fields.Selection(string='¿Esta apto?', selection=[('s','Si'),('n','No')],required=True)
    resultado = fields.Boolean(string='Marcar si tiene que volver' )
    resultado2 = fields.Boolean(string='Marcar si no tiene que volver')
    descripcion2 = fields.Text(string='Detalles a dar')
    
    
    
    
#Relaciones entre tablas

    auto_ids = fields.Many2many('vtv.auto',string='Autos',required=True)