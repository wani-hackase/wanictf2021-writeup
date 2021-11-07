var express = require("express");
var router = express.Router();

const { MongoClient } = require("mongodb");
const uri = "mongodb://root:aduhwsfeok@mongo:27017?writeConcern=majority";

router.get("/", function (req, res, next) {
  res.render("login");
});

router.post("/", async function (req, res) {
  const client = new MongoClient(uri);
  try {
    if (!req.body.username || !req.body.password) {
      throw "error";
    }

    await client.connect();
    const user = await client.db("nosql").collection("users").findOne({
      username: req.body.username,
      password: req.body.password,
    });
    if (!user) {
      throw "error";
    }

    req.session.user = user;
    res.redirect("/");
  } catch (error) {
    const debug = JSON.stringify({
      username: req.body.username,
      password: req.body.password,
    });
    res.render("login", { message: "ログインに失敗しました", debug });
  } finally {
    client.close();
  }
});

module.exports = router;
