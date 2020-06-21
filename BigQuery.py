import configparser
import json
import os

from google.cloud import bigquery
config = configparser.ConfigParser()
config.read('etl.ini')
print(config['google_bigquery']['environment_variable_path'])
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config['google_bigquery']['environment_variable_path']
# Construct a BigQuery client object.

def BQcall(reader,table_id):
    # with open('nd-proceesed.json','r') as f:
    #     reader=json.load(f)
    print(reader)
    # reader =[{"Type": "ACCREC","InvoiceID": "fee88eea-f2aa-4a71-a372-33d6d83d3c45","HasErrors": False}]
    # reader='\n'.join(result)
    # reader =[{"Type": "ACCREC", "InvoiceID": "fee88eea-f2aa-4a71-a372-33d6d83d3c45", "InvoiceNumber": "INV-0027", "Reference": "Ref MK815", "Payments": [], "CreditNotes": [], "Prepayments": [], "Overpayments": [], "AmountDue": 396.0, "AmountPaid": 0.0, "AmountCredited": 0.0, "CurrencyRate": 1.0, "IsDiscounted": false, "HasAttachments": false, "HasErrors": false, "Contact": {"ContactID": "5b96e86b-418e-48e8-8949-308c14aec278", "Name": "Marine Systems", "Addresses": [], "Phones": [], "ContactGroups": [], "ContactPersons": [], "HasValidationErrors": false}, "DateString": "2020-06-19T00:00:00", "Date": "/Date(1592524800000+0000)/", "DueDateString": "2020-06-25T00:00:00", "DueDate": "/Date(1593043200000+0000)/", "BrandingThemeID": "d613f7f9-8fcb-477f-97f0-31eb85b7e5cf", "Status": "AUTHORISED", "LineAmountTypes": "Inclusive", "LineItems": [], "SubTotal": 365.82, "TotalTax": 30.18, "Total": 396.0, "UpdatedDateUTC": "/Date(1229650679057+0000)/", "CurrencyCode": "USD"}]
    # client = bigquery.Client()
    project_id = 'lucky-wonder-280516'
    dataset_id = 'Invoices'
    # table_id = 'Invoice'

    client = bigquery.Client(project=project_id)
    dataset = client.dataset(dataset_id)
    table = dataset.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    # job_config.autodetect = True
    job = client.load_table_from_json(reader, table, job_config=job_config)

    print(job.result())
    # query = """insert * from lucky-wonder-280516.Invoices.Invoice"""
    # query_job = client.query(query)  # Make an API request.

    # print(f"The query data: {query_job}")
    # for row in query_job:
    #     printrow
        # Row values can be accessed by field name or index.
        # print(f'{row}')
#
#
# if __name__ == "__main__":
#     BQcall()

# cat test.json | jq -c '.[]' > testNDJSON.json
#{"Invoices": [{"name": "Hammad","age": "22"}]}