# Примеры команд для OKEx V5 API (websockets)
# Code examples for the OKEx V5 API (websockets)

import asyncio
import websockets
import json
import requests
import hmac
import base64
import zlib
import datetime
import time

# форматирование timestamp / format the timestamp
def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

# время серверa / server time
def get_server_time():
    url = "https://www.okex.com/api/v5/public/time"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data'][0]['ts']
    else:
        return ""
    
def get_local_timestamp():
    return int(time.time())

# аутентификация / login
def login_params(timestamp, api_key, passphrase, secret_key):
    message = timestamp + 'GET' + '/users/self/verify'

    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    sign = base64.b64encode(d)

    login_param = {"op": "login", "args": [{"apiKey": api_key,
                                            "passphrase": passphrase,
                                            "timestamp": timestamp,
                                            "sign": sign.decode("utf-8")}]}
    login_str = json.dumps(login_param)
    return login_str

# данные по bids & asks / bids & asks data
def partial(res):
    data_obj = res['data'][0]
    bids = data_obj['bids']
    asks = data_obj['asks']
    instrument_id = res['arg']['instId']
    return bids, asks, instrument_id

# изменение bids / modify & update bids
def update_bids(res, bids_p):
    bids_u = res['data'][0]['bids']
    for i in bids_u:
        bid_price = i[0]
        for j in bids_p:
            if bid_price == j[0]:
                if i[1] == '0':
                    bids_p.remove(j)
                    break
                else:
                    del j[1]
                    j.insert(1, i[1])
                    break
        else:
            if i[1] != "0":
                bids_p.append(i)
    else:
        bids_p.sort(key=lambda price: sort_num(price[0]), reverse=True)
        # print('合并后的bids为：' + str(bids_p) + '，档数为：' + str(len(bids_p)))
    return bids_p

# изменение asks / modify & update asks
def update_asks(res, asks_p):
    # 获取增量asks数据
    asks_u = res['data'][0]['asks']
    for i in asks_u:
        ask_price = i[0]
        for j in asks_p:
            if ask_price == j[0]:
                if i[1] == '0':
                    asks_p.remove(j)
                    break
                else:
                    del j[1]
                    j.insert(1, i[1])
                    break
        else:
            if i[1] != "0":
                asks_p.append(i)
    else:
        asks_p.sort(key=lambda price: sort_num(price[0]))
    return asks_p


def sort_num(n):
    if n.isdigit():
        return int(n)
    else:
        return float(n)

# получить список bids & asks / get the bids & asks file
def check(bids, asks):
    bids_l = []
    bid_l = []
    count_bid = 1
    while count_bid <= 25:
        if count_bid > len(bids):
            break
        bids_l.append(bids[count_bid-1])
        count_bid += 1
    for j in bids_l:
        str_bid = ':'.join(j[0 : 2])
        bid_l.append(str_bid)
    asks_l = []
    ask_l = []
    count_ask = 1
    while count_ask <= 25:
        if count_ask > len(asks):
            break
        asks_l.append(asks[count_ask-1])
        count_ask += 1
    for k in asks_l:
        str_ask = ':'.join(k[0 : 2])
        ask_l.append(str_ask)
    num = ''
    if len(bid_l) == len(ask_l):
        for m in range(len(bid_l)):
            num += bid_l[m] + ':' + ask_l[m] + ':'
    elif len(bid_l) > len(ask_l):
        for n in range(len(ask_l)):
            num += bid_l[n] + ':' + ask_l[n] + ':'
        for l in range(len(ask_l), len(bid_l)):
            num += bid_l[l] + ':'
    elif len(bid_l) < len(ask_l):
        for n in range(len(bid_l)):
            num += bid_l[n] + ':' + ask_l[n] + ':'
        for l in range(len(bid_l), len(ask_l)):
            num += ask_l[l] + ':'

    new_num = num[:-1]
    int_checksum = zlib.crc32(new_num.encode())
    fina = change(int_checksum)
    return fina


