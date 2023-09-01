# Raspberry Pi PhotoFrame

## Summary

A Raspberry Pi powered smart photo frame using Balloon.io + Dropbox + Javascript + Frame Buffer ImageViewer (FBI). The Raspberry Pi is running a Node application that fetches the latest images from Dropbox and displays the images using FBI. Through Balloon.io, anyone with the password can upload photos to the pre-designated Dropbox folder, which will be synced and displayed on the photo frame. The frame was a Christmas gift to my girlfriend that I've continued to improve and update.

![TBD](./imgs/PhotoFrame/cover.jpg)

![TBD](./imgs/PhotoFrame/cover_alt.jpg)

## How it works

Balloon.io allows you to setup a website where anyone can upload images that are placed into the Apps folder of the linked Dropbox account, which works on mobile and desktop. The app pulls all images from the set Dropbox folder and loads them locally. Once completely downloaded, the FBI task is started to update the image at short time intervals. There is additional logic to handle stopping and starting the FBI task to keep the display always up to date as new photos are downloaded and added to the cycle. The displays goes to sleep at various intervals so the displays is only on during the weekends and weekdays after work.

## The hardware

I modified an IKEA frame to hold a small TFT display with space for airflow and mounting point for the Raspberry Pi and driver board. I stacked a piece of thick white paper for a crisp edge around the display then three pieces of laser cut acrylic. The first piece holds the display, the second provides space for the ribbon cable, and the third has air holes for circulation and is the surface that the boards are mounted to with standoffs

![TBD](./imgs/PhotoFrame/lc_base_layer.jpg)

![TBD](./imgs/PhotoFrame/stacked_lc_acrylic.jpg)

Three 3D printed feet hold everything sandwiched in place along with the original stand for support. Just on the inside surface of the stand is a small perf board with an indicator LED and pushbutton to cleanly power down the Raspberry Pi when needed.

![TBD](./imgs/PhotoFrame/3D_printed_feet.jpg)

![TBD](./imgs/PhotoFrame/the_guts.jpg)
