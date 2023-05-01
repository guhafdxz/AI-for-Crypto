#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 20:55:48 2023

@author: crypto_2024
"""

from openbb_terminal.sdk import openbb

class QA:
    def __init__(self, data):
        self.data = data

    # Plots Auto and Partial Auto Correlation of returns and change in returns
    def plot_acf(self, target, symbol='', lags=15, external_axes=False):
        openbb.qa.acf(self.data, target, symbol, lags, external_axes)

    # Plots box and whisker plots
    def plot_box_whisper(self, target, symbol='', yearly=True, external_axes=False):
        openbb.qa.bw(self.data, target, symbol, yearly, external_axes)

    # plots cumulative distribution function
    def plot_cum_dist(self, target):
        openbb.qa.cdf(self.data, target, symbol="", export="", sheet_name=None, external_axes=False)

    # Plots Cumulative sum algorithm (CUSUM) to detect abrupt changes in data
    def plot_cumsum(self, target, threshold=5, drift=2.1):
        openbb.qa.cusum(self.data, target, threshold, drift, external_axes=False)

    # Perform seasonal decomposition
    def decompose_by_season(self, data):
        return openbb.qa.decompose(data, multiplicative=False)

    # Plots hist diagram
    def plot_hist(self, target, symbol='', bins=15):
        openbb.qa.hist(self.data, target, symbol, bins, external_axes=False)

    # Kurtosis Indicator
    def kurtosis(self, window=14):
        return openbb.qa.kurtosis(self.data, window)

    # Display line plot of data
    def Display_line(self, title='', log_y=True, markers_lines=None, ):
        openbb.qa.line(self.data, title, log_y, markers_lines, export="", sheet_name=None, external_axes=False)

    # Look at the distribution of returns and generate statistics on the relation to the normal curve.
    def normality(self, data):
        return openbb.qa.normality(data)

    # Get the omega series
    def omega(self, threshold_start=0, threshold_end=1.5):
        return openbb.qa.omega(self.data, threshold_start, threshold_end)

    # Plots QQ plot for data against normal quantiles
    def qqplot(self, target, symbol):
        return openbb.qa.qqplot(self.data, target, symbol, external_axes=False)

    # Return rolling mean and standard deviationv
    def rolling_mean_standard(self, data, window=14):
        return openbb.qa.rolling(data, window)

    # Calculates the sharpe ratio
    def sharp_ratio(self, rfr=0, window=252):
        return openbb.qa.sharpe(self.data, rfr, window)

    # Overlay Median & Quantile
    def quantitle(self, window=14, quantile_pct=0.5):
        return openbb.qa.quantile(self.data, window, quantile_pct)

    # Skewness Indicator
    def skew(self, window=14):
        return openbb.qa.skew(self.data, window)

    # Calculates the sortino ratio
    def sortino(self, target_return, window=252, adjusted=False):
        return openbb.qa.sortino(self.data, target_return, window, adjusted)

    # Deviation and Variance
    def spread(self, window=14):
        return openbb.qa.spread(self.data, window)

    # Summary of statistics
    def summary(self):
        return openbb.qa.summary(self.data)
class TA:
    def __init__(self, symbol, data):
        self.symbol = symbol
        self.data = data

    # Calculate AD technical indicator
    def ad(self, use_open=False):
        openbb.ta.ad_chart(self.data, use_open, symbol="", export="", sheet_name=None, external_axes=False)
        return openbb.ta.ad(self.data, use_open)  # Dataframe with technical indicator AD

    # Calculate AD oscillator technical indicator
    def ad_oscillator(self, use_open=False, fast=3, slow=10):
        openbb.ta.adosc_chart(self.data, fast, slow, use_open, symbol=self.symbol,
                              export="{} ad_oscillator.xlsx".format(self.symbol), sheet_name=None, external_axes=False)
        return openbb.ta.adosc(self.data, use_open, fast, slow)

    # ADX technical indicator
    def adx(self, window: int = 14, scalar: int = 100, drift: int = 1):
        openbb.ta.adx_chart(self.data, window, scalar, drift, self.symbol, export="{} adx.xlsx".format(self.symbol),
                            sheet_name=None, external_axes=False)
        return openbb.ta.adx(self.data, window, scalar, drift)

    # Aroon
    def aroon(self, window: int = 25, scalar: int = 100, symbol: str = "", export: str = "", sheet_name=None,
              external_axes: bool = False):
        openbb.ta.aroon_chart(self.data, window, scalar, symbol, export, sheet_name, external_axes)
        return openbb.ta.aroon(self.data, window, scalar)

    # Average True Range
    def atr(self, window: int = 14, mamode: str = "ema", offset: int = 0):
        openbb.ta.atr_chart(self.data, symbol="", window=14, mamode="sma", offset=0, export="", sheet_name=None,
                            external_axes=False)
        return openbb.ta.atr(self.data, window, mamode, offset)

    # Calculate Bollinger Bands

    def bbands(self, window: int = 15, n_std: float = 2, mamode: str = "ema"):
        openbb.ta.bbands_chart(self.data, n_std=2, window=15, mamode="sma", export="", sheet_name=None,
                               external_axes=False)
        return openbb.ta.bbands(self.data, window, n_std, mamode)

    # Commodity channel index

    def cci(self, window: int = 14, scalar: float = 0.0015):
        openbb.ta.cci_chart(self.data, window, scalar, symbol="", export="", sheet_name=None, external_axes=False)
        return openbb.ta.cci(self.data, window, scalar)

    def cg(self, values, window=14):
        openbb.ta.cg_chart(values, window, symbol="", export="", sheet_name=None, external_axes=False)
        return openbb.ta.cg(values, window)

    def clenow(self, values, window=90):
        openbb.ta.clenow_chart(values, window=window, symbol="", export="", sheet_name=None, external_axes=False)
        return openbb.ta.clenow(values, window)

    # Returns a DataFrame of realized volatility quantiles.
    def cones(self, lower_q: float = 0.25, upper_q: float = 0.75, is_crypto: bool = False, model: str = "STD"):
        openbb.ta.cones_chart(self.data, lower_q, upper_q, model, is_crypto=False, export="", sheet_name=None,
                              external_axes=False)
        return openbb.ta.cones(self.data, lower_q, upper_q, is_crypto, model)

    # Get the integer value for demark sequential indicator
    def demark(self, values, min_to_show: int = 5):
        openbb.ta.demark_chart(values, min_to_show, export="", sheet_name="", external_axes=False)
        return openbb.ta.demark(values)

    # plots donchian channels
    def donchian(self, upper_length=20, lower_length=20):
        openbb.ta.donchian_chart(self.data, symbol="", upper_length=20, lower_length=20, export="", sheet_name=None,
                                 external_axes=False)
        return openbb.ta.donchian(self.data, upper_length, lower_length)

    # Gets exponential moving average (EMA) for stock
    def ema(self, data, length: int = 50, offset: int = 0):
        return openbb.ta.ema(data, length, offset)

    # Calculate Fibonacci levels
    def fib(self, limit: int = 120, start_date=None, end_date=None):
        openbb.ta.fib_chart(self.data, limit, start_date, end_date, symbol="", export="", sheet_name=None,
                            external_axes=False)
        return openbb.ta.fib(self.data, limit, start_date, end_date)

    # Fisher Transform
    def fisher(self, window: int = 14):
        openbb.ta.fisher_chart(self.data, window, symbol="", export="", sheet_name=None, external_axes=False)
        return openbb.ta.fisher(self.data, window)

    # Gets hull moving average (HMA) for stock
    def hma(self, data, length: int = 50, offset: int = 0):
        return openbb.ta.hma(data, length, offset)

    # Keltner Channels
    def kc(self, window: int = 20, scalar: float = 2, mamode: str = "ema", offset: int = 0):
        openbb.ta.kc_chart(self.data, window, scalar, mamode, offset, symbol="", export="", sheet_name=None,
                           external_axes=False)
        return openbb.ta.kc(self.data, window, scalar, mamode, offset)

    # Plots MA technical indicator
    def ma(self, data, window=None, offset: int = 0, ma_type: str = "EMA"):
        openbb.ta.ma_chart(data, window, offset, ma_type, symbol="", export="", sheet_name=None, external_axes=False)
        return openbb.ta.ma(data, window, offset, ma_type)

        # Moving average convergence divergence

    def macd(self, data, n_fast: int = 12, n_slow: int = 26, n_signal: int = 9):
        openbb.ta.macd_chart(data, n_fast, n_slow, n_signal, symbol="", export="", sheet_name=None, external_axes=False)
        return openbb.ta.macd(data, n_fast, n_slow, n_signal)

    # On Balance Volume
    def obv(self):
        openbb.ta.obv_chart(self.data, symbol="", export="", sheet_name=None, external_axes=False)
        return openbb.ta.obv(self.data)

    # Relative strength index
    def rsi(self, data, window: int = 14, scalar: float = 100, drift: int = 1):
        openbb.ta.rsi_chart(data, window, scalar, drift, symbol="", export="", sheet_name=None, external_axes=False)
        return openbb.ta.rsi(data, window, scalar, drift)

    # Garman-Klass volatility extends Parkinson volatility by taking into account the opening and closing price.
    def rvol_garman_kclass(self, window: int = 30, trading_periods=None, is_crypto: bool = False, clean=True):
        return openbb.ta.rvol_garman_klass(self.data, window, trading_periods, is_crypto, clean)

    # Hodges-Tompkins volatility is a bias correction for estimation using an overlapping data sample.
    def rvol_hodges_tompkins(self, window: int = 30, trading_periods=None, is_crypto: bool = False, clean=True):
        return openbb.ta.rvol_hodges_tompkins(self.data, window, trading_periods, is_crypto, clean)

    # Parkinson's volatility uses the high and low price of the day rather than just close to close prices.

    def rvol_parkinson(self, window: int = 30, trading_periods=None, is_crypto: bool = False, clean=True):
        return openbb.ta.rvol_parkinson(self.data, window, trading_periods, is_crypto, clean)

    # Rogers-Satchell is an estimator for measuring the volatility with an average return not equal to zero.
    def rvol_rogers_satchell(self, window: int = 30, trading_periods=None, is_crypto: bool = False, clean=True):
        return openbb.ta.rvol_rogers_satchell(self.data, window, trading_periods, is_crypto, clean)

    # Standard deviation measures how widely returns are dispersed from the average return.
    def rvol_std(self, window: int = 30, trading_periods=None, is_crypto: bool = False, clean=True):
        return openbb.ta.rvol_std(self.data, window, trading_periods, is_crypto, clean)

    # Yang-Zhang volatility is the combination of the overnight (close-to-open volatility).
    def rvol_yang_zhang(self, window: int = 30, trading_periods=None, is_crypto: bool = False, clean=True):
        return openbb.ta.rvol_yang_zhang(self.data, window, trading_periods=None, is_crypto=False, clean=True)

    # Gets simple moving average (SMA) for stock
    def sma(self, values, length: int = 50, offset: int = 0):
        return openbb.ta.sma(values, length, offset)

    # Standard deviation measures how widely returns are dispersed from the average return.
    def standard_deviation(self, window: int = 30, trading_periods=None, is_crypto=False, clean=True):
        return openbb.ta.standard_deviation(self.data, window, trading_periods, is_crypto, clean)

    # Stochastic oscillator
    def stoch(self, fastkperiod: int = 14, slowdperiod: int = 3, slowkperiod: int = 3):
        openbb.ta.stoch_chart(self.data, fastkperiod, slowdperiod, slowkperiod, symbol="", export="", sheet_name=None,
                              external_axes=False)
        return openbb.ta.stoch(self.data, fastkperiod, slowdperiod, slowkperiod)

    # Gets volume weighted average price (VWAP)
    def vwap(self, start_date, end_date, offset=0):
        openbb.ta.vwap_chart(self.data, start_date, end_date, offset, symbol="", interval="", export="",
                             sheet_name=None, external_axes=False)
        return openbb.ta.vwap(self.data, offset)

    # Gets weighted moving average (WMA) for stock
    def wma(self, values, length: int = 50, offset: int = 0):
        return openbb.ta.wma(values, length, offset)

    # Gets zero-lagged exponential moving average (ZLEMA) for stock
    def zlma(self, values, length: int = 50, offset: int = 0):
        return openbb.ta.zlma(values, length, offset)