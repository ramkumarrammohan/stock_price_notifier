from xmlrpc.client import Boolean
import requests, json

class LiveTicker:
    def __init__(self) -> None:
        self.symbols = []
        self.results = []
        self.response = None
        self.price_map = []

    def add_symbol(self, symbol):
        self.symbols.append(symbol)

    def get_current_price(self):
        self._reset()
        self._get_quote_info()
        if not self._is_valid_response():
            return True, None
        self._parse_response()
        return False, self.price_map

    def _reset(self):
        self.results = []
        self.response = None
        self.price_map = []

    def _is_valid_response(self) -> Boolean:
        print('_is_valid_response called')
        if self.response == None or self.response.status_code != requests.codes.ok:
            return False
        if self.response.json().get('error') != None:
            return False
        self.results = self.response.json().get('quoteResponse').get('result')
        return (len(self.results) == len(self.symbols))

    def _parse_response(self):
        print('_parse_response called')
        for obj in self.results:
            map = {}
            map['symbol'] = obj.get('symbol')
            map['price'] = obj.get('regularMarketPrice')
            self.price_map.append(map)

    def _get_quote_info(self):
        user_agent_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        symbols = ",".join(self.symbols)
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols={}".format(symbols)
        print(url)
        self.response = requests.get(url=url, headers=user_agent_headers)