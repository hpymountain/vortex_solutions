/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("7mog84aeg4q3w58");

  return dao.deleteCollection(collection);
}, (db) => {
  const collection = new Collection({
    "id": "7mog84aeg4q3w58",
    "created": "2024-03-06 01:23:56.178Z",
    "updated": "2024-03-06 01:29:52.427Z",
    "name": "subscribers",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "krez0wfp",
        "name": "invoice_id",
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
        "id": "u9gyt1s6",
        "name": "name",
        "type": "text",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      }
    ],
    "indexes": [],
    "listRule": "",
    "viewRule": "",
    "createRule": "",
    "updateRule": "",
    "deleteRule": "",
    "options": {}
  });

  return Dao(db).saveCollection(collection);
})
