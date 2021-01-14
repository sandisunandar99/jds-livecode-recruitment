const sql = require("./db.js");

// constructor
const User = function(user) {
  this.nama = user.name;
  this.nik = user.nik;
  this.email = user.email;
  this.no_tlp = user.no_tlp;
  this.tgl_lahir = user.tgl_lahir;
  this.alamat = user.alamat;
  this.kode_karyawan = user.kode_karyawan;
};

User.create = (newUser, result) => {
  sql.query("INSERT INTO users SET ?", newUser, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(err, null);
      return;
    }

    console.log("created users: ", { id: res.insertId, ...newUser });
    result(null, { id: res.insertId, ...newUser });
  });
};


module.exports = User;
