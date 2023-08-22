# luxonis_oakd_examples
List of own oakd test and examples

## Installation
Install requirements:

```bash
pip3 install -r requirements.txt
```

## Examples
*   **save_rgb_images.py** -> Example of image RGB preview and how to save images in a folder. It is useful to dataset collection.


## Generating the .blob file using [tools.luxonis.com](http://tools.luxonis.com)
After the training and validation, you can convert the fine-tuned PyTorch model to a `.blob` format.

Please follow these steps to do so:
1.   Download the fine-tuned weights from `runs/train/exp/weights/yolov8ntrained.pt` to your device (as shown in screenshot below)
2.   Go to the page [tools.luxonis.com](http://tools.luxonis.com)
3.   On the page set Yolo Version to `YoloV8 (detection only)` ( (as shown in the screeenshot below)
4.   On the page set File to the downloaded `yolov8ntrained` weights (as shown in the screeenshot below)
5.   On the page set Input shape to `640` (as shown in the screeenshot below)