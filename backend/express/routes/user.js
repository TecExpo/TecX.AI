const express = require("express");
const router = express.Router();

let users = [];

// Get all users
router.get("/", (req, res) => {
  res.json(users);
});

// Create a new user
router.post("/", (req, res) => {
  const user = req.body;
  users.push(user);
  res.json({ message: "User created successfully", user });
});

module.exports = router;
