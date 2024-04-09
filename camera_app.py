import streamlit as st
from PIL import Image
from ultralytics import YOLO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
st.set_page_config(
    page_title="CAMERA APP",
    page_icon="",
)
st.write("# CHOOSE IMAGE")
model=YOLO('best2.pt')
source = 'ruthvik.jpg'
a=model.predict(source, save=True, imgsz=320, conf=0.5)
st.write(a[0].keypoints.xy[0])
b=float(a[0].keypoints.xy[0][1][0])
c=float(a[0].keypoints.xy[0][1][1])
d=float(a[0].keypoints.xy[0][2][0])
e=float(a[0].keypoints.xy[0][2][1])
f=float(a[0].keypoints.xy[0][3][0])
g=float(a[0].keypoints.xy[0][3][1])
h=float(a[0].keypoints.xy[0][4][0])
i=float(a[0].keypoints.xy[0][4][1])
b=((b-d)**2)+((c-e)**2)
b=(b)**(1/2)
st.write(b)
f=((f-h)**2)+((g-i)**2)
f=(f)**(1/2)
st.write(f)
c=float(a[0].boxes.xywh[0][3])
st.write(c)
d=float(st.number_input("Enter the height in cm : "))
e=(d/c)*b
i=(d/c)*(f)
st.write(e+3)
st.write(i)
j=0
if(j==0):
    st.write("For Peter England : ")
    if(e<=41.4):
        st.write("Size is SMALL")
    elif(e>41.4 and e<=43.2):
        st.write("Size is MEDIUM")
    elif(e>43.2 and e<=45.2):
        st.write("Size is LARGE")
    elif(e>45.2 and e<=47.2):
        st.write("Size is  EXTRA LARGE")
    else:
        st.write("Size is EXTRA EXTRA LARGE")
    j=j+1
if(j==1):
    st.write("For Louis Philippe : ")
    if(e<=44.45):
        st.write("Size is SMALL")
    elif(e>44.45 and e<=45.72):
        st.write("Size is MEDIUM")
    elif(e>45.72 and e<=46.99):
        st.write("Size is LARGE")
    elif(e>46.99 and e<=48.26):
        st.write("Size is  EXTRA LARGE")
    else:
        st.write("Size is EXTRA EXTRA LARGE")
    j=j+1
if(j==2):
    st.write("For Raymonds : ")
    if(e<=40):
        st.write("Size is SMALL")
    elif(e>40 and e<=42):
        st.write("Size is MEDIUM")
    elif(e>42 and e<=44):
        st.write("Size is LARGE")
    elif(e>44 and e<=46):
        st.write("Size is  EXTRA LARGE")
    else:
        st.write("Size is EXTRA EXTRA LARGE")
    j=j+1
if(j==3):   
    st.write("For Teamspirit : ")
    if(e<=36):
        st.write("Size is SMALL")
    elif(e>36 and e<=38):
        st.write("Size is MEDIUM")
    elif(e>38 and e<=40):
        st.write("Size is LARGE")
    elif(e>40 and e<=42):
        st.write("Size is  EXTRA LARGE")
    else:
        st.write("Size is EXTRA EXTRA LARGE")
    j=j+1
if(j==4):
    st.write("For Denims : ")
    if(e<=38):
        st.write("Size is SMALL")
    elif(e>38 and e<=41):
        st.write("Size is MEDIUM")
    elif(e>41 and e<=44):
        st.write("Size is LARGE")
    elif(e>44 and e<=47):
        st.write("Size is  EXTRA LARGE")
    else:
        st.write("Size is EXTRA EXTRA LARGE")
    j=j+1
    





