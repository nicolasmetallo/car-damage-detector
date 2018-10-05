"""Split an image folder into train/val/test sets and resize.
- The images dataset comes in the following format:
    images/
        IMG_00000.jpg
        ...
- Resizing reduces the dataset size and loading smaller images makes training faster.
- Modified from: https://cs230-stanford.github.io/train-dev-test-split.html
"""

import argparse
import random
import os

from PIL import Image
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', default='images', help="Directory with your dataset")
parser.add_argument('--output_dir', default='output', help="Where to write the new data")
parser.add_argument('--resize', default=(1024,1024), help="Resize to (width,height)")

args = parser.parse_args()
SIZE = args.resize

def resize_and_save(filename, output_dir, size=SIZE):
    """Resize the image contained in `filename` and save it to the `output_dir`"""
    image = Image.open(filename)
    # Use bilinear interpolation instead of the default "nearest neighbor" method
    image = image.resize((size), Image.BILINEAR)
    image.save(os.path.join(output_dir, filename.split('/')[-1]))


if __name__ == '__main__':
    assert os.path.isdir(args.data_dir), "Couldn't find the dataset at {}".format(args.data_dir)

    # Define the data directories
    images_dir = args.data_dir

    # Get the filenames in each directory (train and test)
    filenames = os.listdir(images_dir)
    filenames = [os.path.join(images_dir, f) for f in filenames if f.endswith('.jpg')]

    # Split the images in the 'images' dir into 80% train, 10% val, and 10% test
    # Make sure to always shuffle with a fixed seed so that the split is reproducible
    random.seed(230)
    filenames.sort()
    random.shuffle(filenames)

    split_a = int(0.8 * len(filenames))
    split_b = int(0.9 * len(filenames))
    train_filenames = filenames[:split_a]
    val_filenames = filenames[split_a:split_b]
    test_filenames = filenames[split_b:]

    filenames = {'train': train_filenames,
                 'val': val_filenames,
                 'test': test_filenames}

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
    else:
        print("Warning: output dir {} already exists".format(args.output_dir))

    # Preprocess train, val and test
    for split in ['train', 'val', 'test']:
        output_dir_split = os.path.join(args.output_dir, '{}'.format(split))
        if not os.path.exists(output_dir_split):
            os.mkdir(output_dir_split)
        else:
            print("Warning: dir {} already exists".format(output_dir_split))

        print("Processing {} data, saving preprocessed data to {}".format(split, output_dir_split))
        for filename in tqdm(filenames[split]):
            resize_and_save(filename, output_dir_split, size=SIZE)

    print("Done building dataset")
