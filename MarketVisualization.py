# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:31:13 2019

@author: Stephan
"""
import matplotlib.pyplot as plt


'''

All Function needs a market

Visualization Functions:

AllPricesSeller(market)
BuyerData(market)
ActorPerformance(market)
BidRande(market)
BuyerBidandAccount(market)
SellerPriceandAccount(market)
MeanPriceBid(market)
AllBidBuyer(market)

'''





def AllPricesSeller(market):
    #-------------------------------Preisentwicklung Seller--------------
    for x in range(0,len(market.ListofSeller)):
        plt.plot(market.ListofSeller[x].SellerData.Loop.values, 
                 market.ListofSeller[x].SellerData.Price.values,
                 label= 'Seller '+ market.ListofSeller[x].name + ' Preis')
    plt.ylabel('Money')
    plt.xlabel('Time')
    plt.legend(loc='upper center', bbox_to_anchor=(1.3, 1.1),
              fancybox=True, shadow=True)
    plt.show()              




#---------------------------Bidentwicklung Buyer--------------------

def AllBidBuyer(market):
    for x in range(0,len(market.ListofBuyer)):
        plt.plot(market.ListofBuyer[x].BuyerData.Loop.values, 
                 market.ListofBuyer[x].BuyerData.Bid.values,
                 label= 'Buyer '+ market.ListofBuyer[x].name + ' Bid')
    plt.ylabel('Money')
    plt.xlabel('Time')
    plt.legend(loc='upper center', bbox_to_anchor=(1.3, 1.1),
              fancybox=True, shadow=True)
    plt.show() 


#---------------------------Mean Price Bid--------------------

def MeanPriceBid(market):
    x = market.market.Market_Metadata.groupby(['Time'])['Price', 'Bid'].mean()
    plt.plot(x.index.values, 
             x['Price'].values,
             label= 'MeanSellerprice')
    plt.plot(x.index.values, 
             x['Bid'].values,
             label= 'MeanBuyerBid')
    
    plt.ylabel('Money')
    plt.xlabel('Time')
    plt.legend(loc='upper center', bbox_to_anchor=(1.3, 1.1),
              fancybox=True, shadow=True)
    plt.show() 


#------------------------Buyer-------------------------------

def BuyerData(market):
    x = market.Market_Metadata.groupby(['Buyer']).count().sort_values(by='Time')
    y = market.Market_Metadata.groupby(['Seller']).count().sort_values(by='Time')
    
    f = plt.figure(figsize=(10,3))
    ax = f.add_subplot(121)
    ax2 = f.add_subplot(122)
    ax.bar(x.index.values.tolist(), x.Time.values.tolist())
    ax.set_xticks(x.index.values.tolist())
    ax.set_xticklabels(x.index.values.tolist(),rotation=90)
    
    ax2.bar(y.index.values.tolist(), y.Time.values.tolist(), color='b')
    ax2.set_xticks(y.index.values.tolist())
    ax2.set_xticklabels(y.index.values.tolist(),rotation=90)




#------------------------Gesamtwertung--------------------------------    
##https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py



def ActorPerformance(market):
    for x in range(0,len(market.ListofBuyer)):
        plt.plot(market.ListofBuyer[x].BuyerData.Loop.values, 
                  market.ListofBuyer[x].BuyerData.Account.values,
                  '--',
                  label = 'Money '+ market.ListofBuyer[x].name)
    for x in range(0,len(market.ListofSeller)):
        plt.plot(market.ListofSeller[x].SellerData.Loop.values, 
                 market.ListofSeller[x].SellerData.Account.values,
                 label= 'Seller '+ market.ListofSeller[x].name + ' Geld')
        #plt.plot(market.ListofSeller[x].SellerData.Loop.values, 
               #  market.ListofSeller[x].SellerData.Price.values,
                # label= 'Seller '+ market.ListofSeller[x].name + ' Preis')
                
    # Put a legend below current axis
    plt.legend(loc='upper center', bbox_to_anchor=(1.3, 1.1),
              fancybox=True, shadow=True)
    
    plt.ylabel('Money')
    plt.xlabel('Time')
    #plt.legend()
    plt.show()        






##--------------------------------Bidrange--------------------------------------

def BidRande(market):
    #fig1, f1_axes = plt.subplots(ncols=2, nrows= int(RandomBuyer/2), constrained_layout=True, figsize=(5, 5))
    fig, axs = plt.subplots(int(len(market.ListofBuyer)/2),2, figsize=(6, 25))
    Plotcount = 0
    for rows in range(0,int(len(market.ListofBuyer)/2)):
        for cols in range(0,2):
            if Plotcount < len(market.ListofBuyer):
                axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Bid.values,'b')
                axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Lower_Price_limit.values, 'C0--')
                axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Upper_Price_limit.values, 'C0--')
                axs[rows, cols].set(title = market.ListofBuyer[Plotcount].name)
                Plotcount += 1
    fig.tight_layout()







##-----------------Buyer Bid und Account------------------------------------
   
def BuyerBidandAccount(market):
    #fig1, f1_axes = plt.subplots(ncols=2, nrows= int(RandomBuyer/2), constrained_layout=True, figsize=(5, 5))
    fig, axs = plt.subplots(int(len(market.ListofBuyer)),2, figsize=(6, len(market.ListofBuyer)*1.25))
    Plotcount = 0
    for rows in range(0,int(len(market.ListofBuyer))):
        for cols in range(0,2):
            if Plotcount < len(market.ListofBuyer):
                if cols == 0:
                    axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Bid.values,'b')
                    axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Lower_Price_limit.values, 'C0--')
                    axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Upper_Price_limit.values, 'C0--')
                    axs[rows, cols].set(title = market.ListofBuyer[Plotcount].name)
                if cols == 1:
                    axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Items.values,'g')
        Plotcount += 1
    fig.tight_layout()




##------------------Seller Price and Account--------------------------------
def SellerPriceandAccount(market):
    fig, axs = plt.subplots(int(len(market.ListofSeller)),2, figsize=(6, len(market.ListofSeller)*1.25))
    Plotcount = 0
    for rows in range(0,int(len(market.ListofSeller))):
        for cols in range(0,2):
            if Plotcount < len(market.ListofSeller):
                if cols == 0:
                    axs[rows, cols].plot(market.ListofSeller[Plotcount].SellerData.Loop.values, market.ListofSeller[Plotcount].SellerData.Price.values,'b')
                    axs[rows, cols].plot(market.ListofSeller[Plotcount].SellerData.Loop.values, market.ListofSeller[Plotcount].SellerData.Lower_Price_limit.values, 'C0--')
                    axs[rows, cols].plot(market.ListofSeller[Plotcount].SellerData.Loop.values, market.ListofSeller[Plotcount].SellerData.Upper_Price_limit.values, 'C0--')
                    axs[rows, cols].set(title = market.ListofSeller[Plotcount].name)
                if cols == 1:
                    axs[rows, cols].plot(market.ListofSeller[Plotcount].SellerData.Loop.values, market.ListofSeller[Plotcount].SellerData.Account.values,'g')
        Plotcount += 1
    fig.tight_layout()





