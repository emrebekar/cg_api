from src.api.coingecko_api import CoingeckoApi
from datetime import datetime
from typing import Dict
import unittest

class Tests(unittest.TestCase):

    def test_get_ping(self):
        cg = CoingeckoApi()
        ping_result = cg.get_ping()
        assert(isinstance(ping_result, Dict))

# Simple
    def test_get_simple_price(self):
        cg = CoingeckoApi()
        simple_price_result = cg.get_simple_price(coin_ids=["bitcoin"], vs_currencies=["usd"], include_24hr_change=True, include_24hr_vol=True, include_last_updated_at=True, include_market_cap=True)
        assert isinstance(simple_price_result, Dict)
    
    def test_get_simple_token_price(self):
        cg = CoingeckoApi()
        simple_token_price_result = cg.get_simple_token_price(asset_platform_id="tron", contract_addresses=["TLvDJcvKJDi3QuHgFbJC6SeTj3UacmtQU3"], vs_currencies=["usd"])
        assert isinstance(simple_token_price_result, Dict)

    def test_get_simple_supported_vs_currencies(self):
        cg = CoingeckoApi()
        simple_supported_vs_currencies_result = cg.get_simple_supported_vs_currencies()
        assert all(isinstance(s, str) for s in simple_supported_vs_currencies_result)

