# -*- coding: utf-8 -*-

from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    image = fields.Binary(string="Profile Photo")
    name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    blood_group = fields.Char(string="Blood_group")
    active = fields.Boolean(string="Active", default=True)
    pharmacy_line_ids = fields.One2many('patient.pharmacy.lines', 'patient_id', string='Pharmacy Lines')
    date = fields.Date(string="Date")
    attachments = fields.Binary(string="Documents", attachment=True)
    total= fields.Float(string="Total", compute="_compute_total", store="True")
    doctor_id = fields.Many2one('res.partner')
    # name = fields.Char(related='doctor_id.name')
    contact = fields.Char(related= 'doctor_id.mobile')
    email = fields.Char(related='doctor_id.email')

    @api.depends('pharmacy_line_ids.price_unit')
    def _compute_total(self):
        for line in self:
            for records in self.pharmacy_line_ids:
                line.total += records.price_unit

    def action_test(self):
        print("Button Clicked!!!!!!")

    @api.depends('pharmacy_line_ids.medicine_id')
    def onchange_object(self):
        for rec in self:
            rec.price_unit=self.pharmacy_line_ids.medicine_id

class PatientPharmacyLines(models.Model):
    _name = "patient.pharmacy.lines"
    _description = "Patient Pharmacy Lines"

    medicine_id = fields.Many2one('patient.medicines', string='Medicines')
    price_unit = fields.Float(string='Price')
    qty = fields.Integer(string='Quantity', default=1)
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    total = fields.Float(string='Total')



class Medicines(models.Model):
    _name = "patient.medicines"
    _description = "Patient Medicines"

    name = fields.Char(string='Medicines')
    list_price = fields.Integer(string='Price')
    expiry_date = fields.Date(string="Expiry Date")