def change(num_old):
    num = pow(2, 31) - 1
    if num_old > num:
        out = num_old - num * 2 - 2
    else:
        out = num_old
    return out


# подписаться на каналы без аутентификации / subscribe channels without login
async def subscribe_without_login(url, channels):
    l = []
    while True:
        try:
            async with websockets.connect(url) as ws:
                sub_param = {"op": "subscribe", "args": channels}
                sub_str = json.dumps(sub_param)
                await ws.send(sub_str)
                print(f"send: {sub_str}")

                while True:
                    try:
                        res = await asyncio.wait_for(ws.recv(), timeout=25)
                    except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed) as e:
                        try:
                            await ws.send('ping')
                            res = await ws.recv()
                            print(res)
                            continue
                        except Exception as e:
                            print("Соединение закрыто, переподключение")
                            break

                    print(get_timestamp() + res)
                    res = eval(res)
                    if 'event' in res:
                        continue
                    for i in res['arg']:
                        if 'books' in res['arg'][i] and 'books5' not in res['arg'][i]:
                            if res['action'] == 'snapshot':
                                for m in l:
                                    if res['arg']['instId'] == m['instrument_id']:
                                        l.remove(m)
                                bids_p, asks_p, instrument_id = partial(res)
                                d = {}
                                d['instrument_id'] = instrument_id
                                d['bids_p'] = bids_p
                                d['asks_p'] = asks_p
                                l.append(d)

                                # контрольные суммы / checksum
                                checksum = res['data'][0]['checksum']
                                check_num = check(bids_p, asks_p)
                                if check_num == checksum:
                                    print("Проверка_checksum：True")
                                else:
                                    print("Проверка_checksum：False，повторная_попытка...")

                                    # отменить подписку / cancel subscription
                                    await unsubscribe_without_login(url, channels)
                                    async with websockets.connect(url) as ws:
                                        sub_param = {"op": "subscribe", "args": channels}
                                        sub_str = json.dumps(sub_param)
                                        await ws.send(sub_str)
                                        print(f"send: {sub_str}")

                            elif res['action'] == 'update':
                                for j in l:
                                    if res['arg']['instId'] == j['instrument_id']:
                                        # получить полные данные / full data
                                        bids_p = j['bids_p']
                                        asks_p = j['asks_p']
                                        bids_p = update_bids(res, bids_p)
                                        asks_p = update_asks(res, asks_p)

                                        # контрольные суммы / checksum
                                        checksum = res['data'][0]['checksum']
                                        # print('checksum/контрольные суммы：' + str(checksum))
                                        check_num = check(bids_p, asks_p)
                                        # print('checksum/контрольные суммы после проверки：' + str(check_num))
                                        if check_num == checksum:
                                            print("Проверка_checksum：True")
                                        else:
                                            print("Проверка_checksum：False，повторная_попыткa...")

                                            # отменить подписку / cancel subscription
                                            await unsubscribe_without_login(url, channels)
                                            async with websockets.connect(url) as ws:
                                                sub_param = {"op": "subscribe", "args": channels}
                                                sub_str = json.dumps(sub_param)
                                                await ws.send(sub_str)
                                                print(f"send: {sub_str}")
        except Exception as e:
            print("соединение прервано，повторное подключение...")
            continue


# подписаться на каналы с аутентификацией / subscribe channels with login
async def subscribe(url, api_key, passphrase, secret_key, channels):
    while True:
        try:
            async with websockets.connect(url) as ws:
                # аутентификация / login
                timestamp = str(get_local_timestamp())
                login_str = login_params(timestamp, api_key, passphrase, secret_key)
                await ws.send(login_str)
                # print(f"send: {login_str}")
                res = await ws.recv()
                print(res)

                # подписаться / subscribe
                sub_param = {"op": "subscribe", "args": channels}
                sub_str = json.dumps(sub_param)
                await ws.send(sub_str)
                print(f"send: {sub_str}")

                while True:
                    try:
                        res = await asyncio.wait_for(ws.recv(), timeout=25)
                    except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed) as e:
                        try:
                            await ws.send('ping')
                            res = await ws.recv()
                            print(res)
                            continue
                        except Exception as e:
                            print("соединение закрыто，повторное подключение...")
                            break

                    print(get_timestamp() + res)

        except Exception as e:
            print("соединение прервано，повторное подключение...")
            continue


