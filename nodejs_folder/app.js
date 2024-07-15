const express = require('express');
const cookieParser = require("cookie-parser");
const { connectToMongoDB } = require("./connect");
//const expressLayouts = require('express-ejs-layouts');
const bodyParser = require('body-parser');
const path = require('path');
const { checkAuth } = require('./middleware/auth');
const app = express();
const PORT = process.env.PORT || 3000;

//mongodb connection
connectToMongoDB(process.env.MONGODB ?? "mongodb+srv://sutanubera82:sutanubera82@cluster1.s0d0ucr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1").then(() =>
    console.log("Mongodb connected")
  );

// EJS setup
//app.use(expressLayouts);
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware to parse URL-encoded bodies (as sent by HTML forms)
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cookieParser());
app.use(checkAuth);

// Cache-control middleware
const nocache = (req, res, next) => {
  res.header('Cache-Control', 'private, no-cache, no-store, must-revalidate');
  res.header('Expires', '-1');
  res.header('Pragma', 'no-cache');
  next();
};

app.use(nocache);

// Routes
const routes = require('./routes/index');
app.use('/',routes);
const userRoute = require("./routes/user");
app.use("/user", userRoute);

// Start the server
app.listen(PORT, () => {
  console.log(`Server started at localhost:${PORT}`);
});
