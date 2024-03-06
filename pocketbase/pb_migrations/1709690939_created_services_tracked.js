/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "gdkuw64z8d1pqev",
    "created": "2024-03-06 02:08:59.690Z",
    "updated": "2024-03-06 02:08:59.690Z",
    "name": "services_tracked",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "7llnlcyp",
        "name": "account",
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
        "id": "eyyzpdee",
        "name": "service",
        "type": "select",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "maxSelect": 1,
          "values": [
            "call",
            "video",
            "browse",
            "download"
          ]
        }
      },
      {
        "system": false,
        "id": "g622oh87",
        "name": "duration",
        "type": "number",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "noDecimal": false
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("gdkuw64z8d1pqev");

  return dao.deleteCollection(collection);
})