# торговый API / trade
async def trade(url, api_key, passphrase, secret_key, trade_param):
    while True:
        try:
            async with websockets.connect(url) as ws:
                # login
                timestamp = str(get_local_timestamp())
                login_str = login_params(timestamp, api_key, passphrase, secret_key)
                await ws.send(login_str)
                # print(f"send: {login_str}")
                res = await ws.recv()
                print(res)

                
                sub_str = json.dumps(trade_param)
                await ws.send(sub_str)
                print(f"send: {sub_str}")

                while True:
                    try:
                        res = await asyncio.wait_for(ws.recv(), timeout=25)
                    except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed) as e:
                        try:
                            await ws.send('ping')
                            res = await ws.recv()
                            print(res)
                            continue
                        except Exception as e:
                            print("соединение закрыто，повторное подключение...")
                            break

                    print(get_timestamp() + res)

        except Exception as e:
            print("соединение прервано，повторное подключение...")
            continue


# отменить подписку / unsubscribe channels
async def unsubscribe(url, api_key, passphrase, secret_key, channels):
    async with websockets.connect(url) as ws:
        # аутентификация / login
        timestamp = str(get_local_timestamp())
        login_str = login_params(timestamp, api_key, passphrase, secret_key)
        await ws.send(login_str)
        # print(f"send: {login_str}")

        res = await ws.recv()
        print(f"recv: {res}")

        # отменить подписку / unsubscribe
        sub_param = {"op": "unsubscribe", "args": channels}
        sub_str = json.dumps(sub_param)
        await ws.send(sub_str)
        print(f"send: {sub_str}")

        res = await ws.recv()
        print(f"recv: {res}")


# отменить подписку / unsubscribe channels
async def unsubscribe_without_login(url, channels):
    async with websockets.connect(url) as ws:
        sub_param = {"op": "unsubscribe", "args": channels}
        sub_str = json.dumps(sub_param)
        await ws.send(sub_str)
        print(f"send: {sub_str}")

        res = await ws.recv()
        print(f"recv: {res}")


api_key = "your_API_key/ваш_API_ключ"
secret_key = "your_secret_key/ваш_секретный_ключ"
passphrase = "your_passphrase/ваша_секретная_фраза"


# публичный WebSocket / WebSocket public
url = "wss://ws.okex.com:8443/ws/v5/public?brokerId=9999"

# приватный WebSocket / WebSocket private
url = "wss://ws.okex.com:8443/ws/v5/private?brokerId=9999"

'''
public channel parametres/параметры публичного канала
:param channel: channel name/название канала
:param instType: instrument type/тип инструмента
:param instId: instrument id/id инструмента
:param uly: base contract index/базовый индекс контракта

'''

