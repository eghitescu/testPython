import pandas as pd

data = {
    "links": {
        "self": "http://neocase.neocase.local:80/v2.0/Portals?startConnectionDate=2022-12-01&endConnectionDate=2023-02-15&detailLevel=2&page=1&perPage=1000"
    },
    "page": 1,
    "pageCount": 1,
    "perPage": 1000,
    "size": 2,
    "totalSize": 2,
    "results": [
        {
            "connectionId": 82502,
            "connectionDate": "2023-01-11T17:31:11.387",
            "connectionDuration": 5936,
            "portalName": "HR Portail",
            "portalId": 1011,
            "employee": "BLAGUIN Jean",
            "employeeId": "2315",
            "organization": "GLOBAL COMPANY",
            "organizationId": 20000148,
            "pages": [
                {
                    "pageId": 1459,
                    "pageName": "Départ volontaire",
                    "visitDate": "2023-01-11T17:32:35.333",
                    "actions": [
                        {
                            "actionName": "CreatedCase",
                            "actionDate": "2023-01-11T17:34:04.96"
                        }
                    ]
                },
                {
                    "pageId": 1399,
                    "pageName": "Accueil",
                    "visitDate": "2023-01-11T17:31:20.403",
                    "actions": [
                        {
                            "actionName": "CreatedCase",
                            "actionDate": "2023-01-11T17:31:48.2"
                        }
                    ]
                },
                {
                    "pageId": 1409,
                    "pageName": "Autres demandes",
                    "visitDate": "2023-01-11T17:32:13.49",
                    "actions": [
                        {
                            "actionName": "CreatedCase",
                            "actionDate": "2023-01-11T17:34:04.96"
                        },
                        {
                            "actionName": "ModifiededCase",
                            "actionDate": "2023-01-11T18:34:04.96"
                        }

                    ]
                },
                {
                    "pageId": 1401,
                    "pageName": "Connexion",
                    "visitDate": "2023-01-11T17:31:15.38",
                    "actions": []
                }
            ]
        },
        {
            "connectionId": 82501,
            "connectionDate": "2023-01-11T17:28:09.897",
            "connectionDuration": 180,
            "portalName": "HR Portail",
            "portalId": 1011,
            "employee": "NOM Prénom",
            "employeeId": "0",
            "organization": "ORGANIZATION NOT FOUND",
            "organizationId": 0,
            "pages": [
                {
                    "pageId": 1401,
                    "pageName": "Connexion",
                    "visitDate": "2023-01-11T17:28:10.74",
                    "actions": [
                        {
                            "actionName": "CreatedCase",
                            "actionDate": "2023-01-11T17:34:04.96"
                        }
                    ]
                }
            ]
        }
    ]
}

print(data["results"])
new_data = data["results"]
print(new_data)

df_global = pd.DataFrame.from_records(new_data)

record_path_actions = ["pages", "actions"]
meta_actions = ["connectionId", ["pages", "pageId"]]
df_actions = pd.json_normalize(new_data, record_path=record_path_actions, meta=meta_actions, errors='ignore')

record_path_pages = ["pages"]
meta_pages = ["connectionId"]
df_pages = pd.json_normalize(new_data, record_path=record_path_pages, meta=meta_pages, errors='ignore', max_level=1)
df_pages = df_pages.loc[ : , df_pages.columns!="actions"]

df_connections = pd.json_normalize(new_data)
df_connections = df_connections.loc[ : , df_connections.columns!="pages"]



print("done")
