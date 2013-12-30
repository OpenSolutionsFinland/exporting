from osv import fields, osv

class product_extension(osv.osv):
	_name='product.product'
	_inherit='product.product'
	_columns= {
		'customs_code': fields.text('Customs code'),
        'country_of_origin': fields.many2one('res.country','Country of Origin')
	}

product_extension()

