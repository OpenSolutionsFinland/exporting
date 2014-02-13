from osv import fields, osv
from openerp.tools.translate import _

class invoice_extension_intrastat(osv.osv):
	_name='account.invoice'
	_inherit='account.invoice'
    
	_columns= {
		'transaction_type': fields.selection((('0', _('Procurement/Sale')), ('1', _('Sample')), ('2', _('Leasing')), ('3', _('Other')), ('4', _('Return')), ('5', _('Replacement')), ('6', _('Repair'))), 'Transaction Type', required=False),
        'transportation_method': fields.selection((('0', _('Sea')), ('1', _('Train')), ('2', _('Road')), ('3', _('Air')), ('4', _('Mail')), ('5', _('Static')), ('6', _('Freshwater')), ('7', _('Self transporting'))), 'Transportation Method', required=False)
	}

invoice_extension_intrastat()