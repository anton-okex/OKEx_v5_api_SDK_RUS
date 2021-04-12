import okex.Account_api as Account
import okex.Funding_api as Funding
import okex.Market_api as Market
import okex.Public_api as Public
import okex.Trade_api as Trade
import okex.subAccount_api as SubAccount
import okex.status_api as Status
import json

if __name__ == '__main__':
    api_key = "your_API_key/ваш_API_ключ"
    secret_key = "your_secret_key/ваш_секретный_ключ"
    passphrase = "your_passphrase/ваша_секретная_фраза"
    # параметр flag используется для переключения между демо и реальным режимом
    # flag = '1'  #демо-режим
    flag = '0'  

    # account api/аутентификация и общие запросы по пользовательскому счетy
    accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)
    # get balance/получить баланс счета в BTC
    result = accountAPI.get_account('BTC')
    # get positions/получить позиции счета по BTC-USD фьючерсам 
    result = accountAPI.get_positions('FUTURES', 'BTC-USD-210402')
    # Get Account Configuration/конфигурация аккаунта
    result = accountAPI.get_account_config()
    # Get Position mode/получить режим исполнения позиции
    result = accountAPI.get_position_mode('long_short_mode')
    # Set Leverage/установка маржи кредитного плеча 
    result = accountAPI.set_leverage(instId='BTC-USD-210402', lever='10', mgnMode='cross')
    # Get Maximum Tradable Size For Instrument/получить максимально возможный размер для выбранного инструмента (фьючерс)  
    result = accountAPI.get_maximum_trade_size('BTC-USDT-210402', 'cross', 'USDT')
    # Get Maximum Available Tradable Amount/получить максимально возможную сумму для фьючерсной сделки 
    result = accountAPI.get_max_avail_size('BTC-USDT-210402', 'isolated', 'BTC')
    # Increase/Decrease margin/Увеличение/сокращение маржи
    result = accountAPI.Adjustment_margin('BTC-USDT-210409', 'long', 'add', '100')
    # Get Leverage/получить маржу кредитного плеча  
    result = accountAPI.get_leverage('BTC-USDT-210409', 'isolated')
    # Get the maximum loan of isolated MARGIN/получить максимальную ссуду изолированного кредитного плеча
    result = accountAPI.get_max_load('BTC-USDT', 'cross', 'BTC')
    # Get Fee Rates/получить размер комиссий
    result = accountAPI.get_fee_rates('FUTURES', '', category='1')
    # Get interest-accrued/получить начисленные проценты
    result = accountAPI.get_interest_accrued('BTC-USDT', 'BTC', 'isolated', '', '', '10')
    # Get Maximum Withdrawals/установить максимальный размер выводoв
    result = accountAPI.get_max_withdrawal('')

    # funding api/основной аккаунт
    fundingAPI = Funding.FundingAPI(api_key, secret_key, passphrase, False, flag)
    # Get Deposit Address/получить адрес для депозита
    result = fundingAPI.get_deposit_address('')
    # Get Balance/ получить баланс основного счета в BTC
    result = fundingAPI.get_balances('BTC')
    # Funds Transfer/сделать трансфер средств на субсчет
    result = fundingAPI.funds_transfer(ccy='', amt='', type='1', froms="", to="",subAcct='')
    # Withdrawal/сделать вывод средств
    result = fundingAPI.coin_withdraw('usdt', '2', '3', '', '', '0')
    # Get Deposit History/получить историю депозитов
    result = fundingAPI.get_deposit_history()
    # Get Withdrawal History/получить историю выводов
    result = fundingAPI.get_withdrawal_history()
    # Get Currencies/получить id валюты
    result = fundingAPI.get_currency()
    # PiggyBank Purchase/Redemption/получить выплату/приобрести в OKEx PiggyBank
    # result = fundingAPI.purchase_redempt('BTC', '1', 'purchase')

    # market api
    marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, flag)
    # 获取所有产品行情信息  Get Tickers
    # result = marketAPI.get_tickers('SPOT')
    # 获取单个产品行情信息  Get Ticker
    # result = marketAPI.get_ticker('BTC-USDT')
    # 获取指数行情  Get Index Tickers
    # result = marketAPI.get_index_ticker('BTC', 'BTC-USD')
    # 获取产品深度  Get Order Book
    # result = marketAPI.get_orderbook('BTC-USDT-210402', '400')
    # 获取所有交易产品K线数据  Get Candlesticks
    # result = marketAPI.get_candlesticks('BTC-USDT-210924', bar='1m')
    # 获取交易产品历史K线数据（仅主流币实盘数据）  Get Candlesticks History（top currencies in real-trading only）
    # result = marketAPI.get_history_candlesticks('BTC-USDT')
    # 获取指数K线数据  Get Index Candlesticks
    # result = marketAPI.get_index_candlesticks('BTC-USDT')
    # 获取标记价格K线数据  Get Mark Price Candlesticks
    # result = marketAPI.get_markprice_candlesticks('BTC-USDT')
    # 获取交易产品公共成交数据  Get Trades
    # result = marketAPI.get_trades('BTC-USDT', '400')

    # public api
    publicAPI = Public.PublicAPI(api_key, secret_key, passphrase, False, flag)
    # 获取交易产品基础信息  Get instrument
    # result = publicAPI.get_instruments('FUTURES', 'BTC-USDT')
    # 获取交割和行权记录  Get Delivery/Exercise History
    # result = publicAPI.get_deliver_history('FUTURES', 'BTC-USD')
    # 获取持仓总量  Get Open Interest
    # result = publicAPI.get_open_interest('SWAP')
    # 获取永续合约当前资金费率  Get Funding Rate
    # result = publicAPI.get_funding_rate('BTC-USD-SWAP')
    # 获取永续合约历史资金费率  Get Funding Rate History
    # result = publicAPI.funding_rate_history('BTC-USD-SWAP')
    # 获取限价  Get Limit Price
    # result = publicAPI.get_price_limit('BTC-USD-210402')
    # 获取期权定价  Get Option Market Data
    # result = publicAPI.get_opt_summary('BTC-USD')
    # 获取预估交割/行权价格  Get Estimated Delivery/Excercise Price
    # result = publicAPI.get_estimated_price('ETH-USD-210326')
    # 获取免息额度和币种折算率  Get Discount Rate And Interest-Free Quota
    # result = publicAPI.discount_interest_free_quota('')
    # 获取系统时间  Get System Time
    # result = publicAPI.get_system_time()
    # 获取平台公共爆仓单信息  Get Liquidation Orders
    # result = publicAPI.get_liquidation_orders('FUTURES', uly='BTC-USDT', alias='next_quarter', state='filled')
    # 获取标记价格  Get Mark Price
    # result = publicAPI.get_mark_price('FUTURES')

    # trade api
    tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase, False, flag)
    # 下单  Place Order
    # result = tradeAPI.place_order(instId='BTC-USDT-210326', tdMode='cross', side='sell', posSide='short',
    #                               ordType='market', sz='100')
    # 批量下单  Place Multiple Orders
    # result = tradeAPI.place_multiple_orders([
    #     {'instId': 'BTC-USD-210402', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17400',
    #      'posSide': 'long',
    #      'clOrdId': 'a12344', 'tag': 'test1210'},
    #     {'instId': 'BTC-USD-210409', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17359',
    #      'posSide': 'long',
    #      'clOrdId': 'a12344444', 'tag': 'test1211'}
    # ])

    # 撤单  Cancel Order
    # result = tradeAPI.cancel_order('BTC-USD-201225', '257164323454332928')
    # 批量撤单  Cancel Multiple Orders
    # result = tradeAPI.cancel_multiple_orders([
    #     {"instId": "BTC-USD-210402", "ordId": "297389358169071616"},
    #     {"instId": "BTC-USD-210409", "ordId": "297389358169071617"}
    # ])

    # 修改订单  Amend Order
    # result = tradeAPI.amend_order()
    # 批量修改订单  Amend Multiple Orders
    # result = tradeAPI.amend_multiple_orders(
    #     [{'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616434384896', 'newPx': '17880'},
    #      {'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616652488704', 'newPx': '17882'}
    #      ])

    # 市价仓位全平  Close Positions
    # result = tradeAPI.close_positions('BTC-USDT-210409', 'isolated', 'long', '')
    # 获取订单信息  Get Order Details
    # result = tradeAPI.get_orders('BTC-USD-201225', '257173039968825345')
    # 获取未成交订单列表  Get Order List
    # result = tradeAPI.get_order_list()
    # 获取历史订单记录（近七天） Get Order History (last 7 days）
    # result = tradeAPI.get_orders_history('FUTURES')
    # 获取历史订单记录（近三个月） Get Order History (last 3 months)
    # result = tradeAPI.orders_history_archive('FUTURES')
    # 获取成交明细  Get Transaction Details
    # result = tradeAPI.get_fills()
    # 策略委托下单  Place Algo Order
    # result = tradeAPI.place_algo_order('BTC-USDT-210409', 'isolated', 'buy', ordType='conditional',
                                       # sz='100',posSide='long', tpTriggerPx='60000', tpOrdPx='59999')
    # 撤销策略委托订单  Cancel Algo Order
    # result = tradeAPI.cancel_algo_order([{'algoId': '297394002194735104', 'instId': 'BTC-USDT-210409'}])
    # 获取未完成策略委托单列表  Get Algo Order List
    # result = tradeAPI.order_algos_list('conditional', instType='FUTURES')
    # 获取历史策略委托单列表  Get Algo Order History
    # result = tradeAPI.order_algos_history('conditional', 'canceled', instType='FUTURES')

    # 子账户API subAccount
    subAccountAPI = SubAccount.SubAccountAPI(api_key, secret_key, passphrase, False, flag)
    # 查询子账户的交易账户余额(适用于母账户) Query detailed balance info of Trading Account of a sub-account via the master account
    # result = subAccountAPI.balances(subAcct='')
    # 查询子账户转账记录(仅适用于母账户) History of sub-account transfer(applies to master accounts only)
    # result = subAccountAPI.bills()
    # 删除子账户APIKey(仅适用于母账户) Delete the APIkey of sub-accounts (applies to master accounts only)
    # result = subAccountAPI.delete(pwd='', subAcct='', apiKey='')
    # 重置子账户的APIKey(仅适用于母账户) Reset the APIkey of a sub-account(applies to master accounts only)
    # result = subAccountAPI.reset(pwd='', subAcct='', label='', apiKey='', perm='')
    # 创建子账户的APIKey(仅适用于母账户) Create an APIkey for a sub-account(applies to master accounts only)
    # result = subAccountAPI.create(pwd='123456', subAcct='', label='', Passphrase='')
    # 查看子账户列表(仅适用于母账户) View sub-account list(applies to master accounts only)
    # result = subAccountAPI.view_list()
    # 母账户控制子账户与子账户之间划转（仅适用于母账户）manage the transfers between sub-accounts(applies to master accounts only)
    # result = subAccountAPI.control_transfer(ccy='', amt='', froms='', to='', fromSubAccount='', toSubAccount='')

    # 系统状态API(仅适用于实盘) system status
    Status = Status.StatusAPI(api_key, secret_key, passphrase, False, flag)
    # 查看系统的升级状态
    # result = Status.status()

    print(json.dumps(result))
