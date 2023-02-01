# Meritz arbitrage

## Overview

<p>Mertiz financial group announced their merger decision on 11-21-2022. They will delist their subsidiary firms, Meritz Securities and Meritz Insuarance, and exhchange their stocks for their parental company, Meritz Financial Holdings. The exchange ratios offered by the firm are</p>

<p>1.265738 for Meritz Insurance,</p>

<p>0.1607327 for Meritz Securities.</p>

<p>However, the market price of Meritz Financial Holdings is not always at the exchange ratio, which makes the arbitrage trading opportunity. There are two ways to make the arbitrage trading: futures market and stock market. I will focus on the stock market side since the data is more accessible and the futures market is currently fairly close to the equilibrium.</p>

<p>The discount rates of Meritz Insurance and Meritz Securities are changing every second. The arbitrage trading is only possible when the discount rates are high enough to dominate the trading costs such as brokerage fees and slippage. Thus, I developed a program to monitor the discount rates and send me an email when the discount rates are breached a certain threshold.</p>

<p>The schedule of the merger is as follows:</p>

<b>Insuarance merger dates</b>

2023-02-01 end of trading + 2 days

2023-02-23 issuance of new shares

<b>Securities merger dates</b>

2023-04-05 end of trading + 2 days

2023-04-25 issuance of new shares

## Monitoring(server)

Run `python3.8 meritz-pyanwhere.py` on the server to monitor the discount rates. `meritz-pyanwhere-feb2023.py` is the same program but for after the February 2023 insurance merger. I have used pyanywhere and mailgun services. The program will send you an email when the discount rates are breached a certain threshold. The email will look like this:

Title: [Meritz]INS EXPENSIVE

Content: This is an arbitrage trading alert.

=======2023-01-30 09:32:54.015389+09:00=======

[41800,51600,6410]

disc_rate_ins=2.4719%

disc_rate_sec=4.5936%

## Trading Helper(local)

Run `python3.10 meritz-executable.py` on your machine to keep track of the discount rates real time. This might be useful when you are placing the orders by hand.
<p align="center">
  <img width="773" alt="Screenshot 2022-12-06 at 11 57 04 PM" src="https://user-images.githubusercontent.com/84216960/206325746-31e38ef4-0067-4fa7-97a2-19a8c3f8bc61.png">
</p>

## Jupyter Notebook
`meritz-arbitrage.ipynb` is basically an equivalent version  of the codes from the other files and I was using it for the development purpose. It is not necessary to run the program.

## Disclaimer
This is not a financial advice. I am not responsible for any losses incurred from the use of this program.