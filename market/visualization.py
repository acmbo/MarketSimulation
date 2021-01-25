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
    '''Plots the development of price over time'''
    #-------------------------------Preisentwicklung Seller--------------
    for x in range(0,len(market.ListofSeller)):
        plt.plot(market.ListofSeller[x].SellerData.Loop.values, 
                 market.ListofSeller[x].SellerData.Price.values,
                 label= 'Seller '+ market.ListofSeller[x].name + ' Preis')
    plt.ylabel('Price')
    plt.xlabel('Time')
    plt.title('Price development over time')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
              fancybox=True)
    plt.tight_layout()
    plt.show()              




#---------------------------Bidentwicklung Buyer--------------------

def AllBidBuyer(market):
    '''Plots the development of bids over time'''
    for x in range(0,len(market.ListofBuyer)):
        plt.plot(market.ListofBuyer[x].BuyerData.Loop.values, 
                 market.ListofBuyer[x].BuyerData.Bid.values,
                 label= 'Buyer '+ market.ListofBuyer[x].name + ' Bid')
    plt.ylabel('Bid')
    plt.xlabel('Time')
    plt.title('Bid development over time')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
              fancybox=True)
    plt.tight_layout()
    plt.show() 


#---------------------------Mean Price Bid--------------------

def MeanPriceBid(market):
    '''Plots the mean bids and prices within the market'''
    x = market.Market_Metadata.groupby(['Time'])['Price'].mean()
    x2 = market.Market_Metadata.groupby(['Time'])['Bid'].mean()
    plt.plot(x.index.values, 
             x.values,
             label= 'Mean seller price')
    plt.plot(x2.index.values,
             x2.values,
             label= 'Mean buyer bid')
    
    plt.ylabel('Money - Unit')
    plt.xlabel('Time')
    plt.title('Bid and price development over time')
    plt.legend(loc='upper left',
              fancybox=True)
    plt.tight_layout()
    plt.show() 


#------------------------Buyer-------------------------------

def SucessfullActivity(market):
    ''' Plots activity on the market'''
    x = market.Market_Metadata.groupby(['Buyer']).count().sort_values(by='Time')
    y = market.Market_Metadata.groupby(['Seller']).count().sort_values(by='Time')
    
    f = plt.figure(figsize=(9,4))

    ax = f.add_subplot(121)
    ax2 = f.add_subplot(122)
    ax.bar(x.index.values.tolist(), x.Time.values.tolist())
    ax.set_xticks(x.index.values.tolist())
    ax.set_xticklabels(x.index.values.tolist(),rotation=90)
    ax.set_ylabel('Amount of sucessfull bids')
    ax.set_ylabel('Buyer')
    
    ax2.bar(y.index.values.tolist(), y.Time.values.tolist(), color='b')
    ax2.set_xticks(y.index.values.tolist())
    ax2.set_xticklabels(y.index.values.tolist(),rotation=90)
    ax2.set_ylabel('Amount of sucessfull sells')
    ax2.set_ylabel('Seller')

    f.suptitle('Actor engagement into the market')
    plt.tight_layout()
    plt.subplots_adjust(top=0.920)




#------------------------Gesamtwertung--------------------------------    
##https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py



def ActorPerformance(market):
    ''' Plots the development of the accounts of the sellers and buyers '''

    f = plt.figure(figsize=(9, 5))
    for x in range(0,len(market.ListofBuyer)):
        plt.plot(market.ListofBuyer[x].BuyerData.Loop.values, 
                  market.ListofBuyer[x].BuyerData.Account.values,
                  '--',
                  label = 'Money of Buyer '+ str(market.ListofBuyer[x].name))
    for x in range(0,len(market.ListofSeller)):
        plt.plot(market.ListofSeller[x].SellerData.Loop.values, 
                 market.ListofSeller[x].SellerData.Account.values,
                 label= 'Money of Seller '+ str(market.ListofSeller[x].name))
        #plt.plot(market.ListofSeller[x].SellerData.Loop.values, 
               #  market.ListofSeller[x].SellerData.Price.values,
                # label= 'Seller '+ market.ListofSeller[x].name + ' Preis')
                
    # Put a legend below current axis
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',prop={'size': 8},
              fancybox=True)

    plt.title('Available Money for the Actors over time')
    plt.ylabel('Money - Unit')
    plt.xlabel('Time')
    plt.tight_layout()
    plt.show()







##--------------------------------Bidrange--------------------------------------

