import os
import fastwer
import argparse
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "gt_file",
        type=str,
        default="Assignment_2/gt.xlsx",
        nargs="?",
        help="Ground truth file",
        metavar="ARG1",
    )
    parser.add_argument(
        "pred_file",
        type=str,
        default="Assignment_2/pred.xlsx",
        nargs="?",
        help="Prediction file",
        metavar="ARG2",
    )
    args = parser.parse_args()

    # Read input files
    gt_df = pd.read_excel(args.gt_file)
    pred_df = pd.read_excel(args.pred_file)

    # Calculate accuracy using fastwer
    acc = 100 - fastwer.score(pred_df["PRED"], gt_df["GT"], char_level=True)
    num_lines = len(gt_df["GT"])
    num_chars = len("".join([line for line in gt_df["GT"]]))
    print(f"Accuracy = {acc}")
    print(f"Number of lines in GT column = {num_lines}")
    print(f"Number of characters in GT column = {num_chars}")
    stats_dict = {
        "Accuracy": [acc],
        "Num_lines": [num_lines],
        "Num_characters": [num_chars],
    }
    # Create DataFrame and dump to disk
    stats_df = pd.DataFrame(stats_dict)
    stats_df.to_excel("output.xlsx", index=False)
