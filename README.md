# Introduction
This program is made to extract gt.txt files data from the frames processed by detection and tracking algorithm. For this, first the frames collected from detection algorithm are processed from online tool: [LabelMe](http://labelme2.csail.mit.edu/Release3.0/index.php).
Each frames are to be labelled malually.
After labelling is done, the work done are to be downloaded. The downloaded files are in the form of .zip which are to be unzipped. Here, each frame will get its own folder with specific name in ascending order. Each folder of each frame are to be copied in this folder to continue our process.
Now, we have to run test.py file using command:
```bash
python3 test.py
```

If the required libraries are not installed yet, first the packages are to be installed as:
```bash
pip3 install bs4 lxml
```
```bash
pip3 install os
```

Now after running test.py file, we will get our required ground truth file: gt.txt