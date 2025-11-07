# 🎲 Dice Rolling App

A simple Streamlit app that simulates rolling a dice. This application allows users to roll a standard six-sided die and see the result.

## Project Structure

```
dice-streamlit-app
├── src
│   ├── streamlit_app.py  # Main entry point for the Streamlit application
│   ├── dice.py           # Logic for simulating dice rolls
│   └── __init__.py       # Marks the directory as a Python package
├── tests
│   └── test_dice.py      # Unit tests for the dice module
├── requirements.txt       # Dependencies for the project
├── .gitignore             # Files and directories to ignore by Git
└── README.md              # Documentation for the project
```

## How to Run the App

1. **Install the requirements**

   ```
   $ pip install -r requirements.txt
   ```

2. **Run the app**

   ```
   $ streamlit run src/streamlit_app.py
   ```

## Features

- Roll a six-sided die and display the result.
- Simple and user-friendly interface.

## Testing

To run the tests for the dice module, use the following command:

```
$ pytest tests/test_dice.py
```

## License

This project is licensed under the MIT License.