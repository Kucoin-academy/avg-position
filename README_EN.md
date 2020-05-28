# Avg_position_strategy

[![Logo](https://img.shields.io/badge/KuCoin-KuMex-yellowgreen?style=flat-square)](https://github.com/Kucoin-academy/Guide)
[![GitHub stars](https://img.shields.io/github/stars/Kucoin-academy/avg-position.svg?label=Stars&style=flat-square)](https://github.com/Kucoin-academy/avg-position)
[![GitHub forks](https://img.shields.io/github/forks/Kucoin-academy/avg-position.svg?label=Fork&style=flat-square)](https://github.com/Kucoin-academy/avg-position)
[![GitHub issues](https://img.shields.io/github/issues/Kucoin-academy/avg-position.svg?label=Issue&style=flat-square)](https://github.com/Kucoin-academy/avg-position/issues)

[![](https://img.shields.io/badge/lang-English-informational.svg?longCache=true&style=flat-square)](README_EN.md)
[![](https://img.shields.io/badge/lang-Chinese-red.svg?longCache=true&style=flat-square)](README_CN.md)

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



**KuCoin** provides **the transaction data of level 3, great matching engine, and the commission discount specially offers to the API customers**. At the same time, we offer the **sandbox environment** as the data testing support to avoid the risks.

Only a simple and incomplete trading strategy is provided here, so please pay attention to **avoiding risks** when using it. We hope that you can **make test adjustments in the sandbox environment with other parameters or strategies,  as we do not want you to become a philanthropist! ! !**

Surely, if you encounter any problems in this process, or you have a profitable strategy to share, please reflect in **ISSUE**, we will try to respond in a timely manner. 

:point_right: If you are interested in this strategy, please click **the star in the upper right corner**, we will  measure **the popularity of this strategy and subsequent optimization prioritie**s based on the amounts of stars. You can also click **watching in the upper right corner** to continue to follow this project by receiving update notifications. 

## How to use

* Download Python

  * Please download python in [Python](https://www.python.org/) official website for other system requirement(Such as **Windows**), if your computer is 64-bit operating system, please click 1, if it is 32-bit operating system, please click 2.

    <img src="./img/python_download.png" style="zoom:50%" />

    * Please note the following options when starting the installation:

      <img src="./img/python_win.png" style="zoom:40%" />

  * For MAC OS X

    * Open terminal and enter the following command to download Homebrew(During the installation, you need to enter the **computer password**):

      ```shell
      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
      ```

    * Enter the following command in terminal to download Python3:

      ```shell
      brew install python
      ```

    * Enter the following command in terminal to confirm if you download successfully:

      ```shell
      python3 --version
      ```

      ![](./img/python_version.gif)

* Confirm that you have already downloaded git(Mac OS  already has this software, enther `which git` in terminal to check the path of the file）, if you did not download this software, please do it through the [git](https://git-scm.com/) official website.

* Enter the following command in terminal to install the dependency:

  ```shell script
  pip3 install kucoin-python
  ```

  ![pip_install](./img/pip_install.gif)
  
* Create a new folder (such as the desktop) at the location where you need to run the strategy, right click on the newly created folder and select "**Create a new terminal window at the folder location**"(For Windows, right click the folder and select "**git Bash here**"), enter the following command in the pop-up window to clone the project to the local, and a folder **avg-position** will be added locally after completion:
  
  ```shell
  git clone https://github.com/Kucoin-academy/avg-position.git
  ```
  
  ![git_clone](./img/git_clone.gif)
  
* Open the (**avg-position**) project you have cloned,  rename **config.json.example** as **config.json**, using text editor(e.g., **notebook**) to open **config.json**, then add the relevant configuration information: 

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
  
* Mac/Linux open terminal **in the project directory**: 

  ```shell
  cd avg-positon
  ```
  * Using the following command to run your strategy:
  
    ```shell
    ./avg_position.py
    ```
  
* Windows open terminal **in the project directory**: 

  ```shell
  cd avg-positon
  ```
  * Using the following command to run your strategy:
  
    ```shell
    py avg_position.py
    ```
  
  

