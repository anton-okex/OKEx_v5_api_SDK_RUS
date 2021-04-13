# Code examples for the OKEx V5 API (REST)
# Примеры команд для OKEx V5 API (REST)

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
    flag = '0'  #реальн

    # account api/аутентификация и общие запросы по пользовательскому счетy
    accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)
    # get balance/получить баланс счета в BTC
    result = accountAPI.get_account('BTC')
    # get positions/получить позиции счета (BTC-USD, фьючерс)
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
    # Get Fee Rates/получить размер комиссий (фьючерс)
    result = accountAPI.get_fee_rates('FUTURES', '', category='1')
    # Get interest-accrued/получить начисленные проценты (BTC-USDT)
    result = accountAPI.get_interest_accrued('BTC-USDT', 'BTC', 'isolated', '', '', '10')
    # Get Maximum Withdrawals/установить максимальный размер выводoв
    result = accountAPI.get_max_withdrawal('')

    # funding api/основной аккаунт
    fundingAPI = Funding.FundingAPI(api_key, secret_key, passphrase, False, flag)
    # Get Deposit Address/получить адрес для депозита
    result = fundingAPI.get_deposit_address('')
    # Get Balance/ получить баланс основного счета (в BTC)
    result = fundingAPI.get_balances('BTC')
    # Funds Transfer/сделать трансфер средств на субсчет
    result = fundingAPI.funds_transfer(ccy='', amt='', type='1', froms="", to="",subAcct='')
    # Withdrawal/сделать вывод средств (USDT)
    result = fundingAPI.coin_withdraw('usdt', '2', '3', '', '', '0')
    # Get Deposit History/получить историю депозитов
    result = fundingAPI.get_deposit_history()
    # Get Withdrawal History/получить историю выводов
    result = fundingAPI.get_withdrawal_history()
    # Get Currencies/получить id валюты
    result = fundingAPI.get_currency()
    # PiggyBank Purchase/Redemption/получить выплату/приобрести в OKEx PiggyBank
    result = fundingAPI.purchase_redempt('BTC', '1', 'purchase')

    # market api/рыночный API
    marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, flag)
    # Get Tickers/получить ВСЕ тикеры валют на спот рынке
    result = marketAPI.get_tickers('SPOT')
    # Get Ticker/получить тикер пары (BTC-USDT)
    result = marketAPI.get_ticker('BTC-USDT')
    # Get Index Tickers/получить индексный тикер в паре (BTC-USDT)
    result = marketAPI.get_index_ticker('BTC', 'BTC-USD')
    # Get Order Book/получить информацию по OrderBook (BTC-USDT)
    result = marketAPI.get_orderbook('BTC-USDT-210402', '400')
    # Get Candlesticks/получить информацию по свечам (BTC-USDT)
    result = marketAPI.get_candlesticks('BTC-USDT-210924', bar='1m')
    # Get Candlesticks History（top currencies in real-trading only/получить историю по свечам (недоступно в демо-режиме)
    result = marketAPI.get_history_candlesticks('BTC-USDT')
    # Get Index Candlesticks/получить информацию по свечам (индекс)
    result = marketAPI.get_index_candlesticks('BTC-USDT')
    # Get Trades/получить информацию по сделкам (BTC-USDT, 400)
    result = marketAPI.get_trades('BTC-USDT', '400')

    # public api/публичный API
    publicAPI = Public.PublicAPI(api_key, secret_key, passphrase, False, flag)
    # Get instrument/получить информацию по трейдинговому инструменту (фьючерс, BTC-USDT)
    result = publicAPI.get_instruments('FUTURES', 'BTC-USDT')
    # Get Delivery/Exercise History/получить историю по инструменту/паре (фьючерс, BTC-USDT)
    result = publicAPI.get_deliver_history('FUTURES', 'BTC-USD')
    # Get Open Interest/получить информацию по открытым позициям (своп)
    result = publicAPI.get_open_interest('SWAP')
    # Get Funding Rate/получить информацию по текущей ставке (BTC-USDT, своп)
    result = publicAPI.get_funding_rate('BTC-USD-SWAP')
    # Get Funding Rate History/получить информацию по истории ставки (BTC-USDT, своп)
    result = publicAPI.funding_rate_history('BTC-USD-SWAP')
    # Get Limit Price/получить цену лимита (BTC-USDT)
    result = publicAPI.get_price_limit('BTC-USD-210402')
    # Get Option Market Data/получить рыночные данные по опционам (BTC-USD)
    result = publicAPI.get_opt_summary('BTC-USD')
    # Get Estimated Delivery/Excercise Price/получить цену исполнения (ETH-USD)
    result = publicAPI.get_estimated_price('ETH-USD-210326')
    # Get Discount Rate And Interest-Free Quota/получить информацию по ставке и беспроцентной квоте
    result = publicAPI.discount_interest_free_quota('')
    # Get System Time/системное время
    result = publicAPI.get_system_time()
    # Get Liquidation Orders/получить информацию по ликвидационным ордерам (фьючерс, BTC-USDT)
    result = publicAPI.get_liquidation_orders('FUTURES', uly='BTC-USDT', alias='next_quarter', state='filled')
    # Get Mark Price/получить информацию по цене отметки инструмента (фьючерс)
    result = publicAPI.get_mark_price('FUTURES')

    # trade api/торговый API
    tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase, False, flag)
    # Place Order/поставить ордер 
    result = tradeAPI.place_order(instId='BTC-USDT-210326', tdMode='cross', side='sell', posSide='short',
                                    ordType='market', sz='100')
    # Place Multiple Orders/поставить несколько ордеров
    result = tradeAPI.place_multiple_orders([
          {'instId': 'BTC-USD-210402', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17400',
           'posSide': 'long',
           'clOrdId': 'a12344', 'tag': 'test1210'},
          {'instId': 'BTC-USD-210409', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17359',
           'posSide': 'long',
           'clOrdId': 'a12344444', 'tag': 'test1211'}
      ])

    # Cancel Order/oтменить ордер
    result = tradeAPI.cancel_order('BTC-USD-201225', '257164323454332928')
    # Cancel Multiple Orders/oтменить несколько ордеров
    result = tradeAPI.cancel_multiple_orders([
          {"instId": "BTC-USD-210402", "ordId": "297389358169071616"},
          {"instId": "BTC-USD-210409", "ordId": "297389358169071617"}
      ])

    # Amend Order/изменить ордер
    result = tradeAPI.amend_order()
    #   Amend Multiple Orders/изменить несколько ордеров
    result = tradeAPI.amend_multiple_orders(
          [{'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616434384896', 'newPx': '17880'},
           {'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616652488704', 'newPx': '17882'}
           ])

    # Close Positions/закрыть позицию
    result = tradeAPI.close_positions('BTC-USDT-210409', 'isolated', 'long', '')
    # Get Order Details/получить информацию по конкретному ордеру
    result = tradeAPI.get_orders('BTC-USD-201225', '257173039968825345')
    # Get Order List/получить список ордеров
    result = tradeAPI.get_order_list()
    # Get Order History (last 7 days/получить историю ордеров (последние 7 дней, фьючерс)
    result = tradeAPI.get_orders_history('FUTURES')
    # Get Order History (last 3 months)/получить историю ордеров (последние 3 месяца, фьючерс)
    result = tradeAPI.orders_history_archive('FUTURES')
    # Get Transaction Details/получить историю транзакций
    result = tradeAPI.get_fills()
    # Place Algo Order/пример постановки алгоритмического ордера
    result = tradeAPI.place_algo_order('BTC-USDT-210409', 'isolated', 'buy', ordType='conditional',
                                         sz='100',posSide='long', tpTriggerPx='60000', tpOrdPx='59999')
    # Cancel Algo Order/отменить алгоритмический ордер
    result = tradeAPI.cancel_algo_order([{'algoId': '297394002194735104', 'instId': 'BTC-USDT-210409'}])
    # Get Algo Order List/получить список алгоритмических ордеров
    result = tradeAPI.order_algos_list('conditional', instType='FUTURES')
    # Get Algo Order History/получить историю алгоритмических ордеров
    result = tradeAPI.order_algos_history('conditional', 'canceled', instType='FUTURES')

    # API subAccount/API субсчетoв
    subAccountAPI = SubAccount.SubAccountAPI(api_key, secret_key, passphrase, False, flag)
    # Query detailed balance info of Trading Account of a sub-account via the master account/получить подробную информацию о балансе субсчета через основной счет
    result = subAccountAPI.balances(subAcct='')
    # History of sub-account transfer(applies to master accounts only)/получить историю трансферов всех субсчетов (работает только с основного счета)
    result = subAccountAPI.bills()
    # Delete the APIkey of sub-accounts (applies to master accounts only)/удалить API ключ субсчета (работает только с основного счета)
    result = subAccountAPI.delete(pwd='', subAcct='', apiKey='')
    # Reset the APIkey of a sub-account(applies to master accounts only)/сбросить API ключ субсчета (работает только с основного счета)
    result = subAccountAPI.reset(pwd='', subAcct='', label='', apiKey='', perm='')
    # Create an APIkey for a sub-account(applies to master accounts only)/создать API ключ субсчета (работает только с основного счета)
    result = subAccountAPI.create(pwd='123456', subAcct='', label='', Passphrase='')
    # View sub-account list(applies to master accounts only)/получить список субсчетов (работает только с основного счета)
    result = subAccountAPI.view_list()
    # manage the transfers between sub-accounts(applies to master accounts only)/управление трансферами между субсчетами (работает только с основного счета)
    result = subAccountAPI.control_transfer(ccy='', amt='', froms='', to='', fromSubAccount='', toSubAccount='')

    # system status/статус системы
    Status = Status.StatusAPI(api_key, secret_key, passphrase, False, flag)
    result = Status.status()

    #print/execute any of the above queries/вывести/исполнить любую из упомянутых команд
    print(json.dumps(result))
