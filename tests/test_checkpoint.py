from graphgym.checkpoint import *

class TestCheckpoint:
    def test_get_ckpt_dir(self):
        ckpt_dir = get_ckpt_dir()
        assert "results/ckpt" == ckpt_dir

    def test_get_all_epoch(self):
        epochs = get_all_epoch()
        assert epochs == [0]