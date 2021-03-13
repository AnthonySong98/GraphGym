import torch.nn as nn
from graphgym.init import *

class TestInit:
    def test_init_weights(self):
        m = nn.BatchNorm2d(100)
        init_weights(m)
        assert torch.is_nonzero(m.bias.sum()) == False
        m = nn.BatchNorm2d(100)
        init_weights(m)
        assert torch.is_nonzero(m.bias.sum()) == False
        assert torch.is_nonzero(m.weight.sum() - 100) == False
        m = nn.BatchNorm1d(100)
        init_weights(m)
        assert torch.is_nonzero(m.bias.sum()) == False
        assert torch.is_nonzero(m.weight.sum() - 100) == False
        m = torch.nn.Linear(8, 16, bias=True)
        init_weights(m)
        assert torch.is_nonzero(m.bias.sum()) == False