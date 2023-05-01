#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:44:27 2023
@author: crypto_2024
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openbb_terminal.sdk import openbb
from openbb_terminal.sdk import TerminalStyle
from datetime import datetime
from app_env import CONFIG_OPENBB,APP_KEYS


class Coin:

    def __init__(self, symbol, start_date, interval=1440, source='Coingecko', exchange='binance', end_date=None):
        
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.source = source
        self.exchange = exchange
        #self.set_key()

    def login(self):
        
        openbb.login(email=CONFIG_OPENBB['USER_NAME'],password=CONFIG_OPENBB['PASSWORD'],token= CONFIG_OPENBB['API_OPENBB'])

    def set_key(self):

        openbb.keys.messari(key=APP_KEYS['API_MESSARI_KEY'], persist = False, show_output = False)
        openbb.keys.glassnode(key=APP_KEYS['API_GLASSNODE_KEY'],persist = False, show_output = False)
        openbb.keys.av(key=APP_KEYS['API_KEY_ALPHAVANTAGE'], persist=False, show_output=False)
        openbb.keys.cpanic(key=APP_KEYS['API_CRYPTO_PANIC_KEY'], persist=False, show_output=False)
        openbb.keys.cmc(key=APP_KEYS['API_CMC_KEY'], persist=False, show_output=False)
        openbb.keys.github(key=APP_KEYS['API_GITHUB_KEY'], persist=False, show_output=False)
        openbb.keys.ethplorer(key=APP_KEYS['API_ETHPLORER_KEY'], persist=False, show_output=False)
        openbb.keys.twitter(key=APP_KEYS['API_TWITTER_KEY'], secret=APP_KEYS['API_TWITTER_SECRET_KEY'],access_token=APP_KEYS['API_TWITTER_ACCESS_TOKEN'],persist=False, show_output=False)
      
    #Candle
    def plot_candle_df_binance(self,symbol,data,start_date,end_date,interval,exchange='binance',to_symbol='usdt',source='CCXT',volume='True',title='',external_axes=False,yscale='linear',raw=False):
       
        """
        Plot candle chart from dataframe. [Source: Binance]

        Parameters
        ----------
        symbol : str
           Ticker name
        data : pd.DataFramepd.DataFrame
           Ticker name
        start_date : Union[datetime, Union[str, None]]
           Start date for data
        end_date : Union[datetime, Union[str, None]]
            End date for data
        interval : Union[str, int]
           Interval for data
        exchange : str, optional
            Exchange to use. The default is 'binance'.
        to_symbol : str, optional
            Currency to use. The default is 'usdt'.
        source : str, optional
            Source to use. The default is 'CCXT'.
        volume : bool, optional
            If volume data shall be plotted, by default True. The default is 'True'.
        title : str, optional
            Title of graph, by default "". The default is ''.
        external_axes : bool, optional
            Whether to return the figure object or not, by default False. The default is False.
        yscale : str, optional
           Scaling for y axis. Either linear or log. The default is 'linear'.
        raw : bool, optional
             The default is False.

        Returns
        -------
        None.

        """
        
        openbb.crypto.candle(symbol, data, start_date,end_date, interval, exchange, to_symbol, source, volume, title, external_axes, yscale, raw)
    
    def candle_trade_pair_coinbase(self, pair_symbol,time_interval="24 hour"):
       
        """
        Get candles for chosen trading pair and time interval. [Source: Coinbase]

        Parameters
        ----------
        pair_symbol : str
            Trading pair of coins on Coinbase e.g ETH-USDT or UNI-ETH.
        time_interval : str, optional
           Time interval. One from 1min, 5min ,15min, 1hour, 6hour, 24hour, 1day. 
           The default is "24 hour".

        Returns
        -------
       pd.DataFrame,Candles for chosen trading pair.

        """
        
        candle_pair = openbb.crypto.dd.candle(symbol=pair_symbol, interval=time_interval)
        return candle_pair
   
    #Ticker chart 
    
    def plot_ta_chart(self):
        
        """
        Load data for Technical Analysis

        Returns
        -------
        None.

        """
        price_data = openbb.crypto.load(self.symbol)
        openbb.crypto.chart(price_data, to_symbol="usdt", from_symbol=self.symbol, source="binance", exchange="binance",
                            interval="1d", yscale="linear")
     
    
    #Price
    
    def get_close_price(self, start_date, end_date):
        """
        Returns the price of a cryptocurrency

        Parameters
        ----------
        start_date : str
            Initial date, format YYYY-MM-DD.
        end_date : str
            Final date, format YYYY-MM-DD
        Returns
        -------
        close_price :pd.DataFrame

        """
        close_price = openbb.crypto.dd.close(self.symbol, start_date, end_date, print_error=True)
        return close_price
    
    def load_hist_price_volume(self,start):
        """
        Load crypto currency to get data for

        Returns
        -------
        pd.dataframe
            DESCRIPTION.

        """
         
        price_volume_hist = openbb.crypto.load(self.symbol, start_date=self.start_date, exchange=self.exchange,
                                                to_symbol='usdt', source=self.source)
        return price_volume_hist
    
    def get_coin_market_chart(self,symbol,vs_currency='usd',days=30):
        """
        Get prices for given coin. [Source: CoinGecko]

        Parameters
        ----------
        symbol : str
            DESCRIPTION.
        vs_currency : str, optional
            currency vs which display data. The default is 'usd'.
        days : int, optional
            number of days to display the data. The default is 30.

        Returns
        -------
        pd.DataFrame.
        Prices for given coin
        Columns: time, price, currency

        """
        coin_market_coingecko=openbb.crypto.dd.coin_market_chart(symbol, vs_currency, days)
        return coin_market_coingecko
     
    def get_ticker_info_chart(self, quotes='USD'):
         
         """
         
         Get all most important ticker related information for given coin id [Source: CoinPaprika]
         Parameters
         ----------
         quotes : str, optional
            Comma separated quotes to return e.g quotes = USD, BTC. The default is 'USD'.

         Returns
         -------
         pd.DataFrame
         Most important ticker related information
         Columns: Metric, Value

         """
         ps = openbb.crypto.dd.ps(self.symbol, quotes)
         openbb.crypto.dd.ps_chart(self.symbol, to_symbol=quotes, export='{} ps_chart'.format(self.symbol),
                                    sheet_name='ps_chart')   
         return ps
        
     
     
     #Order Book
     
    def get_ob_coin(self,exchange_id,to_symbol):
         """
        Returns orderbook for a coin in a given exchange

         Parameters
         ----------
         exchange_id : str
             DESCRIPTION.
         to_symbol : str
             currency to compare coin against

         Returns
         -------
        Dict[str, Any]
        With bids and asks

         """
         coin_orderbook=openbb.crypto.dd.ob(exchange_id,self.symbol, to_symbol)
         return coin_orderbook
    
    #onchain address   
      
    def get_onchain_address(self):
        """
        Returns onchain addresses info of a certain coin

        Returns
        -------
        pd.Dataframe
        
        """
        #Returns active addresses:pd.dataframe of a certain coin
        active_address = openbb.crypto.dd.active(symbol=self.symbol, interval='24h', start_date=self.start_date, end_date=self.end_date)
        #Returns addresses with non-zero balance of a certain symbol                                        
        nonzero_address = openbb.crypto.dd.nonzero(self.symbol, self.start_date, self.end_date)                                       
        #Plots active addresses of a certain symbol over time
        openbb.crypto.dd.active_chart(symbol=self.symbol, start_date=self.start_date, end_date=self.end_date,
                                      interval="24h", export="{} 's active_address.xlsx ".format(self.symbol),
                                      sheet_name="active_address", external_axes=False)
        return active_address,nonzero_address
    
    #Binance

    def get_binance_trading_pairs(self):
        """
        Returns all available pairs on Binance in DataFrame format

        Returns
        -------
        dataframe
            DataFrame has 3 columns symbol, baseAsset, quoteAsset

        """
        return openbb.crypto.dd.all_binance_trading_pairs()

    def get_binance_account_asset_holding(self,from_symbol='BTC',to_symbol='USDT'):
        
        """
        Get account holdings for asset. [Source: Binance]
        Prints table showing account holdings for asset. [Source: Binance]

        Parameters
        ----------
        from_symbol :str
           The default is 'BTC'.
        to_symbol :str
           The default is 'USDT'.

        Returns
        -------
        assets_holding_df : pd.dataframe
            DESCRIPTION.

        """
        assets_holding_df=openbb.crypto.dd.balance(from_symbol,to_symbol)
        openbb.crypto.dd.balance_chart(from_symbol, to_symbol, export= "asset_holdings_in_binance.xlsx", sheet_name = None)
        return assets_holding_df
    

    def get_coin_quotes_binance(self):
        """
        Helper methods that for every coin available on Binance add all quote assets. [Source: Binance]

        Returns
        -------
       dict
            All quote assets for given coin

        """
        return openbb.crypto.dd.binance_available_quotes_for_each_coin()

    def check_valid_binance_str(self,symbol):
        """
        Check if symbol is in defined binance. [Source: Binance]

        Parameters
        ----------
        symbol : str
           

        Returns
        -------
        str

        """
        return openbb.crypto.dd.check_valid_binance_str(symbol)


    # exchange holdings and supply change
    def get_held_amount_in_exchange_wallet(self,start, end):
       
        """
        Returns the total amount of coins held on exchange addresses in units and percentage.
        Parameters
        ----------
        start : TYPE
            DESCRIPTION.
        end : TYPE
            DESCRIPTION.

        Returns
        -------
        address : TYPE
            DESCRIPTION.

        """
        total_amount = openbb.crypto.dd.eb(self.symbol, start, end, exchange="aggregated")
        return total_amount

    def get_supply_change_exchange(self, exchange, start, end):
        """
        Returns 30d change of the supply held in exchange wallets of a certain symbol.

        Parameters
        ----------
        start : str
            Initial date, format YYYY-MM-DD
        end : str
            Final date, format YYYY-MM-DD

        Returns
        -------
        address : pd.DataFrame
            supply change in exchange wallets of a certain symbol over time

        """
        supply_change = openbb.crypto.dd.change(self.symbol, exchange, start, end)
        return supply_change
    
    #Returns market dominance of a coin over time
    def get_market_dominance(self, start_date, end_date, interval='1d'):
        return openbb.crypto.dd.mcapdom(self.symbol, interval, start_date, end_date)

    #Basic Info of coin
    
    def get_base_info(self, start_date, end_date):
        
        self.login()
        self.set_key()
       
        coin_basic_info = {}
        coin_ath = openbb.crypto.dd.ath(self.symbol) #Get all time high for a coin in a given currency,return dataframe
        coin_atl = openbb.crypto.dd.atl(self.symbol) #Get all time low for a coin in a given currency,return dataframe
        coin_basic = openbb.crypto.dd.basic(self.symbol) #Basic coin information [Source: CoinPaprika]
        coin_dev = openbb.crypto.dd.dev(self.symbol) #Get developer stats for a coin
        coin_event = openbb.crypto.dd.events(self.symbol, sortby="date", ascend=False)#Get all events related to given coin like conferences, start date of futures trading etc.
        coin_investor = openbb.crypto.dd.inv(self.symbol) #Returns coin investors
        coin_links = openbb.crypto.dd.links(self.symbol) #Returns asset's links
        coin_product = openbb.crypto.dd.pi(self.symbol) #Returns coin product info
        coin_team = openbb.crypto.dd.team(self.symbol) #Returns coin team

        coin_tokenomics = openbb.crypto.dd.tokenomics(self.symbol)
        coin_roadmap = openbb.crypto.dd.rm(self.symbol, True) #Returns coin roadmap
        coin_fundrasing = openbb.crypto.dd.fr(self.symbol) #Returns coin fundraising
        coin_goverance = openbb.crypto.dd.gov(self.symbol) #Returns coin governance
        
        coin_score = openbb.crypto.dd.score(self.symbol) #Get scores for a coin from CoinGecko
        coin_social_stats = openbb.crypto.dd.social(self.symbol) #Get social media stats for a coin

        coin_basic_info['ath'] = coin_ath
        coin_basic_info['atl'] = coin_atl
        coin_basic_info['basic'] = coin_basic
        coin_basic_info['dev'] = coin_dev
        coin_basic_info['coin_event'] = coin_event
        coin_basic_info['investor'] = coin_investor
        coin_basic_info['coin_links'] = coin_links
        coin_basic_info['team'] = coin_team
        coin_basic_info['tokenomics'] = coin_tokenomics
        coin_basic_info['roadmap'] = coin_roadmap
        coin_basic_info['fundrasing'] = coin_fundrasing
        coin_basic_info['goverance'] = coin_goverance
        coin_basic_info['product'] = coin_product
        coin_basic_info['score'] = coin_score
        coin_basic_info['social_stats'] = coin_social_stats
        
        return coin_basic_info

    #Messari
    def messari_coin_timeseries(self,timeseries_id,start_date,end_date,interval='1d'):
        
        """
        Parameters
        ----------
        timeseries_id : str
           Messari timeserie id
        start_date : str
           Initial date like string (e.g., 2021-10-01)
        end_date : str
            End date like string (e.g., 2021-10-01)
        interval : str optional
           Interval frequency (possible values are: 5m, 15m, 30m, 1h, 1d, 1w). The default is '1d'.

        Returns
        -------
        Tuple[pd.DataFrame, str].
        Messari timeseries over time,
        Timeseries title
       
        """
        time_series=openbb.crypto.dd.get_mt(only_free = True)
        messari_coin_timeseries=openbb.crypto.dd.mt(self.symbol, timeseries_id, interval,start_date, end_date)
        return time_series,messari_coin_timeseries

    
    #get dev activies of coin  over-time
    
    def dev_activity_crypto(self,symbol,start_date,end_date,dev_activity=False,interval="1d",):
        return openbb.crypto.dd.gh(symbol, dev_activity, interval, start_date, end_date)


    def get_open_interest(self, interval=0):
        """
        Returns open interest by exchange for a certain symbol
    
        Parameters
        ----------
        interval : int, optional
            Frequency (possible values are: 0 for ALL, 2 for 1H, 1 for 4H, 4 for 12H), by default 0. The default is 0.

        Returns
        -------
        pd.DataFrame
           open interest by exchange and price

        """
        return openbb.crypto.dd.oi(symbol=self.symbol, interval=interval)

     
    # Get recent posts from CryptoPanic news aggregator platform
    def get_coin_news(self,limit=60,post_kind='news',filter_="hot",region="en",sortby="published_at",ascend=True):
        """
        Parameters
        ----------
        limit : int
           number of news to fetch
        post_kind : str
            Filter by category of news. Available values: news or media.
        filter_ : str
           Filter by kind of news. One from list: rising
        region : str
            Filter news by regions. Available regions are: en (English), de (Deutsch), nl (Dutch),
            es (Español), fr (Français), it (Italiano), pt (Português), ru (Русский)
        sortby : TYPE
            DESCRIPTION.
        ascend : TYPE
            DESCRIPTION.

        Returns
        -------
        fetch_news : pd.DataFrame
            DataFrame with recent news from different sources filtered by provided parameters.

        """
        fetch_news = openbb.crypto.dd.news(limit, post_kind, filter_, region, sortby)
        return fetch_news
   
    #CoinPaprika 
    def id_exchange_coin(self,symbol):
        """
        #get coin id of CoinPaprika and Get all exchanges for given coin id

        Parameters
        ----------
        symbol : str
            DESCRIPTION.

        Returns
        -------
        pd.dataframe
        All exchanges for given coin
        Columns: id, name, adjusted_volume_24h_share, fiats  

        """
        
        coin_id=openbb.crypto.dd.coin(symbol)
        all_exchanges=openbb.crypto.dd.ex(symbol, sortby= "adjusted_volume_24h_share", ascend = True)
        return all_exchanges
    
    
    def get_sentiment_analysis(self):
       
        """
        Gets Sentiment analysis provided by FinBrain's API [Source: finbrain].
        
        Returns
        -------
        pd.DataFrame
           Empty if there was an issue with data retrieval.

        """
        return openbb.crypto.dd.headlines(self.symbol)

    #Twitter
    
    def get_twitter_timeline(self,limit=10,sort_by='date',ascend=True):
        """
        Get twitter timeline for given coin id. Not more than last 50 tweets [Source: CoinPaprika]

        Parameters
        ----------
        sort_by : str, optional
            Key by which to sort data. Every column name is valid. The default is 'date'.
        ascend : bool, optional
           Flag to sort data descending. The default is True.

        Returns
        -------
        twitter_timeline : pd.DataFrame
        Twitter timeline for given coin.
        Columns: date, user_name, status, retweet_count, like_coun

        """
        
        twitter_timeline= openbb.crypto.dd.twitter(self.symbol, sort_by, ascend)
        openbb.crypto.dd.twitter_chart(self.symbol, sort_by, ascend, limit= 10,export = "{} twitter timeline.xlsx".format(self.symbol))
        
        return twitter_timeline
        


