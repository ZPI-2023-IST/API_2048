# API_2048

### Example call to make_move action

    {
        "move": 1
    }

### The program has a get_response event that is triggered by calling the make_move action and returns to each listener a JSON with the following structure:
```json
    {
  "moves_vector": VECTOR_OF_MOVES,
    "game_board": GAME_BOARD,
    "reward": REWARD,
    "state": STATE,
    "board_raw": BOARD_RAW
}
```
### Example response:


```json
{
  "moves_vector": [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
  ],
  "game_board": [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ],
  "reward": 0.8047189562170501,
  "state": "ONGOING",
  "board_raw": [
    [null, null, 2, null],
    [null, null, null, null],
    [null, null, 2, null],
    [null, null, null, null]
  ]
}
```

### How to open it on your own comp

1. Clone the repo
2. Open the project in your IDE
3. Make venv
4. Install requirements
5. pip3 install git+https://github.com/ZPI-2023-IST/2048.git@fix
6. pip3 install git+https://github.com/ZPI-2023-IST/Translator_2048.git