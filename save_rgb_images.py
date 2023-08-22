import datetime
import os
import cv2
import depthai as dai

# output folders
out_folder = 'images'

# if output folder does not exist, create it
if not os.path.exists(out_folder):
    os.makedirs(out_folder)

# Create pipeline
pipeline = dai.Pipeline()

# Define source and output
camRgb = pipeline.create(dai.node.ColorCamera)
xoutRgb = pipeline.create(dai.node.XLinkOut)

xoutRgb.setStreamName("rgb")

# Properties
camRgb.setPreviewSize(1080, 720)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

# Linking
camRgb.preview.link(xoutRgb.input)

# Connect to device and start pipeline
with dai.Device(pipeline, usb2Mode=True) as device:

    print('Connected cameras:', device.getConnectedCameraFeatures())
    # Print out usb speed
    print('Usb speed:', device.getUsbSpeed().name)
    # Bootloader version
    if device.getBootloaderVersion() is not None:
        print('Bootloader version:', device.getBootloaderVersion())
    # Device name
    print('Device name:', device.getDeviceName())

    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)

    while True:
        inRgb = qRgb.get()  # blocking call, will wait until a new data has arrived

        image = inRgb.getCvFrame()

        # Retrieve 'bgr' (opencv format) frame
        cv2.imshow("rgb", image)

        # get key pressed
        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        elif key == ord('s'):
            # save image in png with datetime as filename
            cv2.imwrite(os.path.join(out_folder, datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.png'), image)