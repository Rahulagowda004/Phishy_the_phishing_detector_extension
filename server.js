const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(cors()); // Enable CORS for all routes

//url fetcher
app.post("/save-url", (req, res) => {
  const url = req.body.url;
  console.log("Received URL:", url);
  res.send("URL received");
});

//input fetcher
app.post("/save-input", (req, res) => {
  const { input } = req.body;
  if (!input) {
    return res.status(400).json({ error: "Input is required." });
  }
  console.log("Received input:", input);
  res.send("Input received successfully.");
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
