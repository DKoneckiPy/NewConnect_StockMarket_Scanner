# NewConnect_StockMarket_Scanner

Script containing two tools: getting single company data by ticker and NewConnect(Warsaw Stock Exchange market) market scanner using web scrapping

First tool: user need to enter the name of the company(ticker), starting year month and day. Obtaining data with get_data_stooq

Second tool: Extracting Data with BeautifulSoup from each page (Stooq divides the company list into several parts), setting filter by daily price change (in this case D1>+20%) and drawing charts of price changes for filtered companies

Data source: https://stooq.pl/q/i/?s=ncindex
