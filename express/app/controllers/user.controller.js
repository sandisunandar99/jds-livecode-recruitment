const User = require("../models/user.model.js");

exports.create = (req, res) => {
  // Validate request
  if (!req.body) {
    res.status(400).send({
      message: "Content can not be empty!"
    });
  }

  // Create a User
  const user = new User({
    nama = req.body.name,
    nik = req.body.nik,
    email = req.body.email,
    no_tlp = req.body.no_tlp,
    alamat = req.body.alamat,
    kode_karyawan = req.body.kode_karyawan
  });

  // Save User in the database
  User.create(user, (err, data) => {
    if (err)
      res.status(500).send({
        message:
          err.message || "Some error occurred while creating the Customer."
      });
    else res.send(data);
  });

  
};

