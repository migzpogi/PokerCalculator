from flask import Flask, request, jsonify
from PokerCalcMain import calculate_deuces, compute_win_percentage

app = Flask(__name__)

@app.route("/poker")
def hello():
    board = request.args.get('board')
    hand = request.args.get('hand')

    b = split_board(board)
    h = split_hand(hand)

    d = calculate_deuces(b,h)
    d_score = d[0]
    d_class = d[1]

    win = compute_win_percentage(b, h)

    return jsonify(
        {'score': d_score},
        {'class': d_class},
        {'win_percent': win}
    )


def split_board(board_args):
    """
    Splits the board args
    :param board_args:
    :return:
    """

    board = []

    card_1 = board_args[0:2]
    board.append(card_1)
    card_2 = board_args[2:4]
    board.append(card_2)
    card_3 = board_args[4:6]
    board.append(card_3)

    card_4 = board_args[6:8]


    if card_4 is not "":
        board.append(card_4)

    card_5 = board_args[8:10]

    if card_5 is not "":
        board.append(card_5)

    return board


def split_hand(hand_args):
    """

    :param hand_args:
    :return:
    """

    hand = []

    card_1 = hand_args[0:2]
    hand.append(card_1)
    card_2 = hand_args[2:4]
    hand.append(card_2)

    return hand


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    # app.run()