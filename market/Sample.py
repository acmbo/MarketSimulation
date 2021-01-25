# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:09:52 2019

@author: Stephan
"""

from market import Marketactor, Marketplace as Market, visualization as mv


if __name__ == '__main__':
    '''This is a sample, how to set up a market and add actor to the market, which interact with each other.+
        After Simulation the results are printed'''


    # Add a single Buyer to the List of Buyers in the market
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

    # Add a single Seller to the List of Buyers in the market
    ListofSeller = [Marketactor.market_Seller(name ='Boris',
                                              upperlimit = 23,
                                              lowerlimit = 13,
                                              account = 0,
                                              items = 20),
                    Marketactor.market_Seller(name ='Tony',
                                              upperlimit = 30,
                                              lowerlimit = 10,
                                              account = 0,
                                              items = 30)]

    #Creation of the market
    market = Market.market(ListofBuyer,ListofSeller)


    #Adding randome buyers and Sellers
    RandomSeller = 10
    RandomBuyer = 10

    for count in range(0,RandomSeller):
        market.AddRandomSeller('RandomSeller_' + str(count),50,10,30)

    for count in range(0,RandomBuyer):
        market.AddRandomBuyer('RandomBuyer_' + str(count),50,10,300)

    #Run the Simulation
    market.SimulateIdealMarket(LengthofSimulation = 40,     # How many Rounds to Simulate
                                wanteditems = 1,            # How many items are transfered with one buy
                                MultipleSells = True)      # How can an actor buy multiple items in one round


    #Plott the Results - choose a command and decommend it with matplotlib together
    #import matplotlib.pyplot as plt

    #mv.AllPricesSeller(market)
    #plt.savefig('allPircesSeller.png' ,dpi=300)
    #mv.SucessfullActivity(market)
    #plt.savefig('SucessfullActivity.png', dpi=300)
    #mv.ActorPerformance(market)
    #plt.savefig('ActorPerformance.png', dpi=300)
    #mv.BidRande(market)
    #plt.savefig('BidRande.png', dpi=300)
    #mv.BuyerBidandAccount(market)
    #plt.savefig('BuyerBidandAccount.png', dpi=300)
    #mv.SellerPriceandAccount(market)
    #plt.savefig('SellerPriceandAccount.png', dpi=300)
    #mv.MeanPriceBid(market)
    #plt.savefig('MeanPriceBid.png', dpi=300)
    #mv.AllBidBuyer(market)
    #plt.savefig('AllBidBuyer.png', dpi=300)
    #mv.SellerPriceandItems(market)
    #plt.savefig('SellerPriceandItems.png', dpi=300)
    #mv.BuyerBidandItems(market)
    #plt.savefig('BuyerBidandItems.png', dpi=300)
