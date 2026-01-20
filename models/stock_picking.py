from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        res=super().button_validate()
        if isinstance(res,dict):
            return res
            print('res')
        if not self.sale_id:
            return {'type': 'ir.actions.act_window',
                    'name': "insufficien Stocl",
                    'res_model': 'stock.pick.invoice',
                    'view_mode': 'form',
                    'target': 'new',
                    'context': {
                        'default_picking_id': self.id,
                    }
                }
        return res

    def validate_any_way(self):
        res=super().button_validate()
        print("AA",res)
        return super().button_validate()
