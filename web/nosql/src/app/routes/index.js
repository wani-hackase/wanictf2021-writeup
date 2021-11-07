var express = require("express");
var router = express.Router();

router.get("/", function (req, res, next) {
  if (!req.session.user) {
    return res.redirect("/login");
  }
  res.render("index", { FLAG: process.env.FLAG });
});

module.exports = router;
