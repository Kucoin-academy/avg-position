# Avg_position_strategy

## Strategy description

The strategy based on the spot average position is essentially a simplified version of the grid strategy. Keep fixing the ratio of the position of an investment target held to the total position. When the value of this investment target exceed an established threshold, sell part of the target to keep the ratio. When the value of this investment target become under than the established threshold, buy back part of the target to keep the ratio. Through continuous adjustment, the tartget ratio has been maintained at a fixed value to keep dynamic balancing.  



**e.g.**: If the BTC market price is 10000 USDT, while the balance is 1 BTC and 10000 USDT.  

Scenario 1: If the value of BTC is greater than the balance 10000 USDT and exceeds the threshold, like the price rising to 12000 USDT, sell 0.0833 BTC = (12000 - 10000)/2/12000, then the price drop down back to 10000 USDT, we buy back the same amount of BTC.  

Scenario 2: If the value of BTC is less than the balance 10000 USDT and under than the threshold, like the price dropping down to 8000 USDT, buy 0.125 BTC = (10000 - 8000)/2/8000, then the price rises back to 10000 USDT, we sell the same amount of BTC.  

**Summary: In this case, keep well the ratio between the target and the total position, that is, to maintain the value ratio of the base and the remaining funds in the account to 1: 1, so it is called the average position strategy**.  



**Advantages: The strategy of averaging positions is essentially a grid strategy, and its income comes from the fluctuation of prices within a certain range, so it will perform better in a shock market.**  

**Disadvantages: The risk is that the price continues to rise or fall unilaterally after the adjustment of positions.**  

In addition,   

In general:  Trigger price range is set at about 4 times of the trading fee as the benchmark to start the adjustment is more reasonable.  

Liquid market: It could be 1.5-2 times of the trading fee.  

Illiquid market: It could be 8, 10, even 20 or 50 times of the trading fee.  

**Controlling the minimum amounts of trades can also reduce the frequency of trades and increase the probability of grabbing a more dominant price, thereby increasing profit.**

**Notice: This strategy is to adjust the current price range fluctuations in the spot market.** 

 

**Moreover, KuCoin provides the transaction data of level 3, great matching engine, and the commission discount specially offers to the API customers, which could greatly reduce the disadvantages of the trading operations. At the same time, we offer the sandbox environment as the data testing support to avoid the risks.**

**Only a simple and incomplete trading strategy is provided here, so please pay attention to avoiding risks when using it. Of course, we do not want you to suffer more losses, so please do not directly run it in the actual environment before you have tested it yourself. We do not want you to become a philanthropist! ! !**

**If you want to use the strategy in the actual environment to earn stable profits, we hope that you can make test adjustments in the sandbox environment with other parameters or strategies to enable you to achieve your goals. We also look forward to sharing your test data and Insights.**

**Surely, if you encounter any problems in this process, or you have a profitable strategy to share, please reflect in ISSUE, we will try to respond in a timely manner.**

## How to use

* After clone this project to your local, install the dependency: 

  ```shell script
  pip install kucoin-python
  ```

* Paste config.json.example,  rename as config.json, then add the relevant configuration information:   

  ```
  {  
    "api_key": "api key",
    "api_secret": "api secret",
    "api_passphrase": "api pass phrase",
    // if sandbox
    "is_sandbox": true,
    // contract name, e.g.: BTC  
    "symbol": "coin name",
    // minimum trading threshold
    "min_param": "minimal value for symbol transaction",
    // the nunmbers of fluctuations to place an order
    "price_param": "price interval for creating an order"
  }
  ```

  

* Run your strategy

  ```shell
  ./avg_position.py
  ```

  
