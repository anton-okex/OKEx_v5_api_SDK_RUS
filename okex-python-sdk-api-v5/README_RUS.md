## Требования

`Python версия：3.6+`

`WebSocketAPI： рекомендованная версия websockets package - 6.0`

#### Шаг 1: Скачивание SDK и установка необходимых библиотек

1.1 Скачивание этого SDK (python)

- Используйте `Clone` или `Download` для того что-бы скачать `okex-python-sdk-api-v5` SDK  

1.2 Установка необходимых библиотек

```python
pip install requests
pip install websockets==6.0
```

#### Шаг 2: Заполнение личной информации для API

2.1 Если у вас нет API ключа и других данных, то их можно получить [в вашем аккаунте на ОКЕх](https://www.okex.com/account/users/myApi) 

2.2 Заполните всю необходимую информацию для аутентификации в`REST_examples.py（RestAPI）` и `websocket_examples.py（WebSocketAPI）`

```python 
api_key = "ваш_API_ключ"
secret_key = "ваш_секретный_ключ"
passphrase = "ваша_секретная_фраза"
```

#### Шаг 3: Соединение с API

- RestAPI
  - Запустите `REST_examples.py`
  - Используйте нужные вам команды

- WebSocketAPI
  - Запустите `websocket_examples.py`
  - В зависимости от `public channel`/`private channel`/`trade`, выберете соответствующий `url`, а также нужные вам команды

```python 
# WebSocket public channel
url = "wss://ws.okex.com:8443/ws/v5/public?brokerId=9999"

# WebSocket private channel
url = "wss://ws.okex.com:8443/ws/v5/private?brokerId=9999"
```

```Python
# Для public channel аутентификация не требуется  （Instrument, Tickers, Index, Mark price, Order Book, Funding rate, и т.д.）
loop.run_until_complete(subscribe_without_login(url, channels))

# Для private channel аутентификация необходимa（Account,Positions, Order, и т.д.）
loop.run_until_complete(subscribe(url, api_key, passphrase, seceret_key, channels))

# Трейдинг（Place Order, Cancel Order, Amend Order, и т.д.）
loop.run_until_complete(trade(url, api_key, passphrase, seceret_key, trade_param))
```

- Для дополнительной информации по API V5 используйте [официальную документацию ОКЕх](https://www.okex.com/docs-v5/en/)

- Пользователи RestAPI могут использовать параметр `flag` в `example.py` для того, что-бы выбирать режимы трейдинга (демо или реальный)

- Пользователи WebSocketAPI могут использовать `url` для того, что-бы выбирать режимы трейдинга (демо или реальный)

- Дополнительная информация для `WebSocketAPI` содержится на следующих ресурсах:

  - `asyncio`、`websockets` document/`github`：

    ```python 
    https://docs.python.org/3/library/asyncio-dev.html
    https://websockets.readthedocs.io/en/stable/intro.html
    https://github.com/aaugustin/websockets
    ```

  - Информация по `code=1006`：

    ```python 
    https://github.com/Rapptz/discord.py/issues/1996
    https://github.com/aaugustin/websockets/issues/587
    ```
