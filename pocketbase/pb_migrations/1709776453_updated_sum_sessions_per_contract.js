/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("dtf4akjndbfwoev")

  collection.options = {
    "query": "SELECT\n  contracts.id,\n  customers.forename,\n  customers.surname,\n  (\n    SELECT IFNULL(SUM(sessions.duration),0)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type = 'call'\n  ) as call_duration_sum,\n  (\n    SELECT IFNULL(SUM(sessions.duration),0)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type != 'call'\n  ) as data_duration_sum,\n  (\n    SELECT IFNULL(SUM(sessions.data_volume),0)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type != 'call'\n  ) as data_volume_sum\nFROM\n  contracts,\n  customers\nWHERE\n  customers.id = contracts.customer"
  }

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

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "espwdyoa",
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
    "id": "vx4qndn5",
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
    "id": "kxwjscy6",
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
    "id": "otncoard",
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
    "id": "zfjn7u8a",
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
    "query": "SELECT\n  contracts.id,\n  customers.forename,\n  customers.surname,\n  (\n    SELECT 0+SUM(sessions.duration)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type = 'call'\n  ) as call_duration_sum,\n  (\n    SELECT 0+SUM(sessions.duration)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type != 'call'\n  ) as data_duration_sum,\n  (\n    SELECT 0+SUM(sessions.data_volume)\n    FROM sessions\n    WHERE sessions.contract = contracts.id\n    AND sessions.service_type != 'call'\n  ) as data_volume_sum\nFROM\n  contracts,\n  customers\nWHERE\n  customers.id = contracts.customer"
  }

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

  // remove
  collection.schema.removeField("espwdyoa")

  // remove
  collection.schema.removeField("vx4qndn5")

  // remove
  collection.schema.removeField("kxwjscy6")

  // remove
  collection.schema.removeField("otncoard")

  // remove
  collection.schema.removeField("zfjn7u8a")

  return dao.saveCollection(collection)
})
