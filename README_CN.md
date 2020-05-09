# 均仓策略

[![Logo](https://img.shields.io/badge/KuCoin-KuMex-yellowgreen?style=flat-square)](https://github.com/Kucoin-academy/Guide)
[![GitHub stars](https://img.shields.io/github/stars/Kucoin-academy/simple-grid.svg?label=Stars&style=flat-square)](https://github.com/Kucoin-academy/simple-grid)
[![GitHub forks](https://img.shields.io/github/forks/Kucoin-academy/simple-grid.svg?label=Fork&style=flat-square)](https://github.com/Kucoin-academy/simple-grid)
[![GitHub issues](https://img.shields.io/github/issues/Kucoin-academy/simple-grid.svg?label=Issue&style=flat-square)](https://github.com/Kucoin-academy/simple-grid/issues)

[![](https://img.shields.io/badge/lang-English-informational.svg?longCache=true&style=flat-square)](README.md)
[![](https://img.shields.io/badge/lang-Chinese-red.svg?longCache=true&style=flat-square)](README_CN.md)

## 策略说明

基于现货均衡仓位的策略，本质上是网格策略的简化版。将持有的某种投资标的的仓位占总仓位的比例固定。当超过这个价值比例时，卖出一部分标的；当低于这个价值比例时，买入一部分标的。通过不断调整，使得标的占比一直维持在一个固定值，达到动态的平衡。  

**举个例子** ：假设当前比特币价格10000 USDT，账户同时持有等价值的1个BTC和10000USDT。

场景1：如果币的价值大于账户余额10000 USDT并且差价超过了阈值，如价格上涨到12000 USDT，就卖掉（12000 - 10000）/2/12000 = 0.0833 个BTC，BTC升值了，需要把钱兑换回来。  

场景2：如果币贬值了，比如下跌到8000USDT，则买入（10000 - 8000）/2/8000 = 0.125个BTC，如果再涨了就再卖掉。  

**总结： 此案例中，平衡好标的与总仓位的比例，即维持标底与账户剩余资金的价值比为1:1，所以称为均仓策略**。  

**优势：均仓策略本质为网格策略，其收益来源于价格一定范围内来回波动，所以在震荡行情中表现 会更好**  

**劣势：风险在于执行调仓操作后，价格继续单边上涨或下跌。**  

补充：一般价格变动范围设置在手续费的4倍左右为基准开始调优较为合理，市场活跃时，可以是手续费的1.5~2倍左右。市场不太活跃时，手续费的8倍，十倍，甚至二十，五十倍都是可以的。  

**控制最小交易数量，也可以降低交易频率，增加抓取到更优点位的概率，从而提高收益。**

**请注意，该策略是在现货市场对现价范围波动进行调仓。**



**KuCoin**拥有**level3交易数据、强大的撮合引擎、针对api用户提供的手续费折扣**，同时提供**sandbox环境**作为数据测试支撑，帮助你规避风险。

我们仅提供一个简单且不完备的交易策略，使用时**请注意规避风险**，我们希望你能够**在sandbox环境配合其他参数或是策略进行测试调整，我们也不想你成为一个慈善家！！！**

当然，如果这个过程中，你遇到任何问题或是有赚钱的策略想要分享，请在**ISSUE**中反映，我们会努力及时响应。

:point_right: 如果你对该策略有兴趣，请点击**右上角star**，我们会根据star数来衡量策略的**受欢迎程度和后续优化优先级**，你也可以点击**右上角watching**通过接收更新通知来持续关注该项目。

## 如何使用

* 安装Python

  * Windows系统请前往[Python](https://www.python.org/downloads/windows/)官网自行安装，64位请选择1，32位请选择2。

    <img src="./img/python_download.png" style="zoom:50%" />

    * 在开始安装时请注意将以下选项勾选：

      <img src="./img/python_win.png" style="zoom:40%" />

  * MAC OS X安装

    * 打开命令终端，输入以下命令安装Homebrew（安装过程中需要输入**电脑密码**）：

      ```shell
      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
      ```

    * 在命令终端输入以下命令，安装Python3：

      ```shell
      brew install python
      ```

    * 在命令终端输入以下命令，确认是否安装成功：

      ```shell
      python3 --version
      ```

      ![](./img/python_version.gif)

* 确保你已经安装git (mac 自带该软件,终端输入`which git`，查看安装位置)，未安装者请前往官网[git](https://git-scm.com/)安装。

* 在命令终端输入以下命令，安装项目依赖：

  ```shell script
  pip3 install kucoin-python
  ```

  ![pip_install](./img/pip_install.gif)
  
* 在你需要跑策略的位置新建文件夹（例如桌面），**右键**点击新建的文件夹选择“**新建位于文件夹位置的终端窗口**”（**windows**系统：在右键点击文件夹点击**git Bash here**），在弹出的窗口中输入以下命令，克隆项目至本地，完成后本地会新增文件夹**avg-position**：
  
  ```shell
  git clone https://github.com/Kucoin-academy/avg-position.git
  ```
  
  ![git_clone](./img/git_clone.gif)
  
* 打开克隆好的项目（**avg-position**）文件夹，将**config.json.example**文件重命名为**config.json**，并用文本编辑器（比如**记事本**）打开**config.json**，然后完善相关的配置信息：

  ```
  {  
    "api_key": "api key",
    "api_secret": "api secret",
    "api_passphrase": "api pass phrase",
    // 是否是沙盒环境
    "is_sandbox": true,
    // 货币名称，比如：BTC 
    "symbol": "coin name",
    // 最小买卖阈值
    "min_param": "minimal value for symbol transaction",
    // 当价格变动多少时进行一次买卖下单
    "price_param": "price interval for creating an order"
  }
  ```
  
* Mac/Linux **在项目目录下**打开命令终端：

  ```shell
  cd avg-positon
  ```
  * 用以下命令让你的策略运行起来：
  
    ```shell
    ./avg_position.py
    ```
  
* Windows **在项目目录下**打开命令终端：

  ```shell
  cd avg-positon
  ```
  * 用以下命令让你的策略运行起来：
  
    ```shell
    py avg_position.py
    ```
  
  

