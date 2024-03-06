/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "dtf4akjndbfwoev",
    "created": "2024-03-06 02:59:45.865Z",
    "updated": "2024-03-06 02:59:45.865Z",
    "name": "services_per_account_per_month",
    "type": "view",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "bdgsgfqk",
        "name": "first_name",
        "type": "text",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "3k1ozfkt",
        "name": "last_name",
        "type": "text",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "zfin2em7",
        "name": "sum_duration",
        "type": "json",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "maxSize": 1
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {
      "query": "SELECT\n  accounts.id,\n  accounts.first_name,\n  accounts.last_name,\n  sum(services_tracked.duration) as sum_duration\nFROM\n  accounts,\n  services_tracked\nWHERE\n  services_tracked.account = accounts.id\n  AND\n  services_tracked.service = 'call'\nGROUP BY\n  accounts.id,\n  accounts.first_name,\n  accounts.last_name\n"
    }
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("dtf4akjndbfwoev");

  return dao.deleteCollection(collection);
})
