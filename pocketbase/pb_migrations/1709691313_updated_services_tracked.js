/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("gdkuw64z8d1pqev")

  // remove
  collection.schema.removeField("7llnlcyp")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "qdxl0koz",
    "name": "account",
    "type": "relation",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "collectionId": "jl2q3bdcuvbofh7",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": null
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("gdkuw64z8d1pqev")

  // add
  collection.schema.addField(new SchemaField({
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
  }))

  // remove
  collection.schema.removeField("qdxl0koz")

  return dao.saveCollection(collection)
})
