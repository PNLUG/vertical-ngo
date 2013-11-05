from datetime import timedelta
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
import openerp.tests.common as test_common
from .common import BaseAgreementTestMixin


class TestAgreementPriceList(test_common.TransactionCase, BaseAgreementTestMixin):
    """Test observer on change and purchase order on chnage"""

    def setUp(self):
        """ Create a default agreement
        with 3 price line
        qty 0  price 70
        qty 200 price 60
        qty 500 price 50
        qty 1000 price 45
        """
        super(TestAgreementPriceList, self).setUp()
        self.commonsetUp()
        cr, uid = self.cr, self.uid
        start_date = self.now + timedelta(days=10)
        start_date = start_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        end_date = self.now + timedelta(days=20)
        end_date = end_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        agr_id = self.agreement_model.create(cr, uid,
                                             {'supplier_id': self.supplier_id,
                                              'product_id': self.product_id,
                                              'start_date': start_date,
                                              'end_date': end_date,
                                              'delay': 5,
                                              'quantity': 1500})
        self.agreement_line_model.create(cr, uid,
                                         {'framework_agreement_id': agr_id,
                                          'quantity': 0,
                                          'price': 70.0})
        self.agreement_line_model.create(cr, uid,
                                         {'framework_agreement_id': agr_id,
                                          'quantity': 200,
                                          'price': 60.0})
        self.agreement_line_model.create(cr, uid,
                                         {'framework_agreement_id': agr_id,
                                          'quantity': 500,
                                          'price': 50.0})
        self.agreement_line_model.create(cr, uid,
                                         {'framework_agreement_id': agr_id,
                                          'quantity': 1000,
                                          'price': 45.0})
        self.agreement = self.agreement_model.browse(cr, uid, agr_id)

    def test_00_test_qty(self):
        """Test if barem retrival is correct"""
        self.assertEqual(self.agreement.get_price(0), 70.0)
        self.assertEqual(self.agreement.get_price(100), 70.0)
        self.assertEqual(self.agreement.get_price(200), 60.0)
        self.assertEqual(self.agreement.get_price(210), 60.0)
        self.assertEqual(self.agreement.get_price(500), 50.0)
        self.assertEqual(self.agreement.get_price(800), 50.0)
        self.assertEqual(self.agreement.get_price(999), 50.0)
        self.assertEqual(self.agreement.get_price(1000), 45.0)
        self.assertEqual(self.agreement.get_price(10000), 45.0)
        self.assertEqual(self.agreement.get_price(-10), 70.0)