def BidRande(market, FONTSIZE = 8):
    '''Plots Bid behavior of Buyers'''
    fig, axs = plt.subplots(int(len(market.ListofBuyer)/2),2, figsize=(7,8))
    Plotcount = 0
    for rows in range(0,int(len(market.ListofBuyer)/2)):
        for cols in range(0,2):
            if Plotcount < len(market.ListofBuyer):
                axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Bid.values,'b')
                axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Lower_Price_limit.values, 'C0--')
                axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Upper_Price_limit.values, 'C0--')
                axs[rows, cols].set(title = market.ListofBuyer[Plotcount].name)
                for item in ([axs[rows, cols].title, axs[rows, cols].xaxis.label, axs[rows, cols].yaxis.label] +
                             axs[rows, cols].get_xticklabels() + axs[rows, cols].get_yticklabels()):
                    item.set_fontsize(FONTSIZE)
                Plotcount += 1

    fig.suptitle('Ranges of Bids of the Buyers', fontsize= FONTSIZE+1 )

    from matplotlib.lines import Line2D

    legend_elements = [Line2D([0], [0], color='C0', linestyle='--', lw=2, label='Upperlimit of buyer bid'),
                       Line2D([0], [0], color='b', lw=2, label='Choosen bid'),
                       Line2D([0], [0], color='C0',linestyle='--', lw=2, label='Bottomlimit of buyer bid')]

    fig.legend(handles=legend_elements, bbox_to_anchor=(0.7, 0.5), loc='upper left', prop={'size': FONTSIZE+1},
               fancybox=True)

    fig.text(0.45, 0.04, 'Time', fontsize=FONTSIZE+1, ha='center')
    fig.text(0.04, 0.5, 'Money - Unit', fontsize=FONTSIZE+1,va='center', rotation='vertical')

    plt.tight_layout()
    plt.subplots_adjust(top=0.927, right=0.68, left = 0.1, bottom=.09)








##-----------------Buyer Bid und Account------------------------------------
   
def BuyerBidandAccount(market, FONTSIZE=8):
    '''Plots Bid behavior of Buyers and their Account'''
    fig, axs = plt.subplots(int(len(market.ListofBuyer)),2, figsize=(7.5, len(market.ListofBuyer)*1.5))
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
                    axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values, market.ListofBuyer[Plotcount].BuyerData.Account.values,'g')
                    axs[rows, cols].set(title='Account of '  + str(market.ListofBuyer[Plotcount].name))

            for item in ([axs[rows, cols].title, axs[rows, cols].xaxis.label, axs[rows, cols].yaxis.label] +
                         axs[rows, cols].get_xticklabels() + axs[rows, cols].get_yticklabels()):
                item.set_fontsize(FONTSIZE)

        Plotcount += 1


    fig.suptitle('Ranges of Bids of the Buyers and Buyer account', fontsize= FONTSIZE+1 )

    from matplotlib.lines import Line2D

    legend_elements = [Line2D([0], [0], color='C0', linestyle='--', lw=2, label='Upperlimit of buyer bid'),
                       Line2D([0], [0], color='b', lw=2, label='Choosen price'),
                       Line2D([0], [0], color='C0',linestyle='--', lw=2, label='Bottomlimit of buyer bid'),
                       Line2D([0], [0], color='g', lw=2, label='Account of buyer'),]

    fig.legend(handles=legend_elements, bbox_to_anchor=(0.69, 0.5), loc='upper left', prop={'size': FONTSIZE+1},
               fancybox=True)

    fig.text(0.45, 0.04, 'Time', fontsize=FONTSIZE+1, ha='center')
    fig.text(0.04, 0.5, 'Money - Unit', fontsize=FONTSIZE+1,va='center', rotation='vertical')

    plt.tight_layout()
    plt.subplots_adjust(top=0.94, right=0.68, left = 0.105, bottom=.08, hspace=1)


def BuyerBidandItems(market, FONTSIZE=8):
    '''Plots Bid behavior of Buyers and their Account'''
    fig, axs = plt.subplots(int(len(market.ListofBuyer)), 2, figsize=(7.5, len(market.ListofBuyer) * 1.5))
    Plotcount = 0
    for rows in range(0, int(len(market.ListofBuyer))):
        for cols in range(0, 2):
            if Plotcount < len(market.ListofBuyer):
                if cols == 0:
                    axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values,
                                         market.ListofBuyer[Plotcount].BuyerData.Bid.values, 'b')
                    axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values,
                                         market.ListofBuyer[Plotcount].BuyerData.Lower_Price_limit.values, 'C0--')
                    axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values,
                                         market.ListofBuyer[Plotcount].BuyerData.Upper_Price_limit.values, 'C0--')
                    axs[rows, cols].set(title=market.ListofBuyer[Plotcount].name)
                if cols == 1:
                    axs[rows, cols].plot(market.ListofBuyer[Plotcount].BuyerData.Loop.values,
                                         market.ListofBuyer[Plotcount].BuyerData.Items.values, 'g')
                    axs[rows, cols].set(title='Items of ' + str(market.ListofBuyer[Plotcount].name))

            for item in ([axs[rows, cols].title, axs[rows, cols].xaxis.label, axs[rows, cols].yaxis.label] +
                         axs[rows, cols].get_xticklabels() + axs[rows, cols].get_yticklabels()):
                item.set_fontsize(FONTSIZE)

        Plotcount += 1

    fig.suptitle('Ranges of Bids of the Buyers and Buyer items', fontsize=FONTSIZE + 1)

    from matplotlib.lines import Line2D

    legend_elements = [Line2D([0], [0], color='C0', linestyle='--', lw=2, label='Upperlimit of buyer bid'),
                       Line2D([0], [0], color='b', lw=2, label='Choosen price'),
                       Line2D([0], [0], color='C0', linestyle='--', lw=2, label='Bottomlimit of buyer bid'),
                       Line2D([0], [0], color='g', lw=2, label='Items of Buyer'), ]

    fig.legend(handles=legend_elements, bbox_to_anchor=(0.69, 0.5), loc='upper left', prop={'size': FONTSIZE + 1},
               fancybox=True)

    fig.text(0.45, 0.04, 'Time', fontsize=FONTSIZE + 1, ha='center')
    fig.text(0.04, 0.5, 'Money - Unit', fontsize=FONTSIZE + 1, va='center', rotation='vertical')

    plt.tight_layout()
    plt.subplots_adjust(top=0.94, right=0.68, left=0.105, bottom=.08, hspace=1)


