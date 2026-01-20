from odoo import models, fields

class SaleOrderStockWarningWizard(models.TransientModel):
    _name = 'stock.pick.invoice'
    _description = 'stock invoice Wizard'

    picking_id = fields.Many2one(comodel_name='stock.picking', required=True)

    def action_create_invoice(self):
        invoice_lines=[]
        for line in self.picking_id.move_line_ids:
            invoice_lines.append((0,0,{
                'product_id':line.product_id.id,
                'name':line.product_id.name,
                'quantity':line.quantity
            }))
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.picking_id.partner_id.id,
            'invoice_origin': self.picking_id.name,
            'invoice_line_ids': invoice_lines,
        })
        return {'type': 'ir.actions.act_window',
                    'name': "Inv",
                    'res_model': 'account.move',
                    'view_mode': 'form',
                    'res_id': invoice.id,
                }

    def action_normal_validate(self):
        self.picking_id.validate_any_way()

