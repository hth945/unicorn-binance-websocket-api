#%%

from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
import os
import time
import threading
import logging

from example_process_streams import BinanceWebSocketApiProcessStreams

logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")



# binance_websocket_api_manager = BinanceWebSocketApiManager(BinanceWebSocketApiProcessStreams.process_stream_data)
# binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com-margin-testnet")

binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.us")

def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            #pass
            print(oldest_stream_data_from_stream_buffer)


worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
worker_thread.start()
print('1')
ticker_arr_stream_id = binance_websocket_api_manager.create_stream("ticker","btcusdt")
time.sleep(7)
print('2')
binance_websocket_api_manager.stop_stream(ticker_arr_stream_id)
time.sleep(2)
print('3')
# %%
