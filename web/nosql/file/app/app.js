var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");
var session = require("express-session");
var expressLayouts = require("express-ejs-layouts");

var indexRouter = require("./routes/index");
var loginRouter = require("./routes/login");
var logoutRouter = require("./routes/logout");

var app = express();

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.use(expressLayouts);

app.use(
  session({
    resave: true,
    saveUninitialized: true,
    secret: "jancnasdmvkmdevopomvkadlcmla",
  })
);

app.use(function (req, res, next) {
  res.locals.user = req.session.user;
  if (res.locals.message == null) {
    res.locals.message = "";
  }
  if (res.locals.debug == null) {
    res.locals.debug = "";
  }
  next();
});

app.use("/", indexRouter);
app.use("/login", loginRouter);
app.use("/logout", logoutRouter);

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
