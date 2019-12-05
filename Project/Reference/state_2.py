import numpy as np
import random
import math, random 
import gym 
import numpy as np 


class State:
    def __init__(self, data, Bal_stocks, open_cash, timestep):
        # data: t x n_stocks
        # data: t x n_stocks
        self.StockPrices=data[timestep] #stock 1 open price
        # self.=data2[timestep] #stock 2 open price
        self.StockBlncs=Bal_stocks #stock 1 balance
        # self.Stock2Blnc=Bal_stock2 #stock 2 balance
        self.open_cash=open_cash #cash balance
        self.fiveday_stocks=self.five_day_window(data, timestep)
        # self.fiveday_stock2=self.five_day_window(data2, timestep)
        #self.volume1=volume1[timestep]
        #self.volume2=volume2[timestep]
        self.portfolio_value=self.portfolio_value()

    def portfolio_value(self):
        return self.StockPrices * float(self.StockBlncs) + self.open_cash
    
    def next_opening_price(self):
        return data[timestep+1]
    
    def five_day_window(self, data, timestep):
        step = timestep
        if step < 5:
            return data[0]
        
        stock_5days = np.mean(data[step-5:step], axis=0)

        return stock_5days
    
    def reset(self):
        self.StockPrices=np.array([151.25, 21.845])  #stock 1 open price Google
        self.StockBlncs=np.array([34, 221]) #stock 1 balance Google
        self.open_cash=10000 #cash balance
        self.fiveday_stocks=np.array([151.25, 21.845])
        self.portfolio_value=10000
        
    def getState(self):
        res=[]
        res.append(self.StockPrices) #stock 1 open price
        res.append(self.StockBlncs) #stock 1 balance
        res.append(self.open_cash) #cash balance
        res.append(self.fiveday_stocks)
        res.append(self.portfolio_value)

        res1=np.array([res])
        return res1