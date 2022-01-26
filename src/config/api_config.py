class ApiConfig:
    class Url:
        PING = "/ping"
        SIMPLE_PRICE = "/simple/price"
        SIMPLE_TOKEN_PRICE = "/simple/token_price/{asset_platform_id}"
        SIMPLE_SUPPORTED_VS_CURRENCIES = "/simple/supported_vs_currencies"
        COIN_LIST = "/coins/list"
        COIN_MARKETS = "/coins/markets"
        COIN = "/coins/{coin_id}"
        COIN_TICKERS = "/coins/{coin_id}/tickers"
        COIN_HISTORY = "/coins/{coin_id}/history"
        COIN_MARKETCHART = "/coins/{coin_id}/market_chart"
        COIN_MARKETCHART_RANGE = "/coins/{coin_id}/market_chart/range"
        COIN_STATUS_UPDATES = "/coins/{coin_id}/status_updates"
        COIN_OHLC = "/coins/{coin_id}/ohlc"
        COIN_CONTRACT = "/coins/{asset_platform_id}/contract/{contract_address}"
        COIN_CONTRACT_MARKET_CHART = "/coins/{asset_platform_id}/contract/{contract_address}/market_chart/"
        COIN_CONTRACT_MARKET_CHART_RANGE = "/coins/{asset_platform_id}/contract/{contract_address}/market_chart/range"
        ASSET_PLATFORMS = "/asset_platforms"
        COIN_CATEGORY_LIST = "/coins/categories/list"
        COIN_CATEGORIES = "/coins/categories"
        EXCHANGES = "/exchanges"
        EXCHANGE_LIST = "/exchanges/list"
        EXCHANGE = "/exchanges/{exchange_id}"
        EXCHANGE_TICKERS = "/exchanges/{exchange_id}/tickers"
        EXCHANGE_STATUSUPDATES = "/exchanges/{exchange_id}/status_updates"
        EXCHANGE_VOLUMECHART = "/exchanges/{exchange_id}/volume_chart"
        FINANCE_PLATFORMS = "/finance_platforms"
        FINANCE_PRODUCTS = "/finance_products"
        INDEXES = "/indexes"
        INDEX_MARKET = "/indexes/{market_id}/{index_id}"
        INDEX_LIST = "/indexes/list"
        DERIVATIVES = "/derivatives"
        DERIVATIVE_EXCHANGES = "/derivatives/exchanges"
        DERIVATIVE_EXCHANGE = "/derivatives/exchanges/{exchange_id}"
        DERIVATIVE_EXCHANGE_LIST = "/derivatives/exchanges/list"
        STATUS_UPDATE = "/status_updates"
        EXCHANGE_RATES = "/exchange_rates"
        SEARCH = "/search"
        SEARCH_TRENDING = "/search/trending"
        GLOBAL = "/global"
        GLOBAL_DEFI = "/global/decentralized_finance_defi"
        COMPANIES_PUBLIC_TREASURY = "/companies/public_treasury/{coin_id}"

    class Default:
        SCHEME = "https"
        HOST = "api.coingecko.com"
        BASE_PATH = "/api/v3"
