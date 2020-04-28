from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter

mapping = {
    'has_header': True,
    'is_split': False,
    'bank': 'Apple Card',
    'currency': 'USD',
    'delimiter': ',',
    'account': 'Apple Card',
    'account_type': 'CCard',
    'date_fmt': '%m/%d/%Y',
    'date': itemgetter('Transaction Date'),
    'amount': itemgetter('Amount (USD)'),
    'desc': itemgetter('Description'),
    'payee': itemgetter('Merchant'),
    'class': itemgetter('Category'),
    'id': itemgetter('Row'),
}
