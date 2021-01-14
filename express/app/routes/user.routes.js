module.exports = app => {
  const users = require("../controllers/user.controller.js");

  app.post("/api/soal1", users.create);

};
