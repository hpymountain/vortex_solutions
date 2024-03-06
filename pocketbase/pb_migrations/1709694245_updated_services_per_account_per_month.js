/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dtf4akjndbfwoev")

  collection.options = {
    "query": "SELECT\n  a.id,\n  a.first_name,\n  a.last_name,\n  (\n    SELECT SUM(services_tracked.duration)\n    FROM services_tracked\n    WHERE services_tracked.account = a.id\n    AND services_tracked.service = 'call'\n  ) as call_duration_sum,\n  (\n    SELECT SUM(services_tracked.duration)\n    FROM services_tracked\n    WHERE services_tracked.account = a.id\n    AND services_tracked.service != 'call'\n  ) as data_duration_sum\nFROM\n  accounts a\n"
  }

  // remove
  collection.schema.removeField("ifnh7xtx")

  // remove
  collection.schema.removeField("djexeksa")

  // remove
  collection.schema.removeField("1haawwad")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "f8oxccyi",
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
    "id": "nql04cuy",
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
    "id": "h4dfgtdc",
    "name": "call_duration_sum",
    "type": "json",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSize": 1
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "sibdifi5",
    "name": "data_duration_sum",
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
    "query": "SELECT\n  a.id,\n  a.first_name,\n  a.last_name,\n  (\n    SELECT SUM(services_tracked.duration)\n    FROM services_tracked\n    WHERE services_tracked.account = a.id\n    AND services_tracked.service = 'call'\n  ) as call_duration_sum\nFROM\n  accounts a\n"
  }

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

  // remove
  collection.schema.removeField("f8oxccyi")

  // remove
  collection.schema.removeField("nql04cuy")

  // remove
  collection.schema.removeField("h4dfgtdc")

  // remove
  collection.schema.removeField("sibdifi5")

  return dao.saveCollection(collection)
})
