from telnetlib import AO
from src.config import ApiConfig
from src.util import ApiUtil
from datetime import datetime, date

from typing import List, Dict


class CoingeckoApi:

    def __init__(self, scheme: str = ApiConfig.Default.SCHEME, host: str = ApiConfig.Default.HOST, base_path: str = ApiConfig.Default.BASE_PATH, api_key: str = None):
        self._scheme = scheme
        self._host = host
        self._base_path = base_path
        self._api_key = api_key

    def get_ping(self) -> Dict:
        """Check API server status"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }
        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
                                           method="GET", path=ApiConfig.Url.PING, path_vars=path_vars, query_params=query_params)
        return response
        
    def get_simple_price(self,
                         coin_ids: List[str],
                         vs_currencies: List[str],
                         include_market_cap: bool = False,
                         include_24hr_vol: bool = False,
                         include_24hr_change: bool = False,
                         include_last_updated_at: bool = False) -> Dict:
        """Get the current price of any cryptocurrencies in any other supported currencies that you need.

        @coin_ids: Id of coins, comma-separated if querying more than 1 coin. Refers to get_coin_list
        @vs_currencies: vs_currency of coins, comma-separated if querying more than 1 vs_currency. Refers to get_supported_vs_currencies
        @include_market_cap: True/False to include market_cap. Default: False
        @include_24hr_vol: True/False to include 24hr_vol. Default: False
        @include_24hr_change: True/False to include 24hr_change. Default: False
        @include_last_updated_at: True/False to include last_updated_at. Default: False
        """

        path_vars = {}

        query_params = {
            "ids": ",".join(coin_ids),
            "vs_currencies": ",".join(vs_currencies),
            "include_market_cap": str(include_market_cap).lower(),
            "include_24hr_vol": str(include_24hr_vol).lower(),
            "include_24hr_change": str(include_24hr_change).lower(),
            "include_last_updated_at": str(include_last_updated_at).lower(),
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.SIMPLE_PRICE, path_vars=path_vars, query_params=query_params)

        return response

    def get_simple_token_price(self,
                               asset_platform_id: str,
                               contract_addresses: List[str],
                               vs_currencies: List[str],
                               include_market_cap: bool = False,
                               include_24hr_vol: bool = False,
                               include_24hr_change: bool = False,
                               include_last_updated_at: bool = False) -> Dict:
        """Get current price of tokens (using contract addresses) for a given platform in any other currency that you need.

        @asset_platform_id: The id of the platform issuing tokens (See asset_platforms endpoint for list of options)
        @contract_addresses: The contract address of tokens, comma separated 
        @vs_currencies: vs_currency of coins, comma-separated if querying more than 1 vs_currency. Refers to get_simple_supported_vs_currencies
        @include_market_cap: True/False to include market_cap. Default: False
        @include_24hr_vol: True/False to include 24hr_vol. Default: False
        @include_24hr_change: True/False to include 24hr_change. Default: False
        @include_last_updated_at: True/False to include last_updated_at. Default: False
        """

        path_vars = {
            "asset_platform_id": asset_platform_id
        }

        query_params = {
            "contract_addresses": ",".join(contract_addresses),
            "vs_currencies": ",".join(vs_currencies),
            "include_market_cap": str(include_market_cap).lower(),
            "include_24hr_vol": str(include_24hr_vol).lower(),
            "include_24hr_change": str(include_24hr_change).lower(),
            "include_last_updated_at": str(include_last_updated_at).lower(),
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.SIMPLE_TOKEN_PRICE, path_vars=path_vars, query_params=query_params)

        return response

    def get_simple_supported_vs_currencies(self) -> List[str]:
        """Get list of supported_vs_currencies. """

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.SIMPLE_SUPPORTED_VS_CURRENCIES, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_list(self, include_platform: bool = False) -> List[Dict]:
        """List all supported coins id, name and symbol (no pagination required). Use this to obtain all the coins' id in order to make API calls

        @include_platform: Flag to include platform contract addresses (eg. 0x.... for Ethereum based tokens). valid values: True/False Default: False
        """

        path_vars = {}

        query_params = {
            "include_platform": str(include_platform).lower(),
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_LIST, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_markets(self,
                         vs_currency: str,
                         coin_ids: List[str] = None,
                         category: str = None,
                         order: str = None,
                         per_page: int = None,
                         page: int = None,
                         sparkline: bool = False,
                         price_change_percentage: str = None) -> List[Dict]:
        """List all supported coins price, market cap, volume, and market related data. Use this to obtain all the coins market data (price, market cap, volume)

        @vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        @coin_ids: The ids of the coin, comma separated crytocurrency symbols (base). refers to get_coin_list. When left empty, returns numbers the coins observing the params `limit` and `start`
        @category: Filter by coin category, only decentralized_finance_defi is supported at the moment
        @order: Valid values: market_cap_desc, gecko_desc, gecko_asc, market_cap_asc, market_cap_desc, volume_asc, volume_desc, id_asc, id_desc sort results by field.
        @per_page: Valid values: 1..250Total results per page
        @page: Page through results
        @sparkline: Include sparkline 7 days data (eg. true, false)
        @price_change_percentage: Include price change percentage in 1h, 24h, 7d, 14d, 30d, 200d, 1y (eg. '`1h,24h,7d`' comma-separated, invalid values will be discarded)
        """

        path_vars = {}

        query_params = {
            "vs_currency": vs_currency,
            "ids": ",".join(coin_ids),
            "category": category,
            "order": order,
            "per_page": per_page,
            "page": page,
            "sparkline": str(sparkline).lower(),
            "price_change_percentage": price_change_percentage,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_MARKETS, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin(self,
                 coin_id: str,
                 localization: bool = True,
                 tickers: bool = True,
                 market_data: bool = True,
                 community_data: bool = True,
                 developer_data: bool = True,
                 sparkline: bool = False) -> Dict:
        """Get current data (name, price, market, ... including exchange tickers) for a coin.IMPORTANT: Ticker object is limited to 100 items, to get more tickers, use get_coin_tickers. Ticker 'is_stale' is true when ticker that has not been updated/unchanged from the exchange for a while. Ticker 'is_anomaly' is true if ticker's price is outliered by our system. You are responsible for managing how you want to display these information (e.g. footnote, different background, change opacity, hide)

        @coin_id: pass the coin id (can be obtained from get_coin_list) eg. bitcoin
        @localization: Include all localized languages in response (True/False) Default: True
        @tickers: Include tickers data (True/False) Default: True
        @market_data: Include market_data (True/False) Default: True
        @community_data: Include community_data data (True/False) Default: True
        @developer_data: Include developer_data data (True/False) Default: True
        @sparkline: Include sparkline 7 days data (True/False) Default: False
        """

        path_vars = {
            "coin_id": coin_id
        }

        query_params = {
            "localization": str(localization).lower(),
            "tickers": str(tickers).lower(),
            "market_data": str(market_data).lower(),
            "community_data": str(community_data).lower(),
            "developer_data": str(developer_data).lower(),
            "sparkline": str(sparkline).lower(),
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_tickers(self,
                         coin_id: str,
                         exchange_ids: List[str],
                         page: int = None,
                         order: str = "trust_score_desc",
                         include_exchange_logo: bool = False,
                         depth: bool = False) -> Dict:
        """Get coin tickers (paginated to 100 items) Ticker `is_stale` is true when ticker that has not been updated/unchanged from the exchange for a while.nTicker `is_anomaly` is true if ticker's price is outliered by our system.
            You are responsible for managing how you want to display these information (e.g. footnote, different background, change opacity, hide)

        @coin_id: pass the coin id (can be obtained from get_coin_list) eg. bitcoin
        @exchange_ids: filter results by exchange_ids
        @include_exchange_logo: flag to show exchange_logo
        @page: Page through results
        @order: valid values: trust_score_desc (default), trust_score_asc and volume_desc
        @depth: flag to show 2% orderbook depth. valid values: true, false
        """

        path_vars = {
            "coin_id": coin_id
        }

        query_params = {
            "exchange_ids": exchange_ids,
            "include_exchange_logo": include_exchange_logo,
            "page": page,
            "order": order,
            "depth": depth,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_TICKERS, path_vars=path_vars, query_params=query_params)
        return response

    def get_coin_history(self,
                         coin_id: str,
                         start_date: date,
                         localization: bool = False) -> Dict:
        """Get historical data (name, price, market, stats) at a given date for a coin 

        @coin_id: pass the coin id (can be obtained from get_coin_list) eg. bitcoin
        @date: The date of data snapshot in dd-mm-yyyy eg. 30-12-2017
        @localization: Set to false to exclude localized languages in response Default: False
        """

        path_vars = {
            "coin_id": coin_id
        }

        query_params = {
            "date": datetime.strftime(start_date, "%d-%m-%Y"),
            "localization": str(localization).lower(),
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_HISTORY, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_marketchart(self,
                             coin_id: str,
                             vs_currency: str,
                             days: int,
                             interval: str = None) -> Dict:
        """Get historical market data include price, market cap, and 24h volume (granularity auto) Minutely data will be used for duration within 1 day, Hourly data will be used for duration between 1 day and 90 days, Daily data will be used for duration above 90 days.

        @coin_id: pass the coin id (can be obtained from get_coin_list) eg. bitcoin
        @vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        @days: Data up to number of days ago (eg. 1,14,30,max)
        @interval: Data interval. Possible value: daily    
        """
        path_vars = {
            "coin_id": coin_id
        }

        query_params = {
            "vs_currency": vs_currency,
            "days": days,
            "interval": interval,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_MARKETCHART, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_marketchart_range(self,
                                   coin_id: str,
                                   vs_currency: str,
                                   from_date: datetime,
                                   to_date: datetime) -> Dict:
        """Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)Minutely data will be used for duration within 1 day, Hourly data will be used for duration between 1 day and 90 days, Daily data will be used for duration above 90 days.

        @coin_id: pass the coin id (can be obtained from get_coin_list) eg. bitcoin
        @vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        @from: From date
        @to: To date   
        """

        path_vars = {
            "coin_id": coin_id
        }

        query_params = {
            "vs_currency": vs_currency,
            "from": datetime.timestamp(from_date),
            "to": datetime.timestamp(to_date),
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_MARKETCHART_RANGE, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_status_updates(self,
                                coin_id: str,
                                per_page: int = 100,
                                page: int = 1) -> Dict:
        """Get status updates for a given coin

        @coin_id: pass the coin id (can be obtained from get_coin_list) eg. bitcoin
        @per_page: Total results per page Default: 100
        @page: Page through results Default: 1
        """

        path_vars = {
            "coin_id": coin_id,
        }

        query_params = {
            "per_page": per_page,
            "page": page,
            "x_cg_pro_api_key": self._api_key
        }

        header, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_STATUS_UPDATES, path_vars=path_vars, query_params=query_params)

        response["page"] = page
        response["per_page"] = int(header["Per-Page"])
        response["total"] = int(header["Total"])

        return response

    def get_coin_ohlc(self,
                      coin_id: str,
                      vs_currency: str,
                      days: int) -> List[Dict]:
        """Candle's body:1-2 days: 30 minutes 3-30 days: 4 hours 31 and before: 4 days

        @coin_id: Pass the coin id (can be obtained from get_coin_list) eg. bitcoin
        @vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        @days:  Data up to number of days ago (1/7/14/30/90/180/365)
        """
        path_vars = {
            "coin_id": coin_id
        }

        query_params = {
            "vs_currency": vs_currency,
            "days": days,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_OHLC, path_vars=path_vars, query_params=query_params)

        created_response = []
        for response_item in response:
            response_item_dict = {
                "date_time": response_item[0],
                "open": response_item[1],
                "close": response_item[2],
                "low": response_item[3],
                "high": response_item[4],
            }

            created_response.append(response_item_dict)

        return created_response

    def get_coin_contract(self,
                          asset_platform_id: str,
                          contract_address: str) -> Dict:
        """Get coin info from contract address

        @asset_platform_id: Asset platform (only `ethereum` is supported at this moment)
        @contract_address: Token's contract address
        """

        path_vars = {
            "asset_platform_id": asset_platform_id,
            "contract_address": contract_address
        }

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_CONTRACT, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_contract_market_chart(self,
                                       asset_platform_id: str,
                                       contract_address: str,
                                       vs_currency: str,
                                       days: int) -> Dict:
        """Get historical market data include price, market cap, and 24h volume (granularity auto)

        @asset_platform_id: The id of the platform issuing tokens (Only `ethereum` is supported for now)
        @contract_address: Token's contract address
        @vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        @days: Data up to number of days ago (eg. 1,14,30,max)
        """
        path_vars = {
            "asset_platform_id": asset_platform_id,
            "contract_address": contract_address
        }

        query_params = {
            "vs_currency": vs_currency,
            "days": days,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_CONTRACT_MARKET_CHART, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_contract_market_chart_range(self,
                                             asset_platform_id: str,
                                             contract_address: str,
                                             vs_currency: str,
                                             from_date: datetime,
                                             to_date: datetime) -> Dict:
        """Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)

        @asset_platform_id: The id of the platform issuing tokens (Only `ethereum` is supported for now)
        @contract_address: Token's contract address
        @vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        @from_date: From date
        @to_date: To date
        """

        path_vars = {
            "asset_platform_id": asset_platform_id,
            "contract_address": contract_address
        }

        query_params = {
            "vs_currency": vs_currency,
            "from": datetime.timestamp(from_date),
            "to": datetime.timestamp(to_date),
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_CONTRACT_MARKET_CHART_RANGE, path_vars=path_vars, query_params=query_params)

        return response

    def get_asset_platforms(self) -> List[Dict]:
        """List all asset platforms (Blockchain networks)"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.ASSET_PLATFORMS, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_category_list(self) -> List[Dict]:
        """List all categories"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_CATEGORY_LIST, path_vars=path_vars, query_params=query_params)

        return response

    def get_coin_categories(self, order: str = "market_cap_desc") -> List[Dict]:
        """List all categories with market data

        @order: Valid values: market_cap_desc (default), market_cap_asc, name_desc, name_asc, market_cap_change_24h_desc and market_cap_change_24h_asc
        """
        path_vars = {}

        query_params = {
            "order": order,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COIN_CATEGORIES, path_vars=path_vars, query_params=query_params)

        return response

    def get_exchanges(self,
                      page: int = 1,
                      per_page: int = 100) -> Dict:
        """List all exchanges

        @per_page: Valid values: 1...250 Total results per page Default value: 100
        @page: Page through results
        """
        path_vars = {}

        query_params = {
            "page": page,
            "per_page": per_page,
            "x_cg_pro_api_key": self._api_key
        }

        header, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.EXCHANGES, path_vars=path_vars, query_params=query_params)

        created_response = {
            "exchanges": response,
            "page": page,
            "per_page": int(header["per-page"]),
            "total": int(header["total"])
        }

        return created_response

    def get_exchange_list(self) -> List[Dict]:
        """List all supported markets id and name (no pagination required). Use this to obtain all the markets' id in order to make API calls"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.EXCHANGE_LIST, path_vars=path_vars, query_params=query_params)

        return response

    def get_exchange(self, exchange_id: str) -> Dict:
        """Get exchange volume in BTC and tickers: Ticker object is limited to 100 items, to get more tickers, use get_exchange_tickers Ticker `is_stale` is true when ticker that has not been updated/unchanged from the exchange for a while.
        Ticker `is_anomaly` is true if ticker's price is outliered by our system. You are responsible for managing how you want to display these information (e.g. footnote, different background, change opacity, hide)

        @exchange_id: Pass the exchange id (can be obtained from get_exchange_list) eg. binance
        """

        path_vars = {
            "exchange_id": exchange_id
        }

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.EXCHANGE, path_vars=path_vars, query_params=query_params)

        return response

    def get_exchange_tickers(self,
                             exchange_id: str,
                             coin_ids: List[str] = None,
                             page: int = 1,
                             include_exchange_logo: bool = False,
                             depth: str = None,
                             order: str = "trust_score_desc ") -> Dict:
        """Get exchange tickers (paginated) Ticker `is_stale` is true when ticker that has not been updated/unchanged from the exchange for a while. Ticker `is_anomaly` is true if ticker's price is outliered by our system.
        You are responsible for managing how you want to display these information (e.g. footnote, different background, change opacity, hide)

        @exchange_id: Pass the exchange id (can be obtained from get_exchange_list) eg. binance
        @coin_ids: Filter tickers by coin_ids (ref: get_exchange_list)
        @include_exchange_logo: Flag to show exchange_logo
        @page: Page through results
        @depth: Flag to show 2% orderbook depth valid_values cost_to_move_up_usd and cost_to_move_down_usd
        @order: Valid values: trust_score_desc (default), trust_score_asc and volume_desc
        """

        path_vars = {
            "exchange_id": exchange_id
        }

        query_params = {
            "coin_ids": coin_ids,
            "include_exchange_logo": str(include_exchange_logo).lower(),
            "page": page,
            "depth": depth,
            "order": order,
            "x_cg_pro_api_key": self._api_key
        }

        header, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.EXCHANGE_TICKERS, path_vars=path_vars, query_params=query_params)

        created_response = {
            "exchange_tickers": response,
            "page": page,
            "per_page": int(header["per-page"]),
            "total": int(header["total"])
        }
        return created_response

    def get_exchange_statusupdates(self,
                                   exchange_id: str,
                                   per_page: int = 100,
                                   page: int = 1) -> Dict:
        """Get status updates for a given exchange.

        @exchange_id: Pass the exchange id (can be obtained from get_exchange_list) eg. binance.
        @per_page: Total results per page Default: 100.
        @page: Page through results Default: 1.
        """
        path_vars = {
            "exchange_id": exchange_id
        }

        query_params = {
            "per_page": per_page,
            "page": page,
            "x_cg_pro_api_key": self._api_key
        }

        header, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.EXCHANGE_STATUSUPDATES, path_vars=path_vars, query_params=query_params)

        created_response = {
            "exchange_tickers": response,
            "page": page,
            "per_page": int(header["per-page"]),
            "total": int(header["total"]),
            "x_cg_pro_api_key": self._api_key
        }

        return created_response

    def get_exchange_volumechart(self, exchange_id: str, days: int) -> List[List]:
        """Get volume_chart data for a given exchange

        @exchange_id: Pass the exchange id (can be obtained from get_exchange_list) eg. binance
        @days: Data up to number of days ago (eg. 1,14,30)
        """

        path_vars = {
            "exchange_id": exchange_id
        }

        query_params = {
            "days": days,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.EXCHANGE_VOLUMECHART, path_vars=path_vars, query_params=query_params)

        created_response = []
        for response_item in response:
            response_item_dict = {
                "date_time": response_item[0],
                "volume_chart": float(response_item[1])
            }

            created_response.append(response_item_dict)
        return created_response

    def get_finance_platforms(self) -> List[Dict]:
        """List all finance platforms"""
        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.FINANCE_PLATFORMS, path_vars=path_vars, query_params=query_params)

        return response

    def get_finance_products(self,
                             start_at: datetime = None,
                             end_at: datetime = None,
                             per_page: int = 100,
                             page: int = 1) -> Dict:
        """List all finance products 

        @per_page: Total results per page
        @page: Page through results
        @start_at: Start date of the financial products
        @end_at: End date of the financial products
        """

        path_vars = {}

        query_params = {
            "per_page": per_page,
            "page": page,
            "start_at": None if not start_at else int(datetime.timestamp(start_at)),
            "end_at": None if not end_at else int(datetime.timestamp(end_at)),
            "x_cg_pro_api_key": self._api_key
        }

        header, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.FINANCE_PRODUCTS, path_vars=path_vars, query_params=query_params)

        created_response = {
            "finance_products": response,
            "page": page,
            "per_page": int(header["per-page"]),
            "total": int(header["total"])
        }
        return created_response

    def get_indexes(self,
                    per_page: int = 100,
                    page: int = 1) -> Dict:
        """List all market indexes 

        @per_page: Total results per page Default: 100
        @page: Page through results Default: 1
        """

        path_vars = {}

        query_params = {
            "per_page": per_page,
            "page": page,
            "x_cg_pro_api_key": self._api_key
        }

        header, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,

            method="GET", path=ApiConfig.Url.INDEXES, path_vars=path_vars, query_params=query_params)

        created_response = {
            "finance_products": response,
            "page": page,
            "per_page": int(header["per-page"]),
            "total": int(header["total"])
        }

        return created_response

    def get_index_market(self, market_id: str, index_id: str) -> Dict:
        """Get market index by market id and index id 

        @market_id: Pass the market id (can be obtained from get_exchange_list)
        @index_id: Pass the index id (can be obtained from get_index_list)
        """

        path_vars = {
            "market_id": market_id,
            "index_id": index_id
        }

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.INDEX_MARKET, path_vars=path_vars, query_params=query_params)
        return response

    def get_index_list(self) -> List[Dict]:
        """List market indexes id and name"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.INDEX_LIST, path_vars=path_vars, query_params=query_params)

        return response

    def get_derivatives(self, include_tickers: str = "unexpired"):
        """List all derivative tickers

        @include_tickers: ['all', 'unexpired'] - expired to show unexpired tickers, all to list all tickers Default: unexpired
        """

        path_vars = {}

        query_params = {
            "include_tickers": include_tickers,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.DERIVATIVES, path_vars=path_vars, query_params=query_params)

        return response

    def get_derivative_exchanges(self,
                                 order: str = None,
                                 per_page: int = 100,
                                 page: int = 1):
        """List all derivative exchanges 

        @order: Order results using following params name_asc，name_desc，open_interest_btc_asc，open_interest_btc_desc，trade_volume_24h_btc_asc，trade_volume_24h_btc_desc
        @per_page: Total results per page
        @page: Page through results
        """

        path_vars = {}

        query_params = {
            "order": order,
            "per_page": per_page,
            "page": page,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.DERIVATIVE_EXCHANGES, path_vars=path_vars, query_params=query_params)

        return response

    def get_derivative_exchange(self, exchange_id: str, include_tickers: List[str] = None) -> Dict:
        """Show derivative exchange data

        @exchange_id: Pass the exchange id (can be obtained from get_derivative_exchange_list) eg. bitmex
        @include_tickers: ['all', 'unexpired'] - expired to show unexpired tickers, all to list all tickers, None to omit tickers data in response
        """

        path_vars = {
            "exchange_id": exchange_id
        }

        query_params = {
            "include_tickers": None if not include_tickers else ",".join(include_tickers),
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.DERIVATIVE_EXCHANGE, path_vars=path_vars, query_params=query_params)

        return response

    def get_derivative_exchange_list(self) -> List[Dict]:
        """List all derivative exchanges name and identifier"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.DERIVATIVE_EXCHANGE_LIST, path_vars=path_vars, query_params=query_params)

        return response

    def get_status_update(self,
                          category: str,
                          project_type: str = None,
                          per_page: int = 100,
                          page: int = 1) -> Dict:
        """List all status_updates with data (description, category, created_at, user, user_title and pin) 

        @category: Filtered by category (eg. general, milestone, partnership, exchange_listing, software_release, fund_movement, new_listings, event)
        @project_type: Filtered by Project Type (eg. coin, market). If None returns both status from coins and markets.
        @per_page: Total results per page Default: 100
        @page: Page through results Default: 1
        """

        path_vars = {}

        query_params = {
            "category": category,
            "project_type": project_type,
            "per_page": per_page,
            "page": page,
            "x_cg_pro_api_key": self._api_key
        }

        header, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.STATUS_UPDATE, path_vars=path_vars, query_params=query_params)
        
        response["page"] = page
        response["per_page"] = int(header["per-page"])
        response["total"] = int(header["total"])

        return response

    def get_exchange_rates(self) -> Dict:
        """Get BTC-to-Currency exchange rates"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.EXCHANGE_RATES, path_vars=path_vars, query_params=query_params)

        return response

    def get_search(self, query: str) -> Dict:
        """Search for coins, categories and markets listed on CoinGecko ordered by largest Market Cap first

        @query: Search string
        """

        path_vars = {}

        query_params = {
            "query": query,
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.SEARCH, path_vars=path_vars, query_params=query_params)

        return response

    def get_search_trending(self):
        """Top-7 trending coins on CoinGecko as searched by users in the last 24 hours (Ordered by most popular first)"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.SEARCH_TRENDING, path_vars=path_vars, query_params=query_params)

        return response

    def get_global(self) -> Dict:
        """Get cryptocurrency global data"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.GLOBAL, path_vars=path_vars, query_params=query_params)

        return response

    def get_global_defi(self) -> Dict:
        """Get Top 100 Cryptocurrency Global Decentralized Finance(defi) data"""

        path_vars = {}

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.GLOBAL_DEFI, path_vars=path_vars, query_params=query_params)

        return response

    def get_companies_public_treasury(self, coin_id: str) -> Dict:
        """Get public companies bitcoin or ethereum holdings (Ordered by total holdings descending)

        @coin_id: Bitcoin or ethereum
        """

        path_vars = {
            "coin_id": coin_id
        }

        query_params = {
            "x_cg_pro_api_key": self._api_key
        }

        _, response = ApiUtil.send_request(scheme=self._scheme, host=self._host, base_path=self._base_path,
            method="GET", path=ApiConfig.Url.COMPANIES_PUBLIC_TREASURY, path_vars=path_vars, query_params=query_params)

        return response