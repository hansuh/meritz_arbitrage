# meritz_arbitrage

## Overview

Mertiz financial group announced their merger decision on 11-21-2022. They will delist their child firms, Meritz Securities and Meritz Insuarance, and exhchange their stocks for their parental company, Meritz Financial Holdings. The exchange ratios offered by the firm are
<p>1.265738 for Meritz Insurance,</p>
<p>0.1607327 for Meritz Securities.</p>
Thus, the following arbitrage trading opportunity has made and it could be seized by this python trading enviroment.

## Monitoring(server)

Run `python3.8 meritz-pyanwhere.py` on the server to monitor the discount rates. Personally I used pyanywhere and mailgun services.

## Trading Helper(local)

Run `python3.10 meritz-executable.py` on your machine to keep tracking the discount rates real time. This might be useful when you are placing the orders by hand.
<p align="center">
  <img width="773" alt="Screenshot 2022-12-06 at 11 57 04 PM" src="https://user-images.githubusercontent.com/84216960/206325746-31e38ef4-0067-4fa7-97a2-19a8c3f8bc61.png">
</p>

## Jupyter Notebook
`meritz-arbitrage.ipynb` is basically equivalent codes of the other files and I was using it for the development purpose.
