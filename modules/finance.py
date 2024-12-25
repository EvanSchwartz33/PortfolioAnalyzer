import yfinance as yf


def grab_data(ticker):
    data = yf.Ticker(ticker)

    return data



def portfolio_beta(ticker):

    pass

def grab_price(dat):

    return dat.info['currentPrice']

def grab_beta(dat):

    return dat.info['beta']

def grab_ind(dat):
    
    return dat.info['industry']

def grab_Mcap(dat):

    return dat.info['marketCap']

def grab_EV(dat):

    return dat.info['enterpriseValue']

def grab_debt(dat):
    
    return dat.info['totalDebt']



