from osv import fields, osv
from openerp.tools.translate import _

class invoice_extension_intrastat(osv.osv):
	_name='account.invoice'
	_inherit='account.invoice'
    
	_columns= {
		'transaction_type': fields.selection((('11', _('Procurement/Sale')), ('12', _('Sample')), ('14', _('Leasing')), ('19', _('Other')), ('21', _('Return')), ('22', _('Replacement')), ('60', _('Repair'))), 'Transaction Type', required=False),
        'transportation_method': fields.selection((('1', _('Sea')), ('2', _('Train')), ('3', _('Road')), ('4', _('Air')), ('5', _('Mail')), ('7', _('Static')), ('8', _('Freshwater')), ('9', _('Self transporting'))), 'Transportation Method', required=False)
	}

invoice_extension_intrastat()