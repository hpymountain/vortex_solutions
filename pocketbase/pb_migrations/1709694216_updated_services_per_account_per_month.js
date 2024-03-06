/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dtf4akjndbfwoev")

  collection.options = {
    "query": "SELECT\n  a.id,\n  a.first_name,\n  a.last_name,\n  (\n    SELECT SUM(services_tracked.duration)\n    FROM services_tracked\n    WHERE services_tracked.account = a.id\n    AND services_tracked.service = 'call'\n  ) as call_duration_sum\nFROM\n  accounts a\n"
  }

  // remove
  collection.schema.removeField("sdp1st0s")

  // remove
  collection.schema.removeField("nr7ih9qy")

  // remove
  collection.schema.removeField("txtgc3vb")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "ifnh7xtx",
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
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "djexeksa",
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
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "1haawwad",
    "name": "call_duration_sum",
    "type": "json",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSize": 1
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dtf4akjndbfwoev")

  collection.options = {
    "query": "SELECT\n  accounts.id,\n  accounts.first_name,\n  accounts.last_name,\n  sum(services_tracked.duration) as sum_duration\nFROM\n  accounts,\n  services_tracked\nWHERE\n  services_tracked.account = accounts.id\n  AND\n  services_tracked.service != 'call'\nGROUP BY\n  accounts.id,\n  accounts.first_name,\n  accounts.last_name\n"
  }

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "sdp1st0s",
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
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "nr7ih9qy",
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
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "txtgc3vb",
    "name": "sum_duration",
    "type": "json",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSize": 1
    }
  }))

  // remove
  collection.schema.removeField("ifnh7xtx")

  // remove
  collection.schema.removeField("djexeksa")

  // remove
  collection.schema.removeField("1haawwad")

  return dao.saveCollection(collection)
})
