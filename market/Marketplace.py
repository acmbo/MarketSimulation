# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:25:33 2019

@author: Stephan
"""

import pandas as pd
import numpy as np
import datetime
from market import Marketactor


        
class market:
    '''MarketClass Skript:

    Defines a market which Simulate a certain Time of Steps. Consist of Buyers and
    Sellers, which can trade with each other. '''
    def __init__(self, ListofBuyer, ListofSeller):
        self.ListofBuyer = ListofBuyer
        self.ListofSeller = ListofSeller
        self.MultipleSells = False
        self.Market_Metadata = pd.DataFrame(columns=['Time', 'Buyer', 'Seller','Count_Items','Price','Bid'])

    def listallBuyer(self):
        return(self.ListofBuyer)
    
    def listallSeller(self):
        return(self.ListofSeller)
        
    def Buy(self, Buyer, Seller, int_HowMuch, time):
        '''Buy function wich change the Data from Buyer and Trader according to the
        Attributes of the Buyfunction'''
        Buyer.account -= Seller.price * int_HowMuch
        Buyer.items += int_HowMuch
        Seller.items -= int_HowMuch
        Seller.account += Seller.price * int_HowMuch
        Metadata = {'Time':[time],
                    'Buyer':[Buyer.name],
                    'Seller':[Seller.name],
                    'Count_Items':[int_HowMuch],
                    'Price':[float(Seller.price)],
                    'Bid':[float(Buyer.bid)]
                    }
        df_meta = pd.DataFrame(Metadata)
        Buyer.UpdateMetaData(df_meta)
        Seller.UpdateMetaData(df_meta)

        self.Market_Metadata = self.Market_Metadata.append(df_meta)

        if self.MultipleSells == False:
            Buyer.desiretobuy = False
            Seller.desiretosell = False
        else:
            Buyer.evaluateToBuy()
            Seller.evaluateToSell()
        return()


    def GetPriceList(self,ListofSeller):
        '''Get Pricelist from all the Sellers on the market'''
        #Get Preislist. Bound to Order of the List
        PriceList = {}
        
        #erzeuge Preisliste 
        for Seller in ListofSeller:
            if Seller.desiretosell == True and Seller.items > 0:
                PriceList.update({Seller.name : Seller.price})
        return(PriceList)



    def AddRandomSeller(self,name1,upperlimit,lowerlimit,items):
        '''Adds  a Random Seller to the market'''
        self.ListofSeller.append(Marketactor.market_Seller(name = name1,
                                                           upperlimit = np.random.randint(lowerlimit,upperlimit+1),
                                                           lowerlimit = np.random.randint(0,lowerlimit),
                                                           account = 0,
                                                           items = items))

    def AddRandomBuyer(self,name1, upperlimit,lowerlimit,account):
        '''Adds  a Random Buyer to the market'''
        self.ListofBuyer.append(Marketactor.market_Buyer(name = name1,
                                                         upperlimit = np.random.randint(lowerlimit,upperlimit+1),
                                                         lowerlimit = np.random.randint(0,lowerlimit),
                                                         account = account,
                                                         items = 0))
    
    
        
      
    
    def SimulateIdealMarket(self,
                            LengthofSimulation,
                            wanteditems,
                            MultipleSells = False):
        '''
        LengthofSimulation - int - How many timesteps a Simulation has to go through 
        numbertransaktions - how many transaktions  have been made in the Simulation
        wanteditems - int - how many items are wanted by the buyers
        MultipleSells - Can a buyer go to multiple sellers?
        
        
        '''
        numbertransaktions = 0
           
        self.MultipleSells = MultipleSells
        
        starttime = datetime.datetime.now()
        print('Start of Simulation')
        print('Starttime: '+ str(starttime))
        print('Count of Sellers: '+str(len(self.ListofSeller)))
        print('Count of Buyers: '+str(len(self.ListofBuyer)))
        print('---')
        
        
            
        for time in range(1,LengthofSimulation):
            #Initialisierung Markt
            print('Round: ' + str(time))
            PriceList = self.GetPriceList(self.ListofSeller)
           
            for Seller in self.ListofSeller:
                Seller.GeneratePrice(time, DiscountIncreaseVal=0.1)
                Seller.items = Seller.items+3

            for Buyer in self.ListofBuyer:
                Buyer.GenerateBid(time, PriceList, DiscountIncreaseVal=0.05)
                Buyer.account = Buyer.account + 25

            #----Update Datatable of Classes
            for Buyer in self.ListofBuyer:
                Buyer.UpdateAttributeData(time)
            for Seller in self.ListofSeller:
                Seller.UpdateAttributeData(time)
                
            for y in range(0,len(self.ListofBuyer)):
            #-------------Look For price-------------------

                AlreadyChoosenSeller = [] # Variable to store already visited sellers for multiple buying

                while self.ListofBuyer[y].desiretobuy == True:

                    PriceList = self.GetPriceList(self.ListofSeller)

                    if not self.ListofBuyer[y].ChooseSeller_MinDistBid(PriceList) == None:
                        # Finde passenden Händler
                        ChosenSeller = self.ListofBuyer[y].ChooseSeller_MinDistBid(PriceList, wanteditems=wanteditems)

                        #print('SeenSellr: ', str(AlreadyChoosenSeller))

                        if not ChosenSeller == None and ChosenSeller not in AlreadyChoosenSeller:
                            #Finde Seller durch Namen
                            for x in range(0, len(self.ListofSeller)):
                                if ChosenSeller == self.ListofSeller[x].name:
                                    ChoosenSellerIndex = x

                            #Wenn Budget höher als Preis und noch der Händler was im Store hat->Kaufen
                            while self.ListofBuyer[y].desiretobuy == True:

                                if self.ListofBuyer[y].account >= self.ListofSeller[ChoosenSellerIndex].price * wanteditems and self.ListofSeller[ChoosenSellerIndex].items >= wanteditems:
                                    #Buy something
                                    self.Buy(self.ListofBuyer[y], self.ListofSeller[ChoosenSellerIndex], wanteditems, time=time)
                                    numbertransaktions += 1

                                    #Leave loop if only one buy is activated
                                    if MultipleSells == False:
                                        self.ListofBuyer[y].desiretobuy = False

                                else:
                                    # self.ListofBuyer[y].desiretobuy = False
                                    break

                        else:
                            self.ListofBuyer[y].desiretobuy = False

                        AlreadyChoosenSeller.append(ChosenSeller)

                    else:
                        #If no Seller found exit loop
                        self.ListofBuyer[y].desiretobuy = False
              
        endtime = datetime.datetime.now()
        
        print('End of Simulation')
        print('Endingtime: '+ str(endtime))
        delta = endtime - starttime
        print('Simulationtime '+ str(delta.seconds/60) +' mins' )
        print('Completed Transactions: '+str(numbertransaktions))
        print('Moved Money: '+ str(round(self.Market_Metadata['Price'].sum(),2)))
    
    


    
    


