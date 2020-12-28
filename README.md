# Dydx historical funding rate analysis #

Dydx (https://dydx.exchange/) offers the following perpetual contracts:
1. BTC-USD
2. ETH-USD
3. LINK-USD

One key element of the perpetual contract is the funding rate. The funding rate is used as an incentive to keep the price of the derivative aligned with that of the underlying.

I have studied the funding rates, since inception, of the following contracts:
1. BTC-USD: launched in April 2020
2. ETH-USD: launched in July 2020

I have not studied the funding rates of LINK-USD, which has been launched in August 2020.

For direct access to and download of the data, you can run the script. Based on your market selection (BTC-USD, ETH-USD, etc.), the script will create a csv file (data.csv) with all the relevant data since inception.  

The method used is: GET https://api.dydx.exchange/v1/historical-funding-rates

Doc: https://docs.dydx.exchange/#get-historical-funding-rates

Takeaways of the analysis:

* BTC-USD
  * Although positive (longs pay shorts), the annualised funding rate is almost null: 0.0072%

![Alt text](https://raw.githubusercontent.com/TiGowa/dydx-funding-rate/master/btc-usd-funding-per-hour.png?raw=true "Optional Title")

![Alt text](https://raw.githubusercontent.com/TiGowa/dydx-funding-rate/master/btc-usd-funding-annualised.png?raw=true "Optional Title")

* ETH-USD
  * Although better than the BTC-USD funding rate, the annualised funding rate is near zero: 0.01194% 
  
![Alt text](https://raw.githubusercontent.com/TiGowa/dydx-funding-rate/master/eth-usd-funding-per-hour.png?raw=true "Optional Title")

![Alt text](https://raw.githubusercontent.com/TiGowa/dydx-funding-rate/master/eth-usd-funding-annualised.png?raw=true "Optional Title")

