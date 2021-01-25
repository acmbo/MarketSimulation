# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:09:57 2019

@author: Stephan
"""


import pandas as pd
import numpy as np
import random
 


class marketactor:
    '''Rudimental functions for actors

    Initialises marketactors with rudimental attributes.
    Every marketactor has an name, account, itemlist, upperlimit and lowerlimit
    the script is currency neutral. So you can add every kind of value to the
    Money or Value realted attributes


    Attributes:
        -Name - string
        -account - integer or float of how much an actor belongs to
        -items - integer of the stock of an certain item the actor has
        -upperlimit. Descripes the upperlimit of Price the actor accepts. Prices above
            the actor wont accept anymore and stops trading
        -lowerlimit. Same as upperlimit, just for a lowerlimit. Goes the price below the limit
            the trader stops trading

        Bove Limits work for buyer and seller
        Each actor stores metadata in an pandas dataframe, which can be called through a function

    '''
    def __init__(self, name, account, items, upperlimit, lowerlimit):
        self.name = name
        self.account = account
        self.items = items
        self.upperlimit = upperlimit
        self.lowerlimit = lowerlimit
        
        self.Metadata = pd.DataFrame(columns=['Time', 'Buyer', 'Seller','Count_Items','Price','Bid']) 
        
    def UpdateMetaData(self,df):  
        self.Metadata = self.Metadata.append(df)

    def Test(self):
        print('hi')
        
        
        

class market_Buyer(marketactor):
    '''Inherited Class from market actor'''
    
    def __init__(self, name, account, items, upperlimit, lowerlimit):
        '''the class can give out two kinds of Meta records.
        the first is the Data of the Buyer class itsself, the buyerclass
        the second is the Metadata of trading, which is aqquired through the course
        of participating in the market.
        '''

        marketactor.__init__(self, name, account, items, upperlimit, lowerlimit)
        
        self.bid = np.random.randint(self.lowerlimit, self.upperlimit+1) # Generate bid for a item
        self.desiretobuy = True # Does he like to buy thinks?
        #Dict for metadata
        dict_attr = {'Loop':[0],
                     'Name_Buyer': [self.name],
                     'Account': [self.account],
                     'Items': [self.items],
                     'Upper_Price_limit': [self.upperlimit],
                     'Lower_Price_limit': [self.lowerlimit],
                     'Bid':[self.bid]
                     }
        self.BuyerData = pd.DataFrame(dict_attr)
        


    def ChooseMinimumSeller(self, dict_PriceList,wanteditems=1):
        '''Function for Choosing a seller from the Price list. This function just chooses
        a price by looking if its the lowest price available'''
        #Seller nach kleinsten Preis wählen
        MinPreis = min(list(dict_PriceList.values())*wanteditems)
        NameSellerMinPreis = list(dict_PriceList.keys())[list(dict_PriceList.values()).index(MinPreis)]
        return(NameSellerMinPreis)
        
        

    def ChooseSeller_MinDistBid(self,dict_PriceList,wanteditems=1):
        ''' Function for choosing a price by evaluating the difference between a bid from the
        buyer and the price of the seller. It gets the bid of the buyer and chooses the
        price fromthe pricelist with the smallest difference'''
        #Seller wird durch die Kleinste Distantz zum Bid gewählt
        
        List_prices = list(dict_PriceList.values())*wanteditems
        List_prices_checked = []
        
        for x in range(0,len(List_prices)):
            List_prices_checked.append(abs(List_prices[x]-self.bid))
        
        ChoosenPreis = List_prices_checked.index(min(List_prices_checked))
        ChoosenPreis = List_prices[ChoosenPreis]
        
        NameSellerChoosenPreis = list(dict_PriceList.keys())[list(dict_PriceList.values()).index(ChoosenPreis)]
        return(NameSellerChoosenPreis)
        
        

    def ChooseSeller(self, dict_PriceList, randomOrd = False, wanteditems=1):
        '''Function for chosing a price from the difference to the bid. It also checks,
        if the price is within the Bounds of a Boundry. The order, in which
        the price is evaluatetd can be random, there choose randomOrd = true.

        This funcion over a second function, within_boundry. here you can give a second
        boarder, which a price can be, to be sean as possible target. It evaluates
        if a price is within a certain range to the bid (WithinBoundries). So not just
        the nearest price to the bid is choosen, but you can say if a buyer can neither accept
        a price or decline, thus not in his scope if price range'''

        #Filtern welcher Preis in einer Bestimmten Entfernung zum Bid ist. Hier immer 
        # die Hälfte der Differenz zwischen den Grenzen und dem Aktuellen bid.
        def within_Boundries(actor, wanteditems):
            if dict_PriceList[actor] * wanteditems <= (self.upperlimit-(self.upperlimit-self.bid)/2) and dict_PriceList[actor] * wanteditems >= (self.lowerlimit+(self.bid-self.lowerlimit)/2):
                return dict_PriceList[actor]
        #Gibt Liste mit Namen der Gefilterten Preise raus
        PriceswithinBound = list(filter(lambda x: within_Boundries(x, wanteditems), dict_PriceList.keys()))
        
        #Erzeuge mit Namenliste neue Dict mit den Preisen im Filter
        new_dict_PriceList ={}
        
        for names in PriceswithinBound:
             new_dict_PriceList[names] = dict_PriceList[names] * wanteditems
        
        if len(new_dict_PriceList)==0:
            return(None)
        else:
            #Hier wird geguckt, welcher Preis die kleinste Distanz zum Bid hat.
            List_prices = list(new_dict_PriceList.values())
            List_prices_checked = []
            
            #Should be the orde of the price evaluation be random?
            if randomOrd == True:
                range1 = random.sample(range(0,len(List_prices)), len(List_prices))
                for x in range1:
                    List_prices_checked.append(abs(List_prices[x]-self.bid*wanteditems))
            else:
                for x in range(0,len(List_prices)):
                    List_prices_checked.append(abs(List_prices[x]-self.bid*wanteditems))
            
            ChoosenPreis = List_prices_checked.index(min(List_prices_checked))
            ChoosenPreis = List_prices[ChoosenPreis]
            
            NameSellerChoosenPreis = list(new_dict_PriceList.keys())[list(new_dict_PriceList.values()).index(ChoosenPreis)]
            return(NameSellerChoosenPreis)
    
        

      
    def GenerateBid(self, Loop, dict_PriceList, DiscountIncreaseVal=0.01):
        '''Function for generating a bid. The bid is first generated randomly in
        the generation of the class, then here it will get a rise, when a buyer coudnt
        make a transaction. If he makes a transaction he makes the bid lower, (because
        he wants a cheaper deal'''

        self.desiretobuy = True
        
        Sellcounts = len(self.Metadata[self.Metadata.Time == Loop-1])
        ##if he has a made asel reduce the next bid
        if Sellcounts > 0:
            bed = self.bid - self.bid*DiscountIncreaseVal
            if not bed < self.lowerlimit:
              self.bid -= self.bid*DiscountIncreaseVal
        
        ### if he didnt made a sell, rise or lower bid accordingly
        ### if his bid is way to low, the price needs to be raised!
        ### if his bid is way to high, the price needs to be lowerd           
        if Sellcounts ==0:
            MinPreis = min(dict_PriceList.values())
            MaxPreis = min(dict_PriceList.values())
            
            if self.bid > MaxPreis:
                bed = self.bid - self.bid*DiscountIncreaseVal
                if not bed < self.lowerlimit:
                    self.bid -= self.bid*DiscountIncreaseVal
                    
            if self.bid < MinPreis:
                bed = self.bid + self.bid*DiscountIncreaseVal
                if not bed > self.upperlimit:
                    self.bid += self.bid*DiscountIncreaseVal
        
    def evaluateToBuy(self):
        ''' Simple Function for evaluating, if Buyer want to buy.Compares current bid with availbe Money in account'''
        if self.account - self.bid > 0:
            self.desiretobuy = True
        else:
            self.desiretobuy = False


    def UpdateAttributeData(self, Loop):
        '''Update meta data'''
        dict_attr = {'Loop':[Loop],
                     'Name_Buyer': [self.name],
                     'Account': [self.account],
                     'Items': [self.items],
                     'Upper_Price_limit': [self.upperlimit],
                     'Lower_Price_limit': [self.lowerlimit],
                     'Bid': [self.bid]
                     }
        self.BuyerData = self.BuyerData.append(pd.DataFrame(dict_attr))

    


class market_Seller(marketactor):
    '''Sellerclass. inherited from marketactor'''

    def __init__(self, name, account, items, upperlimit, lowerlimit):
        '''Sameprincipal as buyer class, if he makes a sell,try to raise the price,
        else lower it'''

        marketactor.__init__(self, name, account, items, upperlimit, lowerlimit)
        
        self.desiretosell = True
        self.price = np.random.randint(self.lowerlimit, self.upperlimit+1)
        
        dict_attr = {'Loop':[0],
                     'Name_Seller': [self.name],
                     'Account': [self.account],
                     'Items': [self.items],
                     'Price':[self.price],
                     'Upper_Price_limit': [self.upperlimit],
                     'Lower_Price_limit': [self.lowerlimit]        
                     }
        self.SellerData = pd.DataFrame(dict_attr)
        

    
    def GeneratePrice(self, Loop, DiscountIncreaseVal= 0.01):

        self.desiretosell = True
        Sellcounts = len(self.Metadata[self.Metadata.Time == Loop-1])
        if Sellcounts > 0:
            bed = self.price + self.price*DiscountIncreaseVal
            if not bed > self.upperlimit:
              self.price += self.price*DiscountIncreaseVal
              
        if Sellcounts ==0:
            bed = self.price - self.price*DiscountIncreaseVal
            if not bed < self.lowerlimit:
                self.price -= self.price*DiscountIncreaseVal

    def evaluateToSell(self):
        ''' Simple Function for evaluating, if Seller want to sell. Checks current amount items for selling. '''
        if self.items > 0:
            self.desiretosell = True
        else:
            self.desiretosell = False

    def UpdateAttributeData(self, Loop):
        '''Update Metadata'''
        dict_attr = {'Loop':[Loop],
                     'Name_Seller': [self.name],
                     'Account': [self.account],
                     'Items': [self.items],
                     'Price':[self.price],
                     'Upper_Price_limit': [self.upperlimit],
                     'Lower_Price_limit': [self.lowerlimit]
                     }
        self.SellerData = self.SellerData.append(pd.DataFrame(dict_attr))