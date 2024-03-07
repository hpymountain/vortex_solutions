/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dtf4akjndbfwoev")

  collection.options = {
    "query": "SELECT\n  contracts.id,\n  customers.forename,\n  customers.surname,\n  (\n    SELECT 0+SUM(sessions.duration)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type = 'call'\n  ) as call_duration_sum,\n  (\n    SELECT 0+SUM(sessions.duration)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type != 'call'\n  ) as data_duration_sum,\n  (\n    SELECT 0+SUM(sessions.data_volume)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type != 'call'\n  ) as data_volume_sum\nFROM\n  contracts,\n  customers\nWHERE\n  customers.id = contracts.customer"
  }

  // remove
  collection.schema.removeField("rb6n3hjx")

  // remove
  collection.schema.removeField("boef6cmz")

  // remove
  collection.schema.removeField("2owf81ld")

  // remove
  collection.schema.removeField("qcyrau23")

  // remove
  collection.schema.removeField("qdlpabuh")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "lkxgphgs",
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
    "id": "bcsio3vy",
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
    "id": "jnagdj2y",
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
    "id": "p2y1wgpt",
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
    "id": "4zx4nsvj",
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

  collection.options = {
    "query": "SELECT\n  contracts.id,\n  customers.forename,\n  customers.surname,\n  (\n    SELECT SUM(sessions.duration)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type = 'call'\n  ) as call_duration_sum,\n  (\n    SELECT SUM(sessions.duration)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type != 'call'\n  ) as data_duration_sum,\n  (\n    SELECT SUM(sessions.data_volume)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type != 'call'\n  ) as data_volume_sum\nFROM\n  contracts,\n  customers\nWHERE\n  customers.id = contracts.customer"
  }

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "rb6n3hjx",
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
    "id": "boef6cmz",
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
    "id": "2owf81ld",
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
    "id": "qcyrau23",
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
    "id": "qdlpabuh",
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
  collection.schema.removeField("lkxgphgs")

  // remove
  collection.schema.removeField("bcsio3vy")

  // remove
  collection.schema.removeField("jnagdj2y")

  // remove
  collection.schema.removeField("p2y1wgpt")

  // remove
  collection.schema.removeField("4zx4nsvj")

  return dao.saveCollection(collection)
})
