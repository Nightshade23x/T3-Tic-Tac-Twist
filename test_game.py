import unittest
from unittest.mock import MagicMock, patch
import state
import game_logic
import chaos


class TestT3Logic(unittest.TestCase):

    def setUp(self):
        """Reset global state & mock UI before each test."""
        state.init_state()

        # --------------------------
        # Mock UI labels
        # --------------------------
        state.bank_x_label = MagicMock()
        state.bank_o_label = MagicMock()
        state.score_label = MagicMock()
        state.turn_label = MagicMock()

        state.bank_x_label.config = MagicMock()
        state.bank_o_label.config = MagicMock()
        state.score_label.config = MagicMock()
        state.turn_label.config = MagicMock()

        # --------------------------
        # Mock buttons (3x3)
        # --------------------------
        state.buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
        for row in state.buttons:
            for btn in row:
                btn.config = MagicMock()

        # --------------------------
        # Mock messageboxes
        # --------------------------
        self.info_patcher = patch("tkinter.messagebox.showinfo", return_value=None)
        self.ask_patcher = patch("tkinter.messagebox.askquestion", return_value="no")
        self.yesno_patcher = patch("tkinter.messagebox.askyesno", return_value=False)

        # --------------------------
        # Mock ask_question ALWAYS successful
        # --------------------------
        self.ask_question_patcher = patch("game_logic.ask_question", return_value=True)

        self.info_patcher.start()
        self.ask_patcher.start()
        self.yesno_patcher.start()
        self.ask_question_patcher.start()

    def tearDown(self):
        self.info_patcher.stop()
        self.ask_patcher.stop()
        self.yesno_patcher.stop()
        self.ask_question_patcher.stop()

    # =========================================================
    # SHUFFLE TESTS
    # =========================================================

    def test_shuffle_preserves_marker_counts(self):
        state.board = [
            ["X", " ", "O"],
            ["X", "O", " "],
            [" ", " ", "X"]
        ]

        before_X = sum(cell == "X" for row in state.board for cell in row)
        before_O = sum(cell == "O" for row in state.board for cell in row)

        chaos.shuffle_both_players()

        after_X = sum(cell == "X" for row in state.board for cell in row)
        after_O = sum(cell == "O" for row in state.board for cell in row)

        self.assertEqual(before_X, after_X)
        self.assertEqual(before_O, after_O)

    def test_shuffle_no_auto_win(self):
        state.board = [
            ["X", "X", " "],
            ["O", "O", " "],
            [" ", " ", "X"]
        ]

        chaos.shuffle_both_players()

        self.assertFalse(game_logic.check_winner("X"))
        self.assertFalse(game_logic.check_winner("O"))

    def test_shuffle_only_once_per_turn(self):
        state.shuffled_this_turn = False
        chaos.shuffle_both_players()
        chaos.shuffle_both_players()  # should do nothing
        self.assertTrue(state.shuffled_this_turn)

    # =========================================================
    # BANKING LOGIC TESTS
    # =========================================================

    @patch("chaos.shuffle_both_players")
    def test_banking_sets_flag(self, mock_shuffle):
        """Player chooses to bank → bank_X or bank_O becomes 1."""
        with patch("tkinter.messagebox.askquestion", return_value="yes"):
            game_logic.make_move(0, 0)

        self.assertEqual(state.bank_X, 1)

    @patch("chaos.shuffle_both_players")
    def test_using_banked_move_places_two_markers(self, mock_shuffle):
        state.bank_X = 1

        # First click (enter bank mode)
        with patch("tkinter.messagebox.askquestion", return_value="yes"):
            game_logic.make_move(0, 0)

        # Second click via overridden button command
        second_click = state.buttons[0][1].config.call_args[1]["command"]
        second_click()  # call second_click

        marker_count = sum(cell == "X" for row in state.board for cell in row)
        self.assertEqual(marker_count, 2)

    @patch("chaos.shuffle_both_players")
    def test_bank_resets_after_use(self, mock_shuffle):
        state.bank_X = 1

        # First move uses bank
        with patch("tkinter.messagebox.askquestion", return_value="yes"):
            game_logic.make_move(0, 0)

        # Simulate second-click
        second_click = state.buttons[0][1].config.call_args[1]["command"]
        second_click()

        self.assertEqual(state.bank_X, 0)

    # =========================================================
    # RESET TESTS
    # =========================================================

    def test_reset_board_clears_everything(self):
        state.board = [
            ["X", "O", "O"],
            ["X", "X", " "],
            [" ", "O", " "]
        ]

        state.bank_X = 1
        state.bank_O = 1

        game_logic.reset_board("X")

        self.assertTrue(all(
            state.board[i][j] == " "
            for i in range(3) for j in range(3)
        ))

        self.assertEqual(state.bank_X, 0)
        self.assertEqual(state.bank_O, 0)
        self.assertEqual(state.player, "X")


if __name__ == "__main__":
    unittest.main()
