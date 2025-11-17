import unittest
from unittest.mock import patch, MagicMock
import T3   # your main game file

class TestBankingLogic(unittest.TestCase):

    def setUp(self):
    # Reset game state
        T3.board = [[" " for _ in range(3)] for _ in range(3)]
        T3.bank_X = 0
        T3.bank_O = 0
        T3.player = "X"
        T3.shuffled_this_turn = False
        T3.using_bank = False

        # Fake GUI elements so config() calls don't error
        T3.label = MagicMock()
        T3.bank_x_label = MagicMock()
        T3.bank_o_label = MagicMock()
        T3.score_label = MagicMock()

        # Fake buttons grid
        T3.buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]


    # ------------------------------------------------------
    # 1. TEST: Banking should NOT place a marker
    # ------------------------------------------------------
    @patch("T3.ask_question", return_value=True)  # correct answer
    @patch("T3.messagebox.askquestion", return_value="yes")  # choose to bank
    @patch("T3.messagebox.showinfo")
    def test_banking_does_not_place_marker(self, m_info, m_ask, m_q):

        T3.make_move(0, 0)

        self.assertEqual(
            T3.board[0][0], " ",
            "Banking incorrectly placed the marker."
        )

        self.assertEqual(
            T3.bank_X, 1,
            "Bank did NOT store correctly for X."
        )

    # ------------------------------------------------------
    # 2. TEST: Banking switches the turn
    # ------------------------------------------------------
    @patch("T3.ask_question", return_value=True)
    @patch("T3.messagebox.askquestion", return_value="yes")
    @patch("T3.messagebox.showinfo")
    def test_banking_switches_turn(self, m_info, m_ask, m_q):

        T3.make_move(1, 1)

        self.assertEqual(
            T3.player, "O",
            "Turn did not switch after banking."
        )

    # ------------------------------------------------------
    # 3. TEST: NOT banking should place a marker
    # ------------------------------------------------------
    @patch("T3.ask_question", return_value=True)
    @patch("T3.messagebox.askquestion", return_value="no")
    @patch("T3.messagebox.showinfo")
    def test_normal_move_places_marker(self, m_info, m_ask, m_q):

        T3.make_move(0, 0)

        self.assertEqual(
            T3.board[0][0], "X",
            "Normal move failed to place marker."
        )

    # ------------------------------------------------------
    # 4. TEST: Using a bank creates TWO markers
    # ------------------------------------------------------
    @patch("T3.relocate_if_conflict")
    @patch("T3.shuffle_both_players")
    @patch("T3.messagebox.showinfo")
    def test_bank_usage_two_markers(self, m_info, m_shuffle, m_relocate):

        # Give X a bank manually
        T3.bank_X = 1
        T3.player = "X"

        with patch("T3.ask_question", return_value=True):
            with patch("T3.messagebox.askquestion", side_effect=["yes"]):

                # We'll intercept the second-click callback
                second_click_holder = {}

                # Fake override of config to capture callbacks
                def fake_config(command=None, **kwargs):
                    if callable(command):
                        second_click_holder['cb'] = command

                # mock buttons so config captures second-click assignment
                T3.buttons = [[MagicMock() for _ in range(3)] for _ in range(3)]
                for row in T3.buttons:
                    for btn in row:
                        btn.config = fake_config

                # first placement happens here
                T3.make_move(0, 0)

                # Ensure second click was registered
                self.assertIn('cb', second_click_holder,
                            "Second-click handler was never set during bank usage.")

                # simulate second click
                second_click_holder['cb'](1, 1)

        # NOW we must have 2 markers
        total_x = sum(cell == "X" for row in T3.board for cell in row)

        self.assertEqual(
            total_x, 2,
            "Banking failed to place two markers on the board."
        )


    # ------------------------------------------------------
    # 5. TEST: No marker lost during banking
    # ------------------------------------------------------
    @patch("T3.relocate_if_conflict")
    @patch("T3.shuffle_both_players")
    @patch("T3.messagebox.showinfo")
    def test_no_marker_lost_during_bank(self, m_info, m_shuffle, m_relocate):

        T3.board = [
            ["X", " ", "O"],
            [" ", "X", " "],
            ["O", " ", " "]
        ]

        T3.bank_X = 1
        T3.player = "X"

        board_before = [row[:] for row in T3.board]

        with patch("T3.ask_question", return_value=True):
            with patch("T3.messagebox.askquestion", side_effect=["yes"]):
                with patch("T3.restore_main_commands"):
                    T3.make_move(0, 1)

        before_O = sum(cell == "O" for row in board_before for cell in row)
        after_O = sum(cell == "O" for row in T3.board for cell in row)

        self.assertEqual(
            before_O, after_O,
            "Opponent marker disappeared during banking!"
        )


if __name__ == "__main__":
    unittest.main()
