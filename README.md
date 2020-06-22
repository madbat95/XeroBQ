# XeroBQ
the project is a simple tool for performing ETL where the data is etched from XeroAPI into Google BigQuery 

#MINIMAL CONFIGURATION:
1. etl.ini has sections for bigquery adn Xero configuration. the application requires you to put access and refresh tokens otherwise it would retrieve data from the local json files.
2. Google BigQuery authentication file is already mentioned in the etl.ini file.
3. python install -r requirements.txt
#How To Run
python xeroapi.py

good to go :)
