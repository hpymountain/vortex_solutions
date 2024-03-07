/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dtf4akjndbfwoev")

  collection.name = "sum_sessions_per_contract"

  // remove
  collection.schema.removeField("icnlyxp8")

  // remove
  collection.schema.removeField("tiz3dfwx")

  // remove
  collection.schema.removeField("sodwdb34")

  // remove
  collection.schema.removeField("nd4wh2tj")

  // remove
  collection.schema.removeField("kleggc9s")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "0zhghsuy",
    "name": "forename",
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
    "id": "afp4pmto",
    "name": "surname",
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
    "id": "nrej0jx9",
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
    "id": "xqnwdd2a",
    "name": "data_duration_sum",
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
    "id": "ejihj9yv",
    "name": "data_volume_sum",
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

  collection.name = "sessions_per_contract"

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "icnlyxp8",
    "name": "forename",
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
    "id": "tiz3dfwx",
    "name": "surname",
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
    "id": "sodwdb34",
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
    "id": "nd4wh2tj",
    "name": "data_duration_sum",
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
    "id": "kleggc9s",
    "name": "data_volume_sum",
    "type": "json",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSize": 1
    }
  }))

  // remove
  collection.schema.removeField("0zhghsuy")

  // remove
  collection.schema.removeField("afp4pmto")

  // remove
  collection.schema.removeField("nrej0jx9")

  // remove
  collection.schema.removeField("xqnwdd2a")

  // remove
  collection.schema.removeField("ejihj9yv")

  return dao.saveCollection(collection)
})