class CryptoMarket:

    def __init__(self, symbol, limit):
        self.symbol = symbol
        self.limit = limit
    #Get global crypto market data.
    def global_crypto_data(self):
        return openbb.crypto.ov.globe(source="CoinGecko")
    
    #Returns basic coin information for all coins from CoinPaprika API [Source: CoinPaprika]
    
    def get_crypto_ov_info(self):
      return openbb.crypto.ov.info(symbols = "USD", sortby = "rank", ascend= True)
    #Returns basic coin information for all coins from CoinPaprika API [Source: CoinPaprika]
    
    def get_crypto_ov_market(self):
        return openbb.crypto.ov.markets(symbols= "USD", sortby= "rank", ascend= True)
                            
    #Get list of coins available on CoinGecko [Source: CoinGecko]
    def get_coinlist_coingecko(self):
        return openbb.crypto.disc.coin_list()
    #Get list of all available coins on CoinPaprika [Source: CoinPaprika]
    def get_coinlist_coinpaprika(self):
        openbb.crypto.ov.coin_list()
    
    #Helper method to get all coins available on binance exchange [Source: CoinGecko]
    def get_available_coin_binance(self, exchange_id='binance', page=1):
        coin_dict = openbb.crypto.disc.coins_for_given_exchange(exchange_id=exchange_id, page=page)
        return coin_dict
    #get supply of bitcoin
    def get_btc_supply(self):
        return openbb.crypto.onchain.btc_supply()
    # Get bitcoin price data
    def get_btc_price_data(self,start_date,end_date):
        btc_rb=openbb.crypto.ov.btcrb(start_date, end_date)
        return btc_rb
    #Get list of coin categories 
    def get_token_categories(self): 
        return openbb.crypto.disc.categories_keys()
    #Get N coins from CoinGecko [Source: CoinGecko]
    def get_n_coins_coingecko(self, num, category):
        """
        

        Parameters
        ----------
        num : int
           Number of top coins to grab from CoinGecko
        category : str
            Category of the coins we want to retrieve

        Returns
        -------
        n_coin : pd.DataFrame
           N coins

        """
        n_coin = openbb.crypto.disc.coins(limit=num, category=category, sortby="Symbol", ascend=False)
        return n_coin
    
    #trending coins [Source: CoinGecko]
    def trending_coins(self):
        return openbb.crypto.disc.trending()
    
    #stable coins
    def stable_coins(self):
        return openbb.crypto.ov.stables(limit=15, sortby="Market_Cap_[$]", ascend=False)
    
    #altcoin   
    def altcoin_index(self,period,start_date,end_date):    
        """
        

        Parameters
        ----------
        period : int
           Number of days {30,90,365} to check performance of coins and calculate the altcoin index.
          E.g., 365 checks yearly performance, 90 will check seasonal performance (90 days),
         30 will check monthly performance (30 days).
        start_date : str
          
        end_date : str
            
        Returns
        -------
        altcoin_index : pd.Dataframe
          Date, Value (Altcoin Index)

        """
        altcoin_index =openbb.crypto.ov.altindex(period, start_date, end_date)
        return altcoin_index
   #Shows Largest Gainers and Losers coins
    def gain_lose_stats_period(self, interval="1h", limit=50, sortby='market_cap_rank'):
        """
        

        Parameters
        ----------
        interval : str, optional
           Time interval by which data is displayed. One from [1h, 24h, 7d, 14d, 30d, 60d, 1y]. The default is "1h".
        limit :Number of records to display, optional
            DESCRIPTION. The default is 50.
        sortby : TYPE, optional
           Key to sort data. The table can be sorted by every of its columns. The default is 'market_cap_rank'.

        Returns
        -------
        gain_df : pd.Dataframe
           top_gainers
        lose_df : pd.Dataframe
           top_losers

        """
        gain_df = openbb.crypto.disc.gainers(interval=interval, limit=limit, sortby=sortby, ascend=True)
        lose_df = openbb.crypto.disc.losers(interval=interval, limit=limit, sortby=sortby, ascend=True)
        return gain_df, lose_df
   
    
   #Get top cryptp coins,top dapps,top dexes, top_dexes,top game,top nfts 
    def get_top_stats(self):
        top_coins = openbb.crypto.disc.top_coins(source="CoinGecko", limit=10)
        top_dapps = openbb.crypto.disc.top_dapps(sortby="users", limit=10)  # daily volume or users
        top_dexes = openbb.crypto.disc.top_dexes(sortby="users", limit=10)
        top_game = openbb.crypto.disc.top_games(sortby="users", limit=10)
        top_nfts = openbb.crypto.disc.top_nfts(sortby="", limit=10)
        return top_coins,top_dapps,top_dexes,top_nfts
    
    #Get crypto hack info
    def get_coin_hack_info(self):
        major_crypto_hack = openbb.crypto.ov.crypto_hacks(sortby="Platform", ascend=False)
        slugs = openbb.crypto.ov.crypto_hack_slugs()
        crypto_hack = []
        for slug in slugs:
            crypto_hack.append(openbb.crypto.ov.crypto_hack(slug))
        return crypto_hack
    
    #derivatives from CoinGecko API 
    def coin_derivatives(self):
        derivative_market_info = openbb.crypto.ov.derivatives(sortby="Rank", ascend=False)
   
    # Decentralized Finances [Source: CoinGecko]
    def global_defi_market(self):
        defi_market = openbb.crypto.ov.defi()
    
   
    def exchange(self):
        top_exchanges = openbb.crypto.ov.exchanges(source="CoinGecko") #Show top crypto exchanges.
        exchange_withdrawl_fee = openbb.crypto.ov.ewf() #Scrapes exchange withdrawal fees
        exchange_rates = openbb.crypto.ov.exrates(sortby="Name", ascend=False)
    
    #List markets by exchange ID [Source: CoinPaprika]
    def market_list_exchange(self,exchange_id,symbols='USD'):
        market_list_exchange = openbb.crypto.ov.exmarkets(exchange_id, symbols, sortby= "pair", ascend= True)
        return market_list_exchange
  
    #Get list of crypto, fiats, commodity exchange rates from CoinGecko API [Source: CoinGecko]
    def get_ov_exrates(self):
        return openbb.crypto.ov.exrates(sortby= "Name", ascend= False)
   
    #List all smart contract platforms like ethereum, solana, cosmos, polkadot, kusama ... [Source: CoinPaprika]
    def smart_contract_platform(self):
        return openbb.crypto.ov.platforms()
    
    #contract address for smart-contract platform
    def get_contracts(self,platform_id= "eth-ethereum"):
        contract_address= openbb.crypto.ov.contracts(platform_id, sortby = "active", ascend = True)
        return contract_address
    
    #Get list of financial products from CoinGecko API
    def financial_product(self):
        return openbb.crypto.ov.products(sortby="Name", ascend=True)
    #Scrapes coin withdrawal fees per exchange / top coins withdrawal fees
    def coin_withdraw_fee(self, symbol):
        top_coins_fees = openbb.crypto.ov.wf(limit=100)
        top_coins_fees_per_exchange=openbb.crypto.ov.wfpe(symbol=symbol)
        return top_coins_fees, top_coins_fees_per_exchange
    
    #Coin Lending
    
    def get_coin_rate(self):
        borrow_rate =openbb.crypto.ov.cr(rate_type = "borrow")
        supply_rate=openbb.crypto.ov.cr(rate_type = "supply")
       
        return borrow_rate,supply_rate
    
    # Public companies that holds bitcoin or ethereum
    def public_companies_holder(self):
        btc_holder=openbb.crypto.ov.hold(endpoint= "bitcoin")
        eth_holder=openbb.crypto.ov.hold(endpoint= "ethereum")
        
        return btc_holder,eth_holder
   