# получить информацию по инструменту (фьючерс) / instrument
channels = [{"channel": "instruments", "instType": "FUTURES"}]
# получить информацию по тикеру / tickers
channels = [{"channel": "tickers", "instId": "BTC-USD-210326"}]
# получить информацию по открытым позициям / open-interest
channels = [{"channel": "open-interest", "instId": "BTC-USD-210326"}]
# получить информацию по свечам / candlesticks
channels = [{"channel": "candle1m", "instId": "BTC-USD-210326"}]
# получить информацию по сделкам / trades
channels = [{"channel": "trades", "instId": "BTC-USD-201225"}]
# получить цену исполнения / estimated price
channels = [{"channel": "estimated-price", "instType": "FUTURES", "uly": "BTC-USD"}]
# получить информацию по цене отметки инструмента / mark price
channels = [{"channel": "mark-price", "instId": "BTC-USDT-210326"}]
# получить цену лимита / price limit
channels = [{"channel": "price-limit", "instId": "BTC-USD-201225"}]
# получить рыночные данные по опционам / options data
channels = [{"channel": "opt-summary", "uly": "BTC-USD"}]
# получить информацию по текущей ставке / funding rate
channels = [{"channel": "funding-rate", "instId": "BTC-USD-SWAP"}]
# получить информацию по свечам (индекс) / index candlesticks
channels = [{"channel": "index-candle1m", "instId": "BTC-USDT"}]
# получить индексный тикер в паре (BTC-USDT) / index tickers
channels = [{"channel": "index-tickers", "instId": "BTC-USDT"}]

'''
private channel parametres/параметры приватного канала
:param channel: channel name/название канала
:param ccy: currency/валюта
:param instType: instrument type/тип инструмента
:param uly: base contract index/базовый индекс контракта
:param instId: instrument id/id инструмента

'''

# получить баланс счета в BTC / balance
channels = [{"channel": "account", "ccy": "BTC"}]
# получить позиции счета (BTC-USD, фьючерс) / positions
channels = [{"channel": "positions", "instType": "FUTURES", "uly": "BTC-USDT", "instId": "BTC-USDT-210326"}]
# получить ордерa (BTC-USD, фьючерс) / orders
channels = [{"channel": "orders", "instType": "FUTURES", "uly": "BTC-USD", "instId": "BTC-USD-201225"}]
# получить алгоритмическиe ордерa / algo orders
channels = [{"channel": "orders-algo", "instType": "FUTURES", "uly": "BTC-USD", "instId": "BTC-USD-201225"}]


# поставить ордер / place order
trade_param = {"id": "1512", "op": "order", "args": [{"side": "buy", "instId": "BTC-USDT", "tdMode": "isolated", "ordType": "limit", "px": "19777", "sz": "1"}]}
# поставить несколько ордеров / place multiple orders
trade_param = {"id": "1512", "op": "batch-orders", "args": [
          {"side": "buy", "instId": "BTC-USDT", "tdMode": "isolated", "ordType": "limit", "px": "19666", "sz": "1"},
          {"side": "buy", "instId": "BTC-USDT", "tdMode": "isolated", "ordType": "limit", "px": "19633", "sz": "1"}
      ]}
# oтменить ордер / cancel order
trade_param = {"id": "1512", "op": "cancel-order", "args": [{"instId": "BTC-USDT", "ordId": "259424589042823169"}]}
# oтменить несколько ордеров / cancel multiple orders
trade_param = {"id": "1512", "op": "batch-cancel-orders", "args": [
          {"instId": "BTC-USDT", "ordId": "259432098826694656"},
          {"instId": "BTC-USDT", "ordId": "259432098826694658"}
      ]}
# изменить ордер / amend order
trade_param = {"id": "1512", "op": "amend-order", "args": [{"instId": "BTC-USDT", "ordId": "259432767558135808", "newSz": "2"}]}
# изменить несколько ордеров / amend multiple orders
trade_param = {"id": "1512", "op": "batch-amend-orders", "args": [
          {"instId": "BTC-USDT", "ordId": "259435442492289024", "newSz": "2"},
          {"instId": "BTC-USDT", "ordId": "259435442496483328", "newSz": "3"}
      ]}


loop = asyncio.get_event_loop()

# для публичных каналов - аутентификация не нужнa
loop.run_until_complete(subscribe_without_login(url, channels))

# для приватных каналов - необходима
loop.run_until_complete(subscribe(url, api_key, passphrase, secret_key, channels))

# торговля
# loop.run_until_complete(trade(url, api_key, passphrase, secret_key, trade_param))

loop.close()
