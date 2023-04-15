# Import Package
from ecommerce.sales import calc_shipping, calc_tax
from ecommerce import sales

# Import Sub Package
from ecommerce.sub_pack import other_sales

"""
# Absolute Import
from ecommerce.customer import contact
# Relative Import
from ..customer import contact
"""

calc_shipping()
calc_tax()

# For debugging we can use
print(dir(sales))
