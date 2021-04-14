# Примеры команд для OKEx V5 API (REST)
# Code examples for the OKEx V5 API (REST)

import okex.Account_api as Account
import okex.Funding_api as Funding
import okex.Market_api as Market
import okex.Public_api as Public
import okex.Trade_api as Trade
import okex.subAccount_api as SubAccount
import okex.status_api as Status
import json

if __name__ == '__main__':
    api_key = "ваш_API_ключ/your_API_key"
    secret_key = "ваш_секретный_ключ/your_secret_key"
    passphrase = "ваша_секретная_фраза/your_passphrase"
    # параметр flag используется для переключения между демо и реальным режимом
    # flag = '1'  #демо-режим
    flag = '0'  #реальны

    # аутентификация и общие запросы по аккаунту / account api
    accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)
    # получить баланс аккаунтa в BTC / get balance
    result = accountAPI.get_account('BTC')
    # получить позиции аккаунтa (BTC-USD, фьючерс) / get positions
    result = accountAPI.get_positions('FUTURES', 'BTC-USD-210402')
    # конфигурация аккаунта / get account configuration
    result = accountAPI.get_account_config()
    # получить режим исполнения позиции / get position mode
    result = accountAPI.get_position_mode('long_short_mode')
    # установка маржи кредитного плеча / set leverage 
    result = accountAPI.set_leverage(instId='BTC-USD-210402', lever='10', mgnMode='cross')
    # получить максимально возможный размер для выбранного инструмента (фьючерс) / get maximum tradable size for instrument 
    result = accountAPI.get_maximum_trade_size('BTC-USDT-210402', 'cross', 'USDT')
    # получить максимально возможную сумму для сделки (фьючерс) / get maximum available tradable amount
    result = accountAPI.get_max_avail_size('BTC-USDT-210402', 'isolated', 'BTC')
    # yвеличение/сокращение маржи / increase/decrease margin
    result = accountAPI.Adjustment_margin('BTC-USDT-210409', 'long', 'add', '100')
    # получить маржу / get leverage 
    result = accountAPI.get_leverage('BTC-USDT-210409', 'isolated')
    # получить максимальную ссуду изолированной маржи / get the maximum loan of isolated MARGIN
    result = accountAPI.get_max_load('BTC-USDT', 'cross', 'BTC')
    # получить размер комиссий (фьючерс) / get fee rates
    result = accountAPI.get_fee_rates('FUTURES', '', category='1')
    # получить начисленные проценты (BTC-USDT) / get interest-accrued
    result = accountAPI.get_interest_accrued('BTC-USDT', 'BTC', 'isolated', '', '', '10')
    # установить максимальный размер выводoв / get maximum withdrawals
    result = accountAPI.get_max_withdrawal('')

    # основной аккаунт / funding api
    fundingAPI = Funding.FundingAPI(api_key, secret_key, passphrase, False, flag)
    # получить адрес для депозита / get deposit address
    result = fundingAPI.get_deposit_address('')
    # получить баланс основного аккаунтa (в BTC) / get balance
    result = fundingAPI.get_balances('BTC')
    # сделать трансфер средств на субаккаунт / funds transfer
    result = fundingAPI.funds_transfer(ccy='', amt='', type='1', froms="", to="",subAcct='')
    # сделать вывод средств (USDT) / withdrawal
    result = fundingAPI.coin_withdraw('usdt', '2', '3', '', '', '0')
    # получить историю депозитов / get deposit history
    result = fundingAPI.get_deposit_history()
    # получить историю выводов / get withdrawal history
    result = fundingAPI.get_withdrawal_history()
    # получить id валюты / get currencies
    result = fundingAPI.get_currency()
    # redemption/получить выплату/приобрести в OKEx PiggyBank / PiggyBank purchase
    result = fundingAPI.purchase_redempt('BTC', '1', 'purchase')

    # рыночный API / market api
    marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, flag)
    # получить ВСЕ тикеры валют на рынке (спот) / get tickers
    result = marketAPI.get_tickers('SPOT')
    # получить тикер пары (BTC-USDT) / get ticker
    result = marketAPI.get_ticker('BTC-USDT')
    # получить индексный тикер в паре (BTC-USDT) / get index tickers
    result = marketAPI.get_index_ticker('BTC', 'BTC-USD')
    # получить информацию по книге ордеров (BTC-USDT) / get order book
    result = marketAPI.get_orderbook('BTC-USDT-210402', '400')
    # получить информацию по свечам (BTC-USDT) / get candlesticks
    result = marketAPI.get_candlesticks('BTC-USDT-210924', bar='1m')
    # получить историю по свечам (недоступно в демо-режиме) / get candlesticks history（top currencies in real-trading only
    result = marketAPI.get_history_candlesticks('BTC-USDT')
    # получить информацию по свечам (индекс) / get index candlesticks
    result = marketAPI.get_index_candlesticks('BTC-USDT')
    # получить информацию по сделкам (BTC-USDT, 400) / get trades
    result = marketAPI.get_trades('BTC-USDT', '400')

    # публичный API / public api
    publicAPI = Public.PublicAPI(api_key, secret_key, passphrase, False, flag)
    # получить информацию по трейдинговому инструменту (фьючерс, BTC-USDT) / get instrument
    result = publicAPI.get_instruments('FUTURES', 'BTC-USDT')
    # получить историю по инструменту/паре (фьючерс, BTC-USDT) / get delivery/exercise history
    result = publicAPI.get_deliver_history('FUTURES', 'BTC-USD')
    # получить информацию по открытым позициям (своп) / get open interest
    result = publicAPI.get_open_interest('SWAP')
    # получить информацию по текущей ставке (BTC-USDT, своп) / get funding rate
    result = publicAPI.get_funding_rate('BTC-USD-SWAP')
    # получить информацию по истории ставки (BTC-USDT, своп) / get funding rate history
    result = publicAPI.funding_rate_history('BTC-USD-SWAP')
    # получить цену лимита (BTC-USDT) / get limit price
    result = publicAPI.get_price_limit('BTC-USD-210402')
    # получить рыночные данные по опционам (BTC-USD) / get option market data
    result = publicAPI.get_opt_summary('BTC-USD')
    # получить цену исполнения (ETH-USD) / get estimated delivery/excercise price
    result = publicAPI.get_estimated_price('ETH-USD-210326')
    # получить информацию по ставке и беспроцентной квоте / get discount rate & interest-free quota
    result = publicAPI.discount_interest_free_quota('')
    # системное время / get system time
    result = publicAPI.get_system_time()
    # получить информацию по ликвидационным ордерам (фьючерс, BTC-USDT) / get liquidation orders
    result = publicAPI.get_liquidation_orders('FUTURES', uly='BTC-USDT', alias='next_quarter', state='filled')
    # получить информацию по цене отметки инструмента (фьючерс) / get mark price
    result = publicAPI.get_mark_price('FUTURES')

    # торговый API / trade api
    tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase, False, flag)
    # поставить ордер / place order 
    result = tradeAPI.place_order(instId='BTC-USDT-210326', tdMode='cross', side='sell', posSide='short',
                                    ordType='market', sz='100')
    # поставить несколько ордеров / place multiple orders
    result = tradeAPI.place_multiple_orders([
          {'instId': 'BTC-USD-210402', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17400',
           'posSide': 'long',
           'clOrdId': 'a12344', 'tag': 'test1210'},
          {'instId': 'BTC-USD-210409', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17359',
           'posSide': 'long',
           'clOrdId': 'a12344444', 'tag': 'test1211'}
      ])

    # oтменить ордер / cancel order
    result = tradeAPI.cancel_order('BTC-USD-201225', '257164323454332928')
    # oтменить несколько ордеров / cancel multiple orders
    result = tradeAPI.cancel_multiple_orders([
          {"instId": "BTC-USD-210402", "ordId": "297389358169071616"},
          {"instId": "BTC-USD-210409", "ordId": "297389358169071617"}
      ])

    # изменить ордер / amend order
    result = tradeAPI.amend_order()
    # изменить несколько ордеров / amend multiple orders
    result = tradeAPI.amend_multiple_orders(
          [{'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616434384896', 'newPx': '17880'},
           {'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616652488704', 'newPx': '17882'}
           ])

    # закрыть позиции / close positions
    result = tradeAPI.close_positions('BTC-USDT-210409', 'isolated', 'long', '')
    # получить информацию по ордеру / get order details
    result = tradeAPI.get_orders('BTC-USD-201225', '257173039968825345')
    # получить список ордеров / get order list
    result = tradeAPI.get_order_list()
    # получить историю ордеров (последние 7 дней, фьючерс) / get order history (last 7 days)
    result = tradeAPI.get_orders_history('FUTURES')
    # получить историю ордеров (последние 3 месяца, фьючерс) / get order history (last 3 months)
    result = tradeAPI.orders_history_archive('FUTURES')
    # получить историю транзакций / get transaction details
    result = tradeAPI.get_fills()
    # пример постановки алгоритмического ордера / place algo order
    result = tradeAPI.place_algo_order('BTC-USDT-210409', 'isolated', 'buy', ordType='conditional',
                                         sz='100',posSide='long', tpTriggerPx='60000', tpOrdPx='59999')
    # отменить алгоритмический ордер / cancel algo order
    result = tradeAPI.cancel_algo_order([{'algoId': '297394002194735104', 'instId': 'BTC-USDT-210409'}])
    # получить список алгоритмических ордеров / get algo order List
    result = tradeAPI.order_algos_list('conditional', instType='FUTURES')
    # получить историю алгоритмических ордеров / get algo order history
    result = tradeAPI.order_algos_history('conditional', 'canceled', instType='FUTURES')

    # API субаккаунтoв / API subAccount
    subAccountAPI = SubAccount.SubAccountAPI(api_key, secret_key, passphrase, False, flag)
    # получить подробную информацию о балансе субаккаунта через основной аккаунт / query detailed balance info of trading account of a sub-account via the master account
    result = subAccountAPI.balances(subAcct='')
    # получить историю трансферов всех субаккаунтов (работает только с основного аккаунтa) / history of sub-account transfer(applies to master accounts only)
    result = subAccountAPI.bills()
    # удалить API ключ субаккаунта (работает только с основного аккаунтa) / delete the APIkey of sub-accounts (applies to master accounts only)
    result = subAccountAPI.delete(pwd='', subAcct='', apiKey='')
    # сбросить API ключ субаккаунта (работает только с основного аккаунтa) / reset the APIkey of a sub-account(applies to master accounts only)
    result = subAccountAPI.reset(pwd='', subAcct='', label='', apiKey='', perm='')
    # создать API ключ субаккаунта (работает только с основного аккаунтa) / create an APIkey for a sub-account(applies to master accounts only)
    result = subAccountAPI.create(pwd='123456', subAcct='', label='', Passphrase='')
    # получить список субаккаунтов (работает только с основного аккаунтa) / view sub-account list(applies to master accounts only)
    result = subAccountAPI.view_list()
    # управление трансферами между субаккаунтами (работает только с основного аккаунтa) / manage the transfers between sub-accounts(applies to master accounts only)
    result = subAccountAPI.control_transfer(ccy='', amt='', froms='', to='', fromSubAccount='', toSubAccount='')

    # статус системы / system status
    Status = Status.StatusAPI(api_key, secret_key, passphrase, False, flag)
    result = Status.status()

    #вывести/исполнить любую из упомянутых команд / print/execute any of the above queries
    print(json.dumps(result))