##------------------Seller Price and Account--------------------------------

def SellerPriceandAccount(market,FONTSIZE=8):
    '''Plots Bid behavior of sellers and their Account'''

    fig, axs = plt.subplots(int(len(market.ListofSeller)),2, figsize=(6.5, len(market.ListofSeller)*1.5))
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
                    axs[rows, cols].set(title='Account of ' + str(market.ListofSeller[Plotcount].name))

            for item in ([axs[rows, cols].title, axs[rows, cols].xaxis.label, axs[rows, cols].yaxis.label] +
                         axs[rows, cols].get_xticklabels() + axs[rows, cols].get_yticklabels()):
                item.set_fontsize(FONTSIZE)
        Plotcount += 1

    fig.suptitle('Ranges of seller prices and the sellers account', fontsize= FONTSIZE+1 )

    from matplotlib.lines import Line2D

    legend_elements = [Line2D([0], [0], color='C0', linestyle='--', lw=2, label='Upperlimit of seller price'),
                       Line2D([0], [0], color='b', lw=2, label='Choosen price'),
                       Line2D([0], [0], color='C0',linestyle='--', lw=2, label='Upperlimit of seller price'),
                       Line2D([0], [0], color='g', lw=2, label='Account of Seller'),]

    fig.legend(handles=legend_elements, bbox_to_anchor=(0.67, 0.5), loc='upper left', prop={'size': FONTSIZE+1},
               fancybox=True)

    fig.text(0.45, 0.04, 'Time', fontsize=FONTSIZE+1, ha='center')
    fig.text(0.04, 0.5, 'Money - Unit', fontsize=FONTSIZE+1,va='center', rotation='vertical')

    plt.tight_layout()
    plt.subplots_adjust(top=0.94, right=0.66, left = 0.105, bottom=.08, hspace=1)





def SellerPriceandItems(market,FONTSIZE=8):
    '''Plots Bid behavior of sellers and their Account'''

    fig, axs = plt.subplots(int(len(market.ListofSeller)),2, figsize=(6, len(market.ListofSeller)*1.5))
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
                    axs[rows, cols].plot(market.ListofSeller[Plotcount].SellerData.Loop.values, market.ListofSeller[Plotcount].SellerData.Items.values,'g')
                    axs[rows, cols].set(title='Items of ' + str(market.ListofSeller[Plotcount].name))

            for item in ([axs[rows, cols].title, axs[rows, cols].xaxis.label, axs[rows, cols].yaxis.label] +
                         axs[rows, cols].get_xticklabels() + axs[rows, cols].get_yticklabels()):
                item.set_fontsize(FONTSIZE)
        Plotcount += 1

    fig.suptitle('Ranges of seller prices and the sellers Items', fontsize= FONTSIZE+1 )

    from matplotlib.lines import Line2D

    legend_elements = [Line2D([0], [0], color='C0', linestyle='--', lw=2, label='Upperlimit of seller price'),
                       Line2D([0], [0], color='b', lw=2, label='Choosen price'),
                       Line2D([0], [0], color='C0',linestyle='--', lw=2, label='Upperlimit of seller price'),
                       Line2D([0], [0], color='g', lw=2, label='Items of Seller'),]

    fig.legend(handles=legend_elements, bbox_to_anchor=(0.69, 0.5), loc='upper left', prop={'size': FONTSIZE+1},
               fancybox=True)

    fig.text(0.45, 0.04, 'Time', fontsize=FONTSIZE+1, ha='center')
    fig.text(0.04, 0.5, 'Money - Unit', fontsize=FONTSIZE+1,va='center', rotation='vertical')

    plt.tight_layout()
    plt.subplots_adjust(top=0.94, right=0.68, left = 0.105, bottom=.08, hspace=1)



