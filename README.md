# Deepstream IGN Maker YOLO
 Nvidia Deepstream YOLO Python App

Here is the code and the Python apps I used to Run the Nvidia Deepstream YOLO Object detector app.

The Ignition maker app for ignition designer is also included in this Repo incase you want to import it into Ignition designer.

This Repo also contains sparkplug stuff and Deepstream YOLO Config files.

If you clone this Repo and install it on youre Nano or Xavier NX at this location.

/opt/nvidia/deepstream/deepstream-5.0/sources/deepstream_python_apps/apps

It should be able to run out of that folder.


# 1. python3 deepstream_ignition_IP_File_yolo.py

Will run a I.P. camera or a MP4 file and display the Video stream on youre XavierNX or nano 

and also send metadata via sparkplug to the Ignition Maker app.

I.P. Example:python3 deepstream_ignition_IP_File_yolo.py 'rtsp://172.16.2.157:554/user=admin&password=&channel=1&stream=0.sdp?'

MP4 file example:python3 deepstream_ignition_IP_File_yolo.py file:////opt/nvidia/deepstream/deepstream=5.0/samples/streams/video.mp4


# 2. python3 deepstream_ignition_usb_yolo.py

Will run a webcam and display the Video stream on youre XavierNX or nano

and also send metadata via sparkplug to the Ignition Maker app.

webcam example:python3 deepstream_ignition_usb_yolo.py /dev/video0


# 3. python3 deepstream_ignition_IP_File_rtsp_yolo.py

Will run a I.P. camera or a MP4 file and and stream out a RTSP stream 

and also send metadata via sparkplug to the Ignition Maker app.

I.P. Example:python3 deepstream_ignition_IP_File_rtsp_yolo.py 'rtsp://172.16.2.157:554/user=admin&password=&channel=1&stream=0.sdp?'

MP4 file example:python3 deepstream_ignition_IP_File_rtsp_yolo.py file:////opt/nvidia/deepstream/deepstream=5.0/samples/streams/video.mp4 



# 4. python3 deepstream_ignition_usb_rtsp_yolo.py

Will run a webcam and and and stream out a RTSP stream

and also send metadata via sparkplug to the Ignition Maker app.

webcam example:python3 deepstream_ignition_usb_rtsp_yolo.py /dev/video0


# 5. nx_2021-01-29_1525
Is the ignition maker app you can import into ignition designer












