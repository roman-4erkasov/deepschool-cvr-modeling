import logging
import os

import pandas as pd
from src.dataset_splitter import stratify_shuffle_split_subsets
from sklearn.preprocessing import MultiLabelBinarizer


def split_and_save_datasets(df: pd.DataFrame, save_path: str):
    logging.info(f"Original dataset: {len(df)}")
    mlb = MultiLabelBinarizer()
    mhot = mlb.fit_transform(df.tags.str.split())
    d_mhot = pd.DataFrame(
        mhot,
        columns=mlb.classes_
    )
    df = df.assign(**d_mhot.to_dict("list"))
    df = df.drop_duplicates()
    df = df.drop(["tags"], axis=1)
    logging.info(f"Final dataset: {len(df)}")

    train_df, valid_df, test_df = stratify_shuffle_split_subsets(
        df,
        img_path_column="image_name",
        train_fraction=0.8,
        verbose=True,
    )
    logging.info(f"Train dataset: {len(train_df)}")
    logging.info(f"Valid dataset: {len(valid_df)}")
    logging.info(f"Test dataset: {len(test_df)}")

    train_df.to_csv(os.path.join(save_path, "train_df.csv"), index=False)
    valid_df.to_csv(os.path.join(save_path, "valid_df.csv"), index=False)
    test_df.to_csv(os.path.join(save_path, "test_df.csv"), index=False)
    logging.info("Datasets successfully saved!")


if __name__ == "__main__":
    save_path = os.path.dirname(
        os.environ.get("ROOT_PATH")
    )
    logging.basicConfig(level=logging.INFO)
    # df = pd.read_csv(os.path.join(os.path.join(os.environ.get("ROOT_PATH")), "train.csv"))
    df = pd.read_csv(os.environ.get("ROOT_PATH"))
    split_and_save_datasets(df, save_path)

