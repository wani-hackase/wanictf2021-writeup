var createError = require("http-errors");
var express = require("express");
var path = require("path");
var logger = require("morgan");
var expressLayouts = require("express-ejs-layouts");
var fileUpload = require("express-fileupload");

const crypto = require("crypto");
const fs = require("fs");

var app = express();

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(expressLayouts);
app.set("layout extractScripts", true);

app.use(
  fileUpload({
    limits: { fileSize: 1024 * 1024 },
  })
);

app.use(express.static("public"));

app.use(function (req, res, next) {
  if (res.locals.message == null) {
    res.locals.message = "";
  }
  if (req.method === "POST") {
    const debug = {
      requestHeader: req.headers,
      requestBody: req.body,
    };
    res.locals.debug = JSON.stringify(debug);
  } else {
    res.locals.debug = "";
  }
  next();
});

app.get("/", function (req, res, next) {
  res.render("index");
});

app.post("/chal/1", function (req, res) {
  let FLAG = null;
  if (req.body.data === "hoge") {
    FLAG = process.env.FLAG_PART1;
  }
  res.render("chal", { FLAG, chal: 1 });
});

app.post("/chal/2", function (req, res) {
  // リクエストヘッダのUser-AgentにどのブラウザでもついているMozilla/5.0がある場合のみFLAGを送信
  let FLAG = null;
  if (
    req.headers["user-agent"].includes("Mozilla/5.0") &&
    req.body.data === "hoge"
  ) {
    FLAG = process.env.FLAG_PART2;
  }
  res.render("chal", { FLAG, chal: 2 });
});

app.post("/chal/3", function (req, res) {
  let FLAG = null;
  if (req.body.data?.hoge === "fuga") {
    FLAG = process.env.FLAG_PART3;
  }
  res.render("chal", { FLAG, chal: 3 });
});

app.post("/chal/4", function (req, res) {
  let FLAG = null;
  if (req.body.hoge === 1 && req.body.fuga === null) {
    FLAG = process.env.FLAG_PART4;
  }
  res.render("chal", { FLAG, chal: 4 });
});

function md5file(filePath) {
  const target = fs.readFileSync(filePath);
  const md5hash = crypto.createHash("md5");
  md5hash.update(target);
  return md5hash.digest("hex");
}

app.post("/chal/5", function (req, res) {
  let FLAG = null;
  if (req.files?.data?.md5 === md5file("public/images/wani.png")) {
    FLAG = process.env.FLAG_PART5;
  }
  res.render("chal", { FLAG, chal: 5 });
});

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render("error");
});

module.exports = app;
