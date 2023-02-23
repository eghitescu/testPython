
staging_tables_map: dict[str, str] = {
    "case": "tracking.case",
    "operation": "tracking.case",
    "customfield": "tracking.case",
    "portal": "tracking.portal"
}

def get_staging_table_name(endpoint_name):
    return  staging_tables_map.get(endpoint_name)

if __name__ == "__main__":
    result=None
    result = get_staging_table_name("blabla")
    print(result)
