#  Multi Label Classification (hw01)

## System Requirements
|System  |Required                                   |
|:------:|:-----------------------------------------:|
|OS      |Ubuntu 22.04.1 LTS (Jammy Jellyfish)       |
|Python  |Python 3.8.16                              |
|make    |Must be installed, part of build-essentials|

## Get Started
1. Get dataset "Multi_Label_dataset" from ![Kaggle](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/overview) and put it in some folder, for example "/home/$USER/data".
2. Install software using the command `make install`
3. Download weights using the command `make download_weights`
4. Run the following command using ROOT_PATH as path to folder with the dataset:
```bash
ROOT_PATH=/home/$USER/data/Multi_Label_dataset venv/bin/python split_dataset.py &> split.log
```