# Coins
    def test_get_coin_list(self):
        cg = CoingeckoApi()
        coin_list_result = cg.get_coin_list()
        assert  all(isinstance(s, Dict) for s in coin_list_result)

    def test_get_coin_markets(self):
        cg = CoingeckoApi()
        coin_market_result = cg.get_coin_markets(coin_ids=["bitcoin"], vs_currency="usd")
        assert all(isinstance(s, Dict) for s in coin_market_result)

    def test_get_coin(self):
        cg = CoingeckoApi()
        coin_result = cg.get_coin(coin_id="bitcoin")
        assert isinstance(coin_result, Dict)

    def test_get_coin_tickers(self):
        cg = CoingeckoApi()
        coin_tickers_result = cg.get_coin_tickers(coin_id="bitcoin", exchange_ids=["huobi", "binance"])
        assert isinstance(coin_tickers_result, Dict)

    def test_get_coin_history(self):
        cg = CoingeckoApi()
        coin_history_result = cg.get_coin_history(coin_id="bitcoin", start_date=datetime(day=1, month=2, year=2021))
        assert isinstance(coin_history_result, Dict)
    
    def test_get_coin_marketchart(self):
        cg = CoingeckoApi()
        coin_marketchart_result = cg.get_coin_marketchart(coin_id="bitcoin", vs_currency="usd", days="14")
        assert isinstance(coin_marketchart_result, Dict)
    
    def test_get_coin_marketchart_range(self):
        cg = CoingeckoApi()
        coin_marketchart_range_result = cg.get_coin_marketchart_range(coin_id="bitcoin", vs_currency="usd", from_date=datetime(day=1, month=2, year=2021), to_date=datetime(day=1, month=2, year=2022))
        assert isinstance(coin_marketchart_range_result, Dict)

    def test_get_coin_status_updates(self):
        cg = CoingeckoApi()
        coin_status_updates_result = cg.get_coin_status_updates(coin_id="bitcoin")
        assert isinstance(coin_status_updates_result, Dict)

    def test_get_coin_ohlc(self):
        cg = CoingeckoApi()
        coin_ohlc_result = cg.get_coin_ohlc(coin_id="bitcoin", vs_currency="usd", days=30)
        assert all(isinstance(s, Dict) for s in coin_ohlc_result)
    
    # Contract
    def test_get_coin_contract(self):
        cg = CoingeckoApi()
        coin_contract_result = cg.get_coin_contract(asset_platform_id="tron", contract_address="TLvDJcvKJDi3QuHgFbJC6SeTj3UacmtQU3")
        assert isinstance(coin_contract_result, Dict)

    def test_get_coin_contract_market_chart(self):
        cg = CoingeckoApi()
        coin_contract_market_result = cg.get_coin_contract_market_chart(asset_platform_id="tron", contract_address="TLvDJcvKJDi3QuHgFbJC6SeTj3UacmtQU3", vs_currency="usd", days=30)
        assert isinstance(coin_contract_market_result, Dict)

    def test_get_coin_contract_market_chart_range(self):
        cg = CoingeckoApi()
        coin_contract_market_range_result = cg.get_coin_contract_market_chart_range(asset_platform_id="tron", contract_address="TLvDJcvKJDi3QuHgFbJC6SeTj3UacmtQU3", vs_currency="usd", from_date=datetime(day=1, month=2, year=2021), to_date=datetime(day=1, month=2, year=2022))
        assert isinstance(coin_contract_market_range_result, Dict)

    # Asset Platforms
    def test_asset_platforms(self):
        cg = CoingeckoApi()
        asset_platforms_result = cg.get_asset_platforms()
        assert all(isinstance(s, Dict) for s in asset_platforms_result)

    # Categories
    def test_get_coin_category_list(self):
        cg = CoingeckoApi()
        coin_categories_list_result = cg.get_coin_category_list()
        assert all(isinstance(s, Dict) for s in coin_categories_list_result)

    def test_get_coin_categories(self):
        cg = CoingeckoApi()
        coin_categories_result = cg.get_coin_categories()
        assert all(isinstance(s, Dict) for s in coin_categories_result)

    # Exchanges
    def test_get_exchanges(self):
        cg = CoingeckoApi()
        exchanges_result = cg.get_exchanges()
        assert isinstance(exchanges_result, Dict)

    def test_get_exchange_list(self):
        cg = CoingeckoApi()
        exchange_list_result = cg.get_exchange_list()
        assert all(isinstance(s, Dict) for s in exchange_list_result)

    def test_get_exchange(self):
        cg = CoingeckoApi()
        exchange_result = cg.get_exchange(exchange_id="binance")
        assert isinstance(exchange_result, Dict) 

    def test_get_exchange_tickers(self):
        cg = CoingeckoApi()
        exchange_tickers_result = cg.get_exchange_tickers(exchange_id="binance")
        assert isinstance(exchange_tickers_result, Dict) 

    def test_get_exchange_volumechart(self):
        cg = CoingeckoApi()
        exchange_volumechart_result = cg.get_exchange_volumechart(exchange_id="binance", days=30)
        assert all(isinstance(s, Dict) for s in exchange_volumechart_result)

    def test_get_exchange_statusupdates(self):
        cg = CoingeckoApi()
        exchange_statusupdates_result = cg.get_exchange_statusupdates(exchange_id="binance")
        assert isinstance(exchange_statusupdates_result, Dict) 

    # Finance
    def test_finance_platforms(self):
        cg = CoingeckoApi()
        finance_platforms_result = cg.get_finance_platforms()
        assert all(isinstance(s, Dict) for s in finance_platforms_result)

    def test_get_finance_products(self):
        cg = CoingeckoApi()
        finance_products_result = cg.get_finance_products()
        assert isinstance(finance_products_result, Dict) 
    
    # Indexes
    def test_get_indexes(self):
        cg = CoingeckoApi()
        indexes_result = cg.get_indexes()
        assert isinstance(indexes_result, Dict) 

    def test_get_index_market(self):
        cg = CoingeckoApi()
        index_market_result = cg.get_index_market(market_id="jex_futures", index_id="EOS")
        assert isinstance(index_market_result, Dict)

    def test_get_index_list(self):
        cg = CoingeckoApi()
        index_list_result = cg.get_index_list()
        assert all(isinstance(s, Dict) for s in index_list_result)

    # Derivatives
    def test_get_derivatives(self):
        cg = CoingeckoApi()
        derivatives_result = cg.get_derivatives()
        assert all(isinstance(s, Dict) for s in derivatives_result)

    def test_get_derivative_exchanges(self):
        cg = CoingeckoApi()
        derivative_exchanges_result = cg.get_derivative_exchanges()
        assert all(isinstance(s, Dict) for s in derivative_exchanges_result)

    def test_get_derivative_exchange(self):
        cg = CoingeckoApi()
        derivative_exchange_result = cg.get_derivative_exchange(exchange_id="binance_futures")
        assert isinstance(derivative_exchange_result, Dict)

    def test_get_derivative_exchange_list(self):
        cg = CoingeckoApi()
        derivative_exchange_list_result = cg.get_derivative_exchange_list()
        assert all(isinstance(s, Dict) for s in derivative_exchange_list_result)

    # Status Updates
    def test_get_status_update(self):
        cg = CoingeckoApi()
        status_update_result = cg.get_status_update(category="general")
        assert isinstance(status_update_result, Dict)

    # Exchange Rates
    def test_get_exchange_rates(self):
        cg = CoingeckoApi()
        exchange_rates_result = cg.get_status_update(category="general")
        assert isinstance(exchange_rates_result, Dict)

    # Search
    def test_get_search(self):
        cg = CoingeckoApi()
        search_result = cg.get_search(query="Binance")
        assert isinstance(search_result, Dict)

    # Trendings
    def test_get_search_trending(self):
        cg = CoingeckoApi()
        search_trending_result = cg.get_search_trending()
        assert isinstance(search_trending_result, Dict)
    
    # Global
    def test_get_global(self):
        cg = CoingeckoApi()
        global_result = cg.get_global()
        assert isinstance(global_result, Dict)

    def test_get_global_defi(self):
        cg = CoingeckoApi()
        global_defi_result = cg.get_global_defi()
        assert isinstance(global_defi_result, Dict)

    # Companies (Beta)
    def test_get_companies_public_treasury(self):
        cg = CoingeckoApi()
        companies_public_teasury_result = cg.get_companies_public_treasury(coin_id="bitcoin")
        assert isinstance(companies_public_teasury_result, Dict)

