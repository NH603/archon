import archon.facade as facade
import archon.broker as broker
import archon.exchange.exchanges as exc
import archon.exchange.binance as b
import archon.model.models as models
from archon.util import *

import time
import datetime
import math

from datetime import datetime

a = broker.Broker()
a.set_keys_exchange_file()
client = a.afacade.get_client(exc.BINANCE)
market = models.get_market("RVN","BTC",exc.BINANCE)
x = client.get_orderbook_symbol(market)
time.sleep(0.5)
m = models.market_from("RVN","BTC")
[bids,asks] = a.afacade.get_orderbook(m,exc.BINANCE)
print (bids[0],asks[0])