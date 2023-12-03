import json

import socketio
from aiohttp import web

from runner import Runner

sio = socketio.AsyncServer(async_mode="aiohttp", cors_allowed_origins="*")
app = web.Application()
runner = Runner()
sio.attach(app)


def parse_board(board):
    new_board = [
        [x.value if x.value is not None else 0 for x in row]
        for row in board
    ]

    return new_board


@sio.event
async def make_move(sid, data):
    data = json.loads(data)

    if move_ml is None:
        runner.reset()
    else:
        runner.translator.make_move(move_ml)

    state = runner.translator.get_state()
    reward = runner.translator.get_reward()
    moves = runner.translator.get_moves()
    board = runner.translator.get_board()
    board_raw = runner.game.get_board()

    response_data = {
        "moves_vector": moves,
        "game_board": board,
        "reward": reward,
        "state": state.name,
        "board_raw": parse_board(board_raw)
    }

    print(response_data)

    await sio.emit("get_response", json.dumps(response_data), room=sid)


if __name__ == '__main__':
    web.run_app(app, host="0.0.0.0", port=5002)