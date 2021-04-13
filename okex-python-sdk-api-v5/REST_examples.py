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

    # account api/аутентификация и общие запросы по аккаунту
    accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)
    # get balance/получить баланс аккаунтa в BTC
    result = accountAPI.get_account('BTC')
    # get positions/получить позиции аккаунтa (BTC-USD, фьючерс)
    result = accountAPI.get_positions('FUTURES', 'BTC-USD-210402')
    # get account configuration/конфигурация аккаунта
    result = accountAPI.get_account_config()
    # get position mode/получить режим исполнения позиции
    result = accountAPI.get_position_mode('long_short_mode')
    # set leverage/установка маржи кредитного плеча 
    result = accountAPI.set_leverage(instId='BTC-USD-210402', lever='10', mgnMode='cross')
    # get maximum tradable size for instrument/получить максимально возможный размер для выбранного инструмента (фьючерс)  
    result = accountAPI.get_maximum_trade_size('BTC-USDT-210402', 'cross', 'USDT')
    # get maximum available tradable amount/получить максимально возможную сумму для сделки (фьючерс)
    result = accountAPI.get_max_avail_size('BTC-USDT-210402', 'isolated', 'BTC')
    # increase/decrease margin/yвеличение/сокращение маржи
    result = accountAPI.Adjustment_margin('BTC-USDT-210409', 'long', 'add', '100')
    # get leverage/получить маржу  
    result = accountAPI.get_leverage('BTC-USDT-210409', 'isolated')
    # get the maximum loan of isolated MARGIN/получить максимальную ссуду изолированной маржи
    result = accountAPI.get_max_load('BTC-USDT', 'cross', 'BTC')
    # get fee rates/получить размер комиссий (фьючерс)
    result = accountAPI.get_fee_rates('FUTURES', '', category='1')
    # get interest-accrued/получить начисленные проценты (BTC-USDT)
    result = accountAPI.get_interest_accrued('BTC-USDT', 'BTC', 'isolated', '', '', '10')
    # get maximum withdrawals/установить максимальный размер выводoв
    result = accountAPI.get_max_withdrawal('')

    # funding api/основной аккаунт
    fundingAPI = Funding.FundingAPI(api_key, secret_key, passphrase, False, flag)
    # get deposit address/получить адрес для депозита
    result = fundingAPI.get_deposit_address('')
    # get balance/ получить баланс основного аккаунтa (в BTC)
    result = fundingAPI.get_balances('BTC')
    # funds transfer/сделать трансфер средств на субаккаунт
    result = fundingAPI.funds_transfer(ccy='', amt='', type='1', froms="", to="",subAcct='')
    # withdrawal/сделать вывод средств (USDT)
    result = fundingAPI.coin_withdraw('usdt', '2', '3', '', '', '0')
    # get deposit history/получить историю депозитов
    result = fundingAPI.get_deposit_history()
    # get withdrawal history/получить историю выводов
    result = fundingAPI.get_withdrawal_history()
    # get currencies/получить id валюты
    result = fundingAPI.get_currency()
    # PiggyBank purchase/redemption/получить выплату/приобрести в OKEx PiggyBank
    result = fundingAPI.purchase_redempt('BTC', '1', 'purchase')

    # market api/рыночный API
    marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, flag)
    # get tickers/получить ВСЕ тикеры валют на рынке (спот)
    result = marketAPI.get_tickers('SPOT')
    # get ticker/получить тикер пары (BTC-USDT)
    result = marketAPI.get_ticker('BTC-USDT')
    # get index tickers/получить индексный тикер в паре (BTC-USDT)
    result = marketAPI.get_index_ticker('BTC', 'BTC-USD')
    # get order book/получить информацию по книге ордеров (BTC-USDT)
    result = marketAPI.get_orderbook('BTC-USDT-210402', '400')
    # get candlesticks/получить информацию по свечам (BTC-USDT)
    result = marketAPI.get_candlesticks('BTC-USDT-210924', bar='1m')
    # get candlesticks history（top currencies in real-trading only/получить историю по свечам (недоступно в демо-режиме)
    result = marketAPI.get_history_candlesticks('BTC-USDT')
    # get index candlesticks/получить информацию по свечам (индекс)
    result = marketAPI.get_index_candlesticks('BTC-USDT')
    # get trades/получить информацию по сделкам (BTC-USDT, 400)
    result = marketAPI.get_trades('BTC-USDT', '400')

    # public api/публичный API
    publicAPI = Public.PublicAPI(api_key, secret_key, passphrase, False, flag)
    # get instrument/получить информацию по трейдинговому инструменту (фьючерс, BTC-USDT)
    result = publicAPI.get_instruments('FUTURES', 'BTC-USDT')
    # get delivery/exercise history/получить историю по инструменту/паре (фьючерс, BTC-USDT)
    result = publicAPI.get_deliver_history('FUTURES', 'BTC-USD')
    # get open interest/получить информацию по открытым позициям (своп)
    result = publicAPI.get_open_interest('SWAP')
    # get funding rate/получить информацию по текущей ставке (BTC-USDT, своп)
    result = publicAPI.get_funding_rate('BTC-USD-SWAP')
    # get funding rate history/получить информацию по истории ставки (BTC-USDT, своп)
    result = publicAPI.funding_rate_history('BTC-USD-SWAP')
    # get limit price/получить цену лимита (BTC-USDT)
    result = publicAPI.get_price_limit('BTC-USD-210402')
    # get option market data/получить рыночные данные по опционам (BTC-USD)
    result = publicAPI.get_opt_summary('BTC-USD')
    # get estimated delivery/excercise price/получить цену исполнения (ETH-USD)
    result = publicAPI.get_estimated_price('ETH-USD-210326')
    # get discount rate & interest-free quota/получить информацию по ставке и беспроцентной квоте
    result = publicAPI.discount_interest_free_quota('')
    # get system time/системное время
    result = publicAPI.get_system_time()
    # get liquidation orders/получить информацию по ликвидационным ордерам (фьючерс, BTC-USDT)
    result = publicAPI.get_liquidation_orders('FUTURES', uly='BTC-USDT', alias='next_quarter', state='filled')
    # get mark price/получить информацию по цене отметки инструмента (фьючерс)
    result = publicAPI.get_mark_price('FUTURES')

    # trade api/торговый API
    tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase, False, flag)
    # place order/поставить ордер 
    result = tradeAPI.place_order(instId='BTC-USDT-210326', tdMode='cross', side='sell', posSide='short',
                                    ordType='market', sz='100')
    # place multiple orders/поставить несколько ордеров
    result = tradeAPI.place_multiple_orders([
          {'instId': 'BTC-USD-210402', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17400',
           'posSide': 'long',
           'clOrdId': 'a12344', 'tag': 'test1210'},
          {'instId': 'BTC-USD-210409', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17359',
           'posSide': 'long',
           'clOrdId': 'a12344444', 'tag': 'test1211'}
      ])

    # cancel order/oтменить ордер
    result = tradeAPI.cancel_order('BTC-USD-201225', '257164323454332928')
    # cancel multiple orders/oтменить несколько ордеров
    result = tradeAPI.cancel_multiple_orders([
          {"instId": "BTC-USD-210402", "ordId": "297389358169071616"},
          {"instId": "BTC-USD-210409", "ordId": "297389358169071617"}
      ])

    # amend order/изменить ордер
    result = tradeAPI.amend_order()
    # amend multiple orders/изменить несколько ордеров
    result = tradeAPI.amend_multiple_orders(
          [{'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616434384896', 'newPx': '17880'},
           {'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616652488704', 'newPx': '17882'}
           ])

    # close positions/закрыть позиции
    result = tradeAPI.close_positions('BTC-USDT-210409', 'isolated', 'long', '')
    # get order details/получить информацию по ордеру
    result = tradeAPI.get_orders('BTC-USD-201225', '257173039968825345')
    # get order list/получить список ордеров
    result = tradeAPI.get_order_list()
    # get order history (last 7 days)/получить историю ордеров (последние 7 дней, фьючерс)
    result = tradeAPI.get_orders_history('FUTURES')
    # get order history (last 3 months)/получить историю ордеров (последние 3 месяца, фьючерс)
    result = tradeAPI.orders_history_archive('FUTURES')
    # get transaction details/получить историю транзакций
    result = tradeAPI.get_fills()
    # place algo order/пример постановки алгоритмического ордера
    result = tradeAPI.place_algo_order('BTC-USDT-210409', 'isolated', 'buy', ordType='conditional',
                                         sz='100',posSide='long', tpTriggerPx='60000', tpOrdPx='59999')
    # cancel algo order/отменить алгоритмический ордер
    result = tradeAPI.cancel_algo_order([{'algoId': '297394002194735104', 'instId': 'BTC-USDT-210409'}])
    # get algo order List/получить список алгоритмических ордеров
    result = tradeAPI.order_algos_list('conditional', instType='FUTURES')
    # get algo order History/получить историю алгоритмических ордеров
    result = tradeAPI.order_algos_history('conditional', 'canceled', instType='FUTURES')

    # API subAccount/API субаккаунтoв
    subAccountAPI = SubAccount.SubAccountAPI(api_key, secret_key, passphrase, False, flag)
    # query detailed balance info of trading account of a sub-account via the master account/получить подробную информацию о балансе субаккаунта через основной аккаунт
    result = subAccountAPI.balances(subAcct='')
    # history of sub-account transfer(applies to master accounts only)/получить историю трансферов всех субаккаунтов (работает только с основного аккаунтa)
    result = subAccountAPI.bills()
    # delete the APIkey of sub-accounts (applies to master accounts only)/удалить API ключ субаккаунта (работает только с основного аккаунтa)
    result = subAccountAPI.delete(pwd='', subAcct='', apiKey='')
    # reset the APIkey of a sub-account(applies to master accounts only)/сбросить API ключ субаккаунта (работает только с основного аккаунтa)
    result = subAccountAPI.reset(pwd='', subAcct='', label='', apiKey='', perm='')
    # create an APIkey for a sub-account(applies to master accounts only)/создать API ключ субаккаунта (работает только с основного аккаунтa)
    result = subAccountAPI.create(pwd='123456', subAcct='', label='', Passphrase='')
    # view sub-account list(applies to master accounts only)/получить список субаккаунтов (работает только с основного аккаунтa)
    result = subAccountAPI.view_list()
    # manage the transfers between sub-accounts(applies to master accounts only)/управление трансферами между субаккаунтами (работает только с основного аккаунтa)
    result = subAccountAPI.control_transfer(ccy='', amt='', froms='', to='', fromSubAccount='', toSubAccount='')

    # system status/статус системы
    Status = Status.StatusAPI(api_key, secret_key, passphrase, False, flag)
    result = Status.status()

    #print/execute any of the above queries/вывести/исполнить любую из упомянутых команд
    print(json.dumps(result))
