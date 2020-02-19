# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:09:52 2019

@author: Stephan
"""


import os
os.chdir('C:\\Users\\Stephan\\Desktop\\Arbeit\\Arbeit\\MarketSimulation')
import MarketVisualization as mv
import Marketv0_3 as Market
import Marketactor
#####################################Skript#################################


    

ListofBuyer = [Marketactor.market_Buyer(upperlimit = 15,
                     lowerlimit = 5,
                     name = 'John',
                     account = 1000,
                     items = 0),
                Marketactor.market_Buyer(upperlimit = 25,
                                 lowerlimit = 10,
                                 name = 'Terry',
                                 account = 1000,
                                 items = 0)]
                
ListofSeller = [Marketactor.market_Seller(name = 'Boris', 
                       upperlimit = 23,
                       lowerlimit = 13,
                       account = 0,
                       items = 100),
                Marketactor.market_Seller(name = 'Tony', 
                           upperlimit = 30,
                           lowerlimit = 10,
                           account = 0,
                           items = 100)]




market = Market.market(ListofBuyer,ListofSeller)

RandomSeller = 30
RandomBuyer = 50

for count in range(0,RandomSeller):
    market.AddRandomSeller('RandomSeller_' + str(count),50,10)

for count in range(0,RandomBuyer):
    market.AddRandomBuyer('RandomBuyer_' + str(count),50,10)   

market.SimulateIdealMarket(LengthofSimulation = 1000,
                            wanteditems = 1,
                            MultipleSells = False)


mv.AllPricesSeller(market)
mv.BuyerData(market)
mv.ActorPerformance(market)
mv.BidRande(market)
mv.BuyerBidandAccount(market)
mv.SellerPriceandAccount(market)
mv.MeanPriceBid(market)
mv.AllBidBuyer(market)

