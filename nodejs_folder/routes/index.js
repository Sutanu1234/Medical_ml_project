const express = require('express');
const router = express.Router();
const { checkAuth } = require('../middleware/auth');
const axios = require('axios');

// Use the checkAuth middleware
router.use(checkAuth);

// Route to render the home page
router.get('/', (req, res) => {
  const isAuthenticated = req.user !== null; // Assuming req.user determines authentication status
  res.render('layout', { isAuthenticated: isAuthenticated });
});

// Route to render the login page
router.get('/login', (req, res) => {
  res.render('../views/login.ejs');
});

// Route to render the signup page
router.get('/signup', (req, res) => {
  res.render('../views/signup.ejs');
});

// Server-side logout route handling (example in Express.js)
router.post('/logout', (req, res) => {
  res.clearCookie('uid');
  
  // Clear browser cache to prevent going back to the previous state
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');
  
  // Set isAuthenticated to false after logout
  isAuthenticated = false;
  
  // Redirect to the home page
  res.render('layout', { isAuthenticated: isAuthenticated });
});
//blog post
router.get('/blog', (req, res) => {
  res.render('../views/blogLayout.ejs');
});

//profile
router.get('/profile', (req, res) => {
  res.render('../views/profile.ejs');
});

//Route to render the diabetes form page
router.get('/predict', (req, res) => {
  res.render('../views/diabetesForm.ejs');
});

router.post('/predict', async (req, res) => {
  const inputData = {
    Pregnancies: req.body.pregnancies,
    Glucose: req.body.glucose,
    BloodPressure: req.body.blood_pressure,
    SkinThickness: req.body.skin_thickness,
    Insulin: req.body.insulin,
    BMI: req.body.bmi,
    DiabetesPedigreeFunction: req.body.diabetes_pedigree,
    Age: req.body.age
  };

  try {
      const response = await axios.post('http://127.0.0.1:8000/predict', inputData);
      const prediction = response.data.prediction;
      res.render('DiabetesResult', { prediction: prediction });
  } catch (error) {
      res.status(500).send('Error making prediction');
  }
});

module.exports = router;
