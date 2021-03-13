import copy
import deepsnap
import torch.nn as nn
from graphgym.loader import *
from graphgym.config import *

class TestLoader:
    def test_load_dataset(self):
        set_cfg(cfg)
        cfg.dataset.name = 'Cora'
        cfg.dataset.format = 'PyG'
        graphs = load_dataset()
        assert len(graphs) > 0
        assert isinstance(graphs[0], deepsnap.graph.Graph)

    def test_load_pyg(self):
        set_cfg(cfg)
        graphs = load_pyg(name="Karate",dataset_dir=cfg.dataset.dir)
        assert len(graphs) > 0
        assert isinstance(graphs[0], deepsnap.graph.Graph)

    def test_load_nx(self):
        set_cfg(cfg)
        # TODO: add unit test for load nx graph.
        pass

    def test_filter_graphs(self):
        set_cfg(cfg)
        assert filter_graphs() == 5
        cfg.dataset.task = 'graph'
        assert filter_graphs() == 0

    def test_transform_before_split(self):
        set_cfg(cfg)
        dataset = GraphDataset(
        graphs = load_dataset() ,
        task=cfg.dataset.task,
        edge_train_mode=cfg.dataset.edge_train_mode,
        edge_message_ratio=cfg.dataset.edge_message_ratio,
        edge_negative_sampling_ratio=cfg.dataset.edge_negative_sampling_ratio,
        minimum_node_per_graph=5)
        transform_before_split(dataset)
        assert cfg.dataset.augment_feature_dims  == []

    # def test_transform_after_split(self):
    #     set_cfg(cfg)
    #     cfg.dataset.edge_train_mode = 'all'
    #     cfg.dataset.transform = 'edge'
    #     dataset = GraphDataset(
    #     graphs = load_dataset() ,
    #     task=cfg.dataset.task,
    #     edge_train_mode=cfg.dataset.edge_train_mode,
    #     edge_message_ratio=cfg.dataset.edge_message_ratio,
    #     edge_negative_sampling_ratio=cfg.dataset.edge_negative_sampling_ratio,
    #     minimum_node_per_graph=5)
    #     original_dataset = copy.deepcopy(dataset)
    #     dataset = transform_after_split(dataset)
    #     assert original_dataset.graphs[0] == dataset.graphs[0]

    def test_create_dataset(self):
        set_cfg(cfg)
        create_dataset()

    def test_create_loader(self):
        set_cfg(cfg)
        datasets = create_dataset()
        create_loader(datasets)