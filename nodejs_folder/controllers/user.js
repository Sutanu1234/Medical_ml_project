const { v4: uuidv4 } = require("uuid");
const User = require("../models/user");
const { setUser } = require("../service/auth");

async function handleUserSignup(req, res) {
  const { name, email, password } = req.body;

  try {
    await User.create({ name, email, password });
    res.redirect("/"); // Redirect to home or login page after successful signup
  } catch (error) {
    console.error("Error signing up:", error);
    res.render("signup", { error: "Signup failed. Please try again." });
  }
}

async function handleUserLogin(req, res) {
  const { email, password } = req.body;
  const user = await User.findOne({ email, password });

  if (!user)
    return res.render("login", {
      error: "Invalid Username or Password",
    });
  const isAuthenticated = true;
  if (isAuthenticated) {
  const sessionId = uuidv4();
  setUser(sessionId, user);
  res.cookie("uid", sessionId);
    res.redirect('/');
  }
}

module.exports = {
  handleUserSignup,
  handleUserLogin,
};