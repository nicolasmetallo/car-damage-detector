# Car Damage Detector using Mask R-CNN implementation

```
!pip install -r requirements.txt
```

## Download images
Go to Google Images or Flickr. Choose where it's allowed for commercial and other mod uses. Download at least
100 images. Put all of them in the same folder

## Split dataset
Use 'build_dataset.py' to split into train, val, test folders.
Write in command-line
```
!python3 build_dataset.py --data_dir='images' --output_dir='train_data'
```

## Annotate images
Go to http://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html to annotate the images.
- Here's a demo to see what options to use, http://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html

## Download .h5 coco from Matterport Releases
wget https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5
