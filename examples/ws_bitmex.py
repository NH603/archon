from archon.ws.bitmex.bitmex_ws import BitMEXWebsocket
import logging
from logging.handlers import RotatingFileHandler
from time import sleep
import datetime
import json
import toml
from loguru import logger

crypto = "XBTUSD"


def toml_file(fs):
    with open(fs, "r") as f:
        return f.read()

def parse_toml(filename):
    toml_string = toml_file(filename)
    parsed_toml = toml.loads(toml_string)
    return parsed_toml

def run(k,s):
    
    logger.info("run")

    bitmexws = BitMEXWebsocket(symbol=crypto, api_key=k, api_secret=s)

    #logger.info("Instrument data: %s" % ws.get_instrument())
    logger.info("\n\n\n\n************\n\n\n")
    while(bitmexws.ws.sock.connected):        
        #logger.info("Ticker: %s" % bitmexws.get_ticker())
        #logger.info("Open orders: %s" % bitmexws.open_orders(''))
        #t = bitmexws.recent_trades()
        #logger.info("recent trades: %i" % len(t))

        d = bitmexws.market_depth()
        logger.info("depth %i " % len(d))
        print (d)

        """
        sells = list(filter(lambda d: d['side'] == 'Sell' , d))        
        buys = list(filter(lambda d: d['side'] == 'Buy' , d))        

        #sells = list(filter(lambda d: d['side'] == 'Sell' , d))        
        #logger.info(sells[0])
        topbuys = buys[:5]
        topsells = sells[-5:]
        #logger.info(buys[-1])
        logger.info("depth sells %i " % len(sells))
        logger.info("depth  buys %i " % len(buys))

        for i in range(5):
            bp,bq = topbuys[i]['price'],topbuys[i]['size']
            sp,sq = topsells[i]['price'],topsells[i]['size']
            logger.info("%5.3f   %5.2f"%(bp,sp))

        """
        sleep(5.0)

if __name__ == "__main__":
    
    filename = "apikeys.toml"
    apikeys = parse_toml(filename)['BITMEX']
    k,s = apikeys['public_key'],apikeys['secret']
    run(k,s)

