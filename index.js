var express = require('express');
var app = express();
var mysql = require('mysql');
var path=require('path');
var bodyParser = require('body-parser');
app.set("view engine", "ejs"); 
app.set("views", __dirname + "/views"); 
app.use(bodyParser.urlencoded({ extended: false })); 
const PORT = process.env.PORT || 8800;

app.get("/", (req, res) => {

	var con = mysql.createConnection({
	  host: "us-cdbr-east-02.cleardb.com",
	  user: "b1abe9ea04ccbe",
	  password: "808435a1",
	  database: "heroku_47d4dcb9ec5878d"
	});

	con.connect(function(err) {
	  if (err) throw err;
	  con.query("SELECT * FROM moisture", function (err, result, fields) {
	    if (err) throw err;
	    console.log(result);
	    res.render('index',{result: result});
	  });
	});

});


app.listen(PORT);