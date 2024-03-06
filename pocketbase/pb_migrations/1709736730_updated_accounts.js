/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("jl2q3bdcuvbofh7")

  collection.name = "test_accounts"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("jl2q3bdcuvbofh7")

  collection.name = "accounts"

  return dao.saveCollection(collection)
})