class OnChain:

    def __init__(self, symbol, limit):
        self.symbol = symbol
        self.limit = limit

    def btc_chain(self):
        btc_supply = openbb.crypto.onchain.btc_supply() #Returns BTC circulating supply [Source: https://api.blockchain.info/]
        btc_transac = openbb.crypto.onchain.btc_transac() #Returns BTC confirmed transactions [Source: https://api.blockchain.info/]
        

    def btc_singleblock(self, blockhx):
        return openbb.crypto.onchain.btcsingleblock(blockhx) #Returns BTC block data in json format. [Source: https://blockchain.info/]

    def eth_chain(self):
        erc20_tokens = openbb.crypto.onchain.erc20_tokens()  # 1500 coins
        recent_gwei = openbb.crypto.onchain.gwei()  # Returns the most recent Ethereum gas fees in gwei
        return erc20_tokens,recent_gwei
        
    #Get information about balance historical transactions. [Source: Ethplorer]
    def get_hist_transaction(self, address: str, sortby='timestamp', ascending=True):
        hist_trans = openbb.crypto.onchain.hist(address, sortby=sortby, ascend=ascending)
        return hist_trans
    #Get info about top token holders. [Source: Ethplorer]
    def get_top_holder(self, address, sortby='balance', ascend=True):
        top_holder = openbb.crypto.onchain.holders(address=address, sortby=sortby, ascend=ascend)
        return top_holder
    #Returns dataframe with mean hashrate of btc or eth blockchain and symbol price
    def hashrate_price(self, symbol, start, end, interval='24h'):
        hashrate_price_df = openbb.crypto.onchain.hr(symbol=symbol, start_date=start, end_date=end, interval=interval)
        openbb.crypto.onchain.hr_chart(symbol=symbol, start_date=start, end_date=end, interval=interval,
                                       export="hashrate_price_chart.xlsx")
        return hashrate_price_df
    
    #Get info about ERC20 token. [Source: Ethplorer]
    def erc20_info(self, address):
        token_info = openbb.crypto.onchain.info(address)
        return token_info


    #Get number of unique ethereum addresses which made a transaction in given time interval.
    def get_unique_ether_address(self, interval='day', limit=90, sortby='tradeAmount', ascend=True):
        return openbb.crypto.onchain.ueat(interval=interval, limit=limit, sortby=sortby, ascend=ascend)
    
    #Get info about transaction. [Source: Ethplorer]
    def get_tx_info(self, tx_hash):
        return openbb.crypto.onchain.tx(tx_hash)
    
    #Get token volume on different Decentralized Exchanges. [Source: https://graphql.bitquery.io/]
    def get_tv_dex(self, symbol):
        return openbb.crypto.onchain.tv(symbol, trade_amount_currency="USD", sortby="tradeAmount", ascend=True)
 
    #Get most traded crypto pairs on given decentralized exchange in chosen time period.
    def get_most_traded_pair(self, network='bsc', exchange='Uniswap', limit=90,sortby="tradeAmount", ascend=True):
        return openbb.crypto.onchain.ttcp(network=network, exchange=exchange, limit=limit, sortby=sortby, ascend=ascend)
   
    #Get top 50 tokens. [Source: Ethplorer]
    def get_top50(self):
        return openbb.crypto.onchain.top(sortby="rank", ascend=False)
  
    #Helper methods that gets token decimals number. [Source: Ethplorer]
    def get_token_decimals(self, address):
        return openbb.crypto.onchain.token_decimals(address)
    
    #Get info about token historical transactions. [Source: Ethplorer]
    def get_token_th(self, address):
        return openbb.crypto.onchain.th(address, sortby="timestamp", ascend=False)

    #Get token historical prices with volume and market cap, and average price. [Source: Ethplorer]
    def get_token_hist_chart(self, address):
        hist_price = openbb.crypto.onchain.prices(address, sortby="date", ascend=False)
        openbb.crypto.onchain.prices_chart(address, limit=30, sortby="date", ascend=False, export="history_chart.xlsx")
        return hist_price
    
    #Crypto whales transactions
    def get_whale_alerts(self):
        return openbb.crypto.onchain.whales(min_value = 800000, limit= 100, sortby = "date", ascend= False)
    #Get daily volume for given pair [Source: https://graphql.bitquery.io/]
    def get_daily_volume_pairs(self,limit=100,symbol='UNI',to_symbol='USDT',sortby='date',ascend=True):
        return openbb.crypto.onchain.dvcp(limit, symbol, to_symbol, sortby, ascend)
    #Get list of trades on decentralized exchange monthly aggregated
    def get_aggregated_dex_trade(self,trade_amount_currency= "USD",limit=90,ascend=True):
        return openbb.crypto.onchain.dex_trades_monthly(trade_amount_currency, limit, ascend)
   
    #Get trades on Decentralized Exchanges aggregated by DEX [Sourc
    def get_onchain_lt(self,trade_amount_currency= "USD",limit=90,sortby='tradeAmount',ascend=True):
        return openbb.crypto.onchain.lt(trade_amount_currency, limit, sortby, ascend)
   
    #Get an average bid and ask prices, average spread for given crypto pair for chosen time period.
    def get_bid_ask_coin(self,symbol='WETH',to_symbol='USDT',limit=10,sortby='date',ascend=True):
        bid_ask_spread=openbb.crypto.onchain.baas(symbol, to_symbol, limit, sortby, ascend)
        return bid_ask_spread

