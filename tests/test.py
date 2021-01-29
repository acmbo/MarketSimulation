import unittest
import pandas as pd

from market.Marketactor import marketactor, market_Buyer, market_Seller

class TestActors(unittest.TestCase):

    def test_is_actor(self):
    
        for obj in [marketactor, market_Buyer, market_Seller]:
        
            print('Testing Object: ', str(obj))
            object = obj(name='test', account=1, items=1, upperlimit=2, lowerlimit=0)
            
            # error message in case if test case got failed 
            message = "given object is not instance of {s}.".format(s = str(obj))
            
            self.assertIsInstance(object, marketactor, message)
            
            message = "given attribute of {s}. is wrong".format(s = str(object))
            
            # Test attributes of object
            self.assertEqual(object.name, "test", message)
            self.assertEqual(object.account, 1, message)
            self.assertEqual(object.items,1, message)
            self.assertEqual(object.upperlimit, 2, message)
            self.assertEqual(object.lowerlimit, 0, message)
            
            if isinstance(object, market_Buyer):
                self.assertTrue(object.desiretobuy, message)
            if isinstance(object, market_Seller):
                self.assertTrue(object.desiretosell, message)
            

            
            
    def test_Buyer_functions(self):
        
        pricedic= {'Seller A':0.5,
                   'Seller B':1,
                   'Seller C':0.2,
        }
        
        object = market_Buyer(name='tester', account=1, items=1, upperlimit=2, lowerlimit=0)
        
        # Test choosing price functions
        result = object.ChooseMinimumSeller(pricedic,wanteditems=1)
        message = "Buyer choose wrong Seller( {s} ) for ChooseMinimumSeller()".format(s=result)
        self.assertEqual(result, "Seller C", message)
        
        object.bid = 0.6
        result = object.ChooseSeller_MinDistBid(pricedic,wanteditems=1)
        message = "Buyer choose wrong Seller( {s} ) for ChooseMinimumSeller()".format(s=result)
        self.assertEqual(result, "Seller A", message)

        object.bid = 0.3
        object.lowerlimit = 0.25
        result = object.ChooseSeller(pricedic,wanteditems=1)
        message = "Buyer choose wrong Seller( {s} ) for ChooseMinimumSeller()".format(s=result)
        self.assertEqual(result, "Seller A", message)
        
        # check if actor can asign right decision to buy
        object.account=0
        object.bid=1
        object.evaluateToBuy()
        result = object.desiretobuy
        message = "Buyer shouldnt be able to buy".format(s=result)
        self.assertFalse(result, message)

        
        
        
    def test_Seller_functions(self):
        
        object = market_Seller(name='tester', account=1, items=1, upperlimit=2, lowerlimit=0)
        lastSell = {'Time':[2,1, 0], 'Price':[1,1, 1]}
        object.Metadata = pd.DataFrame().from_dict(lastSell)
        
        # check generating right bid
        # Here he should higher his price because he selled in Timepoint 0 one item
        object.price = 1
        objoldprice= object.price
        DiscountIncreaseVal= 0.01
        #print(len(object.Metadata[object.Metadata.Time == 4-1]))
        object.GeneratePrice(Loop=1,DiscountIncreaseVal= DiscountIncreaseVal)
        result = object.price
        message = "Seller calcualted wrong bid ( {s} ) ".format(s=result)
        self.assertEqual(result, objoldprice*(1+DiscountIncreaseVal), message)

        
        # Here he should bid lower, because on Timepoint 4 ( bzw. 5-1) doesnt exist an sell entry
        object.price = 1
        objoldprice= object.price
        DiscountIncreaseVal= 0.01
        object.GeneratePrice(Loop=5,DiscountIncreaseVal= DiscountIncreaseVal)
        result = object.price
        message = "Seller calcualted wrong bid ( {s} ) ".format(s=result)
        self.assertEqual(result, objoldprice*(1-DiscountIncreaseVal), message)
        
        # Check for actor to access correctly to not sell
        object.items=0
        object.evaluateToSell()
        result = object.desiretosell
        message = "Seller shouldnt be able to sell"
        self.assertFalse(result, message)
        
        
if __name__ == '__main__':
    unittest.main()
