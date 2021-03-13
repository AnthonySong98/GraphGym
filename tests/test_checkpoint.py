from graphgym.checkpoint import *

class TestCheckpoint:
    def test_get_ckpt_dir(self):
        ckpt_dir = get_ckpt_dir()
        assert ckpt_dir == "results/ckpt"

    def test_get_all_epoch(self):
        epochs = get_all_epoch()
        assert epochs == [0]

    def test_get_last_epoch(self):
        assert get_last_epoch() == 0

    def test_clean_ckpt(self):
        assert clean_ckpt() == None