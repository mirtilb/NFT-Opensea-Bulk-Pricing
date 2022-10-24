# NFT-Opensea-Bulk-Pricing
Solution to set fixed price to NFTs with a CSV including URL + ETH Price 


Goal			SET PRICE ON OPENSEA in BULK</br>
Project			No More TV (NMTV)</br>
Developer		syed_aj</br>
			https://github.com/SyedAzeemJaved
			https://www.fiverr.com/syed_aj</br>

---------------

<strong>REQUIREMENT</strong></br>

- your custom smart contract (not freely minted using the "OpenSea Shared Storefront")
- Metamask account
- chromedriver + selenium already installed
- CSV including URL + price for each collectible

URL format</br>
https://opensea.io/assets/[SMART_CONTRACT_ADDRESS]/[COLLECTIBLE_ID]

----------------

<strong>HOW IT WORKS</strong></br>

- the script run each URL from the CSV
- it detects if collectibles is new to SELL or if already in SELL LOWER mode.
- after adding PRICE, it'll confirm METAMASK automatically
- if SELL LOWER mode, it'll  automatically check if price if not lower, then ignore the collectible and report the error in CSV ouput.

----------------

<strong>STEPS</strong></br>
01. Make sure the CSV is in assets/input/updatePrice.csv (It is important that we do not change its name and format)
02. Also we will get an output in assets/output
03. Open tasks-mirtil/task-2/openSea/bot in terminal, you can use cd or the shortcut.
04. In terminal window type "python3 main.py"
05. You will be prompted to import your Metamask account, then you have to log to OPENSEA (eg. : go to your user profile) using Metamask again.
06. After successfully logging in press "y" on terminal and hit enter.
07. Script will automatically run and you can check errors in the output CSV file (eg. : set a price too high for "lower price"...etc.).
