

dict_bq = {'schema':
    [
        {'name': 'total_quantity', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'unique_purchases', 'type': 'INTEGER', 'mode': 'NULLABLE'}, 
        {'name': 'visitor_id', 'type': 'STRING', 'mode': 'NULLABLE'}, 
        {'name': 'user_id', 'type': 'STRING', 'mode': 'NULLABLE'}, 
        {'name': 'cookie_id', 'type': 'STRING', 'mode': 'NULLABLE'}, 
        {'name': 'source', 'type': 'STRING', 'mode': 'NULLABLE'}, 
        
        {'name': 'referrer_type', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [{'name': 'code', 'type': 'INTEGER', 'mode': 'NULLABLE'}, {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'}]},
        {'name': 'products', 'type': 'RECORD', 'mode': 'REPEATED', 'fields': [{'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'sku', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'price', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'dimension8', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'dimension9', 'type': 'STRING', 'mode': 'NULLABLE'}]},
        
        {'name': 'referrer_url', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'campaign_name', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'custom_event_category', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'custom_event_action', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'custom_event_name', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'custom_event_value', 'type': 'FLOAT', 'mode': 'NULLABLE'}, {'name': 'event_custom_dimension_1', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'event_custom_dimension_5', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'event_custom_dimension_7', 'type': 'STRING', 'mode': 'NULLABLE'}, {'name': 'visitor_session_number', 'type': 'INTEGER', 'mode': 'NULLABLE'}
        ]}

def get_query_args_schema(keys = True):
    # List of field for Piwik Pro available in the following documentation: 
    # https://developers.piwik.pro/en/latest/custom_reports/columns.html
    schema = {'schema':
        [
        {'name': "total_quantity", "type": "INT64"},
        {'name': "unique_purchases", "type": "INT64"},
        {'name': "visitor_id", "type": "STRING"},
        {'name': "user_id", "type": "STRING"},
        {'name': "cookie_id", "type": "STRING"},
        {'name': "source", "type": "STRING"},
        {'name': "medium", "type": "STRING"},
        {'name': "keyword", "type": "STRING"},
        {'name': "referrer_type",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "INT64"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "products.name", "type": "STRING"},
        {'name': "products.sku", "type": "STRING"},
        {'name': "products.price", "type": "STRING"},
        {'name': "products.quantity", "type": "FLOAT"},
        {'name': "products.revenue", "type": "FLOAT"},
        {'name': "products.brand", "type": "STRING"},
        {'name': "products.variant", "type": "STRING"},
        {'name': "products.category", "type": "STRING"},
        {'name': "products.category1", "type": "STRING"},
        {'name': "products.category2", "type": "STRING"},
        {'name': "products.category3", "type": "STRING"},
        {'name': "products.category4", "type": "STRING"},
        {'name': "products.category5", "type": "STRING"},
        {'name': "products.dimension1", "type": "STRING"},
        {'name': "products.dimension2", "type": "STRING"},
        {'name': "products.dimension3", "type": "STRING"},
        {'name': "products.dimension4", "type": "STRING"},
        {'name': "products.dimension5", "type": "STRING"},
        {'name': "products.dimension6", "type": "STRING"},
        {'name': "products.dimension7", "type": "STRING"},
        {'name': "products.dimension8", "type": "STRING"},
        {'name': "products.dimension9", "type": "STRING"},
        {'name': "products.dimension10", "type": "STRING"},
        {'name': "products.dimension11", "type": "STRING"},
        {'name': "products.dimension12", "type": "STRING"},
        {'name': "products.dimension13", "type": "STRING"},
        {'name': "products.dimension14", "type": "STRING"},
        {'name': "products.dimension15", "type": "STRING"},
        {'name': "products.dimension16", "type": "STRING"},
        {'name': "products.dimension17", "type": "STRING"},
        {'name': "products.dimension18", "type": "STRING"},
        {'name': "products.dimension19", "type": "STRING"},
        {'name': "products.dimension20", "type": "STRING"},
        {'name': "referrer_url", "type": "STRING"},
        {'name': "campaign_name", "type": "STRING"},
        {'name': "campaign_id", "type": "STRING"},
        {'name': "campaign_content",  "type": "STRING"},
        {'name': "campaign_gclid", "type": "STRING"},
        {'name': "operating_system",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "operating_system_version", "type": "STRING"},
        {'name': "browser_engine", "type": "STRING"},
        {'name': "browser_name",  "type": "RECORD", "mode": "REPEATED","fields":[ #new
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "browser_version",  "type": "STRING"},
        {'name': "browser_language_iso639",  "type": "RECORD", "mode": "REPEATED","fields":[ #new
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "browser_fingerprint", "type": "INT64"},
        {'name': "device_type",  "type": "RECORD", "mode": "REPEATED","fields":[ #new
            {"name": "code", "type": "INT64"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "device_brand",  "type": "RECORD", "mode": "REPEATED","fields":[ #new
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "device_model",  "type": "STRING"},
        {'name': "location_continent_iso_code",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "location_country_name",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "download_url",  "type": "STRING"},
        {'name': "location_subdivision_2_name",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "session_entry_title",  "type": "STRING"},
        {'name': "is_bounce",  "type": "INT64"},
        {'name': "event_id", "type": "STRING"},
        {'name': "session_id", "type": "STRING"},
        {'name': "is_exit", "type": "BOOLEAN"},
        {'name': "is_entry",  "type": "INT64"},
        {'name': "event_type",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "INT64"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "event_url", "type": "STRING"},
        {'name': "event_title", "type": "STRING"},
        {'name': "outlink_url", "type": "STRING"},
        {'name': "search_keyword",  "type": "STRING"},
        {'name': "search_category", "type": "STRING"},
        {'name': "search_results_count", "type": "INT64"},
        {'name': "custom_event_category", "type": "STRING"},
        {'name': "custom_event_action", "type": "STRING"},
        {'name': "custom_event_name", "type": "STRING"},
        {'name': "custom_event_value", "type": "FLOAT"},
        {'name': "content_name", "type": "STRING"},
        {'name': "content_piece", "type": "STRING"},
        {'name': "content_target", "type": "STRING"},
        {'name': "event_index", "type": "INT64"},
        {'name': "page_view_index", "type": "INT64"},
        {'name': "time_on_page", "type": "INT64"},
        {'name': "page_generation_time", "type": "FLOAT"},
        {'name': "goal_id",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "INT64"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "goal_uuid",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "timestamp", "type": "DATETIME"},        
        {'name': "goal_revenue", "type": "FLOAT"},
        {'name': "lost_revenue", "type": "FLOAT"},
        {'name': "order_id",  "type": "STRING"},
        {'name': "revenue", "type": "FLOAT"},
        {'name': "revenue_subtotal", "type": "FLOAT"},
        {'name': "revenue_tax", "type": "FLOAT"},
        {'name': "revenue_shipping", "type": "FLOAT"},
        {'name': "revenue_discount", "type": "FLOAT"},
        {'name': "timing_dom_interactive", "type": "INT64"},
        {'name': "timing_event_end", "type": "INT64"},
        {'name': "consent_source",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "INT64"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "consent_form_button",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "INT64"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "consent_scope",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "INT64"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "consent_action",  "type": "RECORD", "mode": "REPEATED","fields":[ #NEW
            {"name": "code", "type": "INT64"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "consent_type_remarketing", "type": "BOOLEAN"},
        {'name': "consent_type_user_feedback", "type": "BOOLEAN"},
        {'name': "consent_type_custom_1", "type": "BOOLEAN"},
        {'name': "event_custom_dimension_1", "type": "STRING"},
        {'name': "event_custom_dimension_2", "type": "STRING"},
        {'name': "event_custom_dimension_3", "type": "STRING"},
        {'name': "event_custom_dimension_4", "type": "STRING"},
        {'name': "event_custom_dimension_5", "type": "STRING"},
        {'name': "event_custom_dimension_6", "type": "STRING"},
        {'name': "event_custom_dimension_7", "type": "STRING"},
        {'name': "event_custom_dimension_8", "type": "STRING"},
        {'name': "event_custom_dimension_9", "type": "STRING"},
        {'name': "event_custom_dimension_10", "type": "STRING"},
        {'name': "event_custom_dimension_11", "type": "STRING"},
        {'name': "event_custom_dimension_12", "type": "STRING"},
        {'name': "event_custom_dimension_13", "type": "STRING"},
        {'name': "event_custom_dimension_14", "type": "STRING"},
        {'name': "event_custom_dimension_15", "type": "STRING"},
        {'name': "event_custom_dimension_16", "type": "STRING"},
        {'name': "event_custom_dimension_17", "type": "STRING"},
        {'name': "event_custom_dimension_18", "type": "STRING"},
        {'name': "event_custom_dimension_19", "type": "STRING"},
        {'name': "event_custom_dimension_20", "type": "STRING"},
        {'name': "event_custom_variable_key_1", "type": "STRING"},
        {'name': "event_custom_variable_value_1", "type": "STRING"},
        {'name': "event_custom_variable_key_2", "type": "STRING"},
        {'name': "event_custom_variable_value_2", "type": "STRING"},
        {'name': "event_custom_variable_key_3", "type": "STRING"},
        {'name': "event_custom_variable_value_3", "type": "STRING"},
        {'name': "event_custom_variable_key_4", "type": "STRING"},
        {'name': "event_custom_variable_value_4", "type": "STRING"},
        {'name': "event_custom_variable_key_5", "type": "STRING"},
        {'name': "event_custom_variable_value_5", "type": "STRING"},
        {'name': "session_custom_dimension_1", "type": "STRING"},
        {'name': "session_custom_dimension_2", "type": "STRING"},
        {'name': "session_custom_dimension_3", "type": "STRING"},
        {'name': "session_custom_dimension_4", "type": "STRING"},
        {'name': "session_custom_dimension_5", "type": "STRING"},
        {'name': "session_custom_variable_key_1", "type": "STRING"},
        {'name': "session_custom_variable_value_1", "type": "STRING"},
        {'name': "session_custom_variable_key_2", "type": "STRING"},
        {'name': "session_custom_variable_value_2", "type": "STRING"},
        {'name': "session_custom_variable_key_3", "type": "STRING"},
        {'name': "session_custom_variable_value_3", "type": "STRING"},
        {'name': "session_custom_variable_key_4", "type": "STRING"},
        {'name': "session_custom_variable_value_4", "type": "STRING"},
        {'name': "session_custom_variable_key_5", "type": "STRING"},
        {'name': "session_custom_variable_value_5", "type": "STRING"},
        {'name': "server_connection_time", "type": "INT64"},
        {'name': "ipv4_address", "type": "STRING"},
        {'name': "ipv6_address", "type": "STRING"},
        {'name': "website_name",  "type": "RECORD", "mode": "REPEATED","fields":[
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "location_subdivision_1_name",  "type": "RECORD", "mode": "REPEATED","fields":[
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "location_city_name",  "type": "RECORD", "mode": "REPEATED","fields":[
            {"name": "code", "type": "INT64"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "location_metro_code",  "type": "RECORD", "mode": "REPEATED","fields":[
            {"name": "code", "type": "STRING"},
            {"name": "name", "type": "STRING"},
        ]},
        {'name': "location_organization", "type": "STRING"},
        {'name': "session_exit_url", "type": "STRING"},
        {'name': "session_exit_title", "type": "STRING"},
        {'name': "session_entry_url", "type": "STRING"},
        {'name': "item_count", "type": "STRING"},
        {'name': "consent_type_analytics", "type": "STRING"},
        {'name': "consent_type_ab_testing_personalization", "type": "STRING"},
        {'name': "consent_type_conversion_tracking", "type": "STRING"},
        {'name': "consent_type_marketing_automation", "type": "STRING"},
        {'name': "visitor_session_number", "type": "INT64"},
        ]
    }
    return schema

dict_piwik = get_query_args_schema(keys=True)

"""
def filter_dict_piwik(schema_bq, schema_piwik):
    schema_piwik_filtered = list()
    list_not_nested_bq_columns = [item['name'] for item in schema_bq['schema']]
    for column_dict in schema_piwik['schema']:
        if 'mode' not in column_dict:
            # Check if there is a dot in "name" value which implies nested fields
            if '.' not in column_dict["name"]:
                # No nested field, we check if we have the column in BQ
                if column_dict['name'] in list_not_nested_bq_columns:
                    schema_piwik_filtered.append(column_dict) 
            else: # We have a nested fields materialized by a dot
                parent, child = column_dict['name'].split('.')
                if parent in list_not_nested_bq_columns:
                    # Retrieve the dict of nested field for this parent in BQ
                    index_parent_bq = list_not_nested_bq_columns.index(parent)
                    parent_dict_bq = schema_bq['schema'][index_parent_bq]
                    list_child_bq = [field['name'] for field in parent_dict_bq['fields']]
                    if child in list_child_bq :
                        schema_piwik_filtered.append(column_dict) 
        else:
            # There is a mode key for this column and based on 
            # get_query_args_schema() it is always equal to "REPEATED"
            # In this case we need to only keep the fields present in bq_schema
            # We check if the nested field exist in BQ first
            if column_dict['name'] in list_not_nested_bq_columns:
                filtered_nested_field = list()
                nested_field_piwik = column_dict["fields"]
                dict_bq = schema_bq['schema'][list_not_nested_bq_columns.index(column_dict["name"])]
                list_nested_field_bq = [item['name'] for item in dict_bq['fields']]
                for field in nested_field_piwik:
                    if field['name'] in list_nested_field_bq:
                        filtered_nested_field.append(field)
                # We rewrite fields value in the current column dict based on 
                # filtered_nested_field and we append the element to schema_piwik_filtered
                column_dict['fields'] = filtered_nested_field
                schema_piwik_filtered.append(column_dict)
    # Create the dict schema_piwik with a key 'schema'
    schema_piwik_filtered = {'schema':schema_piwik_filtered}
    return schema_piwik_filtered
"""
def filter_dict_piwik(schema_bq, schema_piwik):
    """
    Filters the `schema_piwik` dictionary to only include fields that are present in `schema_bq`.

    This function compares two schemas: `schema_bq` (BigQuery schema) and `schema_piwik`.
    It filters out fields in `schema_piwik` that do not exist in `schema_bq`. The filtering
    handles both non-nested and nested fields. Additionally, if a field is repeated (has a "mode" key),
    the function ensures only the nested fields present in the BigQuery schema are kept.

    Args:
        schema_bq (dict): A dictionary representing the BigQuery schema. It has a `schema` key that contains
                          a list of field dictionaries, each with a 'name' key and, in the case of nested fields,
                          a 'fields' key.
        schema_piwik (dict): A dictionary representing the Piwik schema. It follows the same structure as `schema_bq`.

    Returns:
        dict: A filtered version of `schema_piwik` where only fields and nested fields that exist
              in `schema_bq` are retained.
    """
    schema_piwik_filtered = []
    list_not_nested_bq_columns = {item['name']: item for item in schema_bq['schema']}
    for column_dict in schema_piwik['schema']:
        column_name = column_dict['name']
        if 'mode' not in column_dict:
            # Non-nested field
            if '.' not in column_name:
                if column_name in list_not_nested_bq_columns:
                    schema_piwik_filtered.append(column_dict)
            else:
                # Nested field
                parent, child = column_name.split('.')
                parent_dict_bq = list_not_nested_bq_columns.get(parent)
                if parent_dict_bq:
                    bq_children = {field['name'] for field in parent_dict_bq['fields']}
                    if child in bq_children:
                        schema_piwik_filtered.append(column_dict)
                        
        else:
            # Handling repeated fields (mode == "REPEATED")
            bq_dict = list_not_nested_bq_columns.get(column_name)
            if bq_dict:
                nested_field_piwik = column_dict["fields"]
                bq_children = {field['name'] for field in bq_dict['fields']}
                filtered_nested_field = [field for field in nested_field_piwik if field['name'] in bq_children]
                if filtered_nested_field:
                    column_dict['fields'] = filtered_nested_field
                    schema_piwik_filtered.append(column_dict)       
    return {'schema': schema_piwik_filtered}
                

      			


# Filter dict_piwik based on dict_bq
#filtered_piwik_schema = filter_dict_piwik(dict_bq, dict_piwik)

# Output the filtered schema
#print(filtered_piwik_schema)

nested_fields = []
for field in dict_bq['schema']:
    if field['name'] == 'products' and 'fields' in field:
        # Extract nested field names
        nested_fields = [f"products.{nested_field['name']}" for nested_field in field['fields']]
        break


product_keys = [key.split('.')[-1] for key in nested_fields]
print(product_keys)
#zipped_all_products = list(zip(*[data[f'products.{key}'] for key in product_keys]))