class DeFi:

    #Returns information about historical tvl of a defi protocol.
    def get_tvl(self,protocol):
        return openbb.crypto.defi.dtvl(protocol)
    #Display top dApps (in terms of TVL) grouped by chain.
    def display_topDapps(self,limit=50):
        return openbb.crypto.defi.gdapps(limit= limit)
    #Returns information about listed DeFi protocols, their current TVL and changes to it in the last hour/day/week.
    def defi_protocol_info(self):
        return openbb.crypto.defi.ldapps(limit = 100, sortby = "", ascend = False, description = False, drop_chain = True)
    #Scrape all substack newsletters from url list.
    def get_defi_newsletter(self):
        return openbb.crypto.defi.newsletters()
    #Get lastly added trade-able pairs on Uniswap with parameters like:
    def get_last_added_uniswap(self):
        return openbb.crypto.defi.pairs(last_days = 14, min_volume = 100, min_liquidity = 0, min_tx = 100)
    # Get uniswap pools by volume. [Source: https://thegraph.com/en/]
    def get_uniswap_pool(self):
        return openbb.crypto.defi.pools()
    #Get base statistics about Uniswap DEX. [Source: https://thegraph.com/en/]
    def get_stats_uniswap(self):
        return openbb.crypto.defi.stats()
    #Returns historical values of the total sum of TVLs from all listed protocols.
    def get_hist_tvl(self):
        stvl=openbb.crypto.defi.stvl()
        openbb.crypto.defi.stvl_chart(limit = 5, export = "hist_stvl.xlsx", sheet_name = None, external_axes = False)
        return stvl
    
    #Get the last 100 swaps done on Uniswap [Source: https://thegraph.com/en/]
    def get_100_swaps(self):
        return openbb.crypto.defi.swaps(limit = 100, sortby = "timestamp", ascend = False)
  
    #Get list of tokens trade-able on Uniswap DEX. [Source: https://thegraph.com/en/]
    def get_tokens_uniswap(self):
       return openbb.crypto.defi.tokens(skip = 0, limit= 100, sortby= "index", ascend = False)
    
    #Get DeFi Vaults Information. DeFi Vaults are pools of funds with an assigned strategy which main goal is to
    def get_vaults(self,chain='polygon',protocol='beefy',kind='lp'):
        return openbb.crypto.defi.vaults(chain =chain, protocol = protocol, kind =kind, ascend = True, sortby = "apy")
    
    def defi_utilities(self,price_changeA,price_changeB,proportion,initial_pool_value,apr,compounding_time):
        """
        Converts apr into apy
        Calculates Impermanent Loss in a custom liquidity pool

        Parameters
        ----------
        price_changeA :float
           price change of crypto A in percentage
        price_changeB : float
           price change of crypto B in percentage
        proportion : float
           percentage of first token in pool
        initial_pool_value : float
           initial value that pool contains
        apr : float
            value in percentage
        compounding_time : int
           number of compounded periods in a year

        Returns
        -------
        impermanent_loss : Tuple[pd.DataFrame, str]
            pd.DataFrame: dataframe with results
               - str: narrative version of results
        apy : Tuple[pd.DataFrame, str]
            - pd.DataFrame: dataframe with results
            - str: narrative version of results

        """
        impermanent_loss= openbb.crypto.tools.il(price_changeA, price_changeB, proportion, initial_pool_value)
        apy = openbb.crypto.tools.apy(apr, compounding_time)
        return impermanent_loss, apy


class NFT:
    
    def get_collections(self):
        return openbb.crypto.nft.collections()
    def get_nft_fp(self,slug):
        collections=openbb.crypto.nft.fp(slug)
        stats=openbb.crypto.nft.stats(slug)
        return collections,stats



# test
if __name__ == "__main__" :
    data = Coin('BTC',"2020-07-01", 1440,'Coingecko','binance')
