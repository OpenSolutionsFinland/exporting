from osv import fields, osv

class product_extension(osv.osv):
	_name='product.product'
	_inherit='product.product'
	_columns= {
		'x_quality_check': fields.text('Quality check text'),
	}

product_extension()

