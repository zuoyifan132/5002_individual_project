"""
Description: Prepare the experimental settings
"""
import torch


def prep_env():
    # type: () -> dict
    """
    Desc:
        Prepare the experimental settings
    Returns:
        The initialized arguments
    """
    settings = {
        "path_to_test_x": "../data/sdwpf_baidukddcup2022_test_toy/test_x",
        "path_to_test_y": "../data/sdwpf_baidukddcup2022_test_toy/test_y",
        "data_path": "../data",
        "filename": "sdwpf_baidukddcup2022_full.csv",
        "task": "MS",
        "target": "Patv",
        "input_len": 144,
        "output_len": 288,
        "out_var": 1,
        "day_len": 144,
        "train_days": 214,
        "val_days": 16,
        "test_days": 15,
        "total_days": 245,

        "start_col": 0,
        "var_len": 5,
        "select": ['weekday', 'time', 'Wspd', 'Etmp', 'Itmp', 'Prtv', 'Patv'],
        "model": "AGCRN",
        "best": 0,
        "exp_id": '79150',
        "checkpoints": "kfold_dtw_5_data_diff",
        "random": False,
        "only_useful": True,
        "dropout": 0,
        "rnn_units": 64,
        "embed_dim": 10,
        "graph_type": "dtw",
        "weight_adj_epsilon": 0.8,
        "cheb_order": 2,
        "num_layers": 2,
        "dtw_topk": 5,
        "weight": 1.0,
        "ind": -1,
        "K": 5,
        "add_apt": True,
        "binary": True,
        "seed": 0,
        "data_diff": False,

        "num_workers": 2,
        "train_epochs": 30,
        "batch_size": 32,
        "patience": 2,
        "lr": 1e-3,
        "lr_adjust": "type1",
        "gpu": 0,
        "capacity": 134,
        "turbine_id": 0,
        "pred_file": "predict.py",
        "framework": "pytorch",
        "is_debug": True,

        # AGCRN model
        "model_list": [
            {
                "start_col": 0,
                "var_len": 6,
                "model": "AGCRN",
                "best": 2,
                "exp_id": '31543',
                "checkpoints_in": "31543_AGCRN",
                "random": False,
                "only_useful": True,
                "dropout": 0,
                "rnn_units": 64,
                "embed_dim": 10,
                "graph_type": "dtw",
                "weight_adj_epsilon": 0.8,
                "ind": 0,
                "weight": 0.321763283,
                "add_apt": True,
                "data_diff": True,
            },
            {
                "start_col": 0,
                "var_len": 6,
                "model": "AGCRN",
                "best": 0,
                "exp_id": '94237',
                "checkpoints_in": "94237_AGCRN",
                "random": False,
                "only_useful": True,
                "dropout": 0,
                "rnn_units": 64,
                "embed_dim": 10,
                "graph_type": "dtw",
                "weight_adj_epsilon": 0.8,
                "ind": 1,
                "weight": 0.495282746,
                "add_apt": True,
                "data_diff": True,
            },
            {
                "start_col": 0,
                "var_len": 6,
                "model": "AGCRN",
                "best": 1,
                "exp_id": '43292',
                "checkpoints_in": "43292_AGCRN",
                "random": False,
                "only_useful": True,
                "dropout": 0,
                "rnn_units": 64,
                "embed_dim": 10,
                "graph_type": "dtw",
                "weight_adj_epsilon": 0.8,
                "ind": 2,
                "weight": 0.3569738,
                "add_apt": True,
                "data_diff": True,
            },
            {
                "start_col": 0,
                "var_len": 6,
                "model": "AGCRN",
                "best": 1,
                "exp_id": '98201',
                "checkpoints_in": "98201_AGCRN",
                "random": False,
                "only_useful": True,
                "dropout": 0,
                "rnn_units": 64,
                "embed_dim": 10,
                "graph_type": "dtw",
                "weight_adj_epsilon": 0.8,
                "ind": 3,
                "weight": 0.298808416,
                "add_apt": True,
                "data_diff": True,
            },
            {
                "start_col": 0,
                "var_len": 6,
                "model": "AGCRN",
                "best": 0,
                "exp_id": '8204',
                "checkpoints_in": "8204_AGCRN",
                "random": False,
                "only_useful": True,
                "dropout": 0,
                "rnn_units": 64,
                "embed_dim": 10,
                "graph_type": "dtw",
                "weight_adj_epsilon": 0.8,
                "ind": 4,
                "weight": 0.408473526,
                "add_apt": True,
                "data_diff": True,
            },
        ],
        # MTGNN model
        "model_list2": [
            {
                "start_col": 0,
                "var_len": 5,
                "model": "MTGNN",
                "best": 0,
                "exp_id": '55237',
                "checkpoints_in": "55237_MTGNN",
                "random": False,
                "only_useful": True,
                "dropout": 0,
                "graph_type": "geo",
                "weight_adj_epsilon": 0.8,
                "ind": -1,
                "weight": 1,
                "add_apt": False,
                "data_diff": False,
            },
        ],
    }
    settings['device'] = torch.device('cuda:0')

    print("The experimental settings are: \n{}".format(str(settings)))
    return settings