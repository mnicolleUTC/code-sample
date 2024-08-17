from google.cloud import bigquery

def check_column_in_table(project_id, dataset_id, table_id):
    # Initialize a BigQuery client
    client = bigquery.Client(project=project_id)
    
    # Construct the table reference
    table_ref = f"{project_id}.{dataset_id}.{table_id}"
    
    # Fetch the table metadata
    table = client.get_table(table_ref)
    
    # Extract column names from the schema
    columns = [schema_field.name for schema_field in table.schema]
    return columns
        


# Example usage
project_id = "make-automation-do-not-delete"
dataset_id = "piwik__test__dekuple"
table_id = "hit"

columns = check_column_in_table(project_id, dataset_id, table_id)
print(columns)