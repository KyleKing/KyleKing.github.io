# PiAlarm

## Summary

I wasn't happy with the alarm clock I had or the ones I found online, so I built an alarm clock to fit all the features I could dream up. I wanted to have no option but to wake up, bright lights, loud noises, and tons of smart features. For example, the alarm can be accessed via a web app and when I leave my apartment the alarm is dormant until I return. This way if I leave before my alarm, it won't go off and wake anyone else up.

## Wake up call

While still very much in progress, the alarm clock wakes me up every morning. I'm a heavy sleeper, so I designed the alarm clock around a cycle that increases in intensity through three stages. When the alarm starts, an RGB LED strip is activated that gently increases in brightness. The second stage adds a quiet buzzer and increase the LED strips brightness. The third stage initiates the bed shaker, buzzer, and fades the RGB LED strip at full brightness. At any point, I can press the off button to turn it all off.

The breadboarded LED Strip, buzzer, bed shaker driver, and display:

![TBD](./imgs/PiAlarm/Overview.jpg)

### Web App

I built a simple interface using react that displays the alarms and editable content. The alarms can be toggled on/off, deleted, given a title, or the cron scheduled can be updated. The app uses socket.io on the back-end to control the alarm clock in real time and a complicated Cron-scheduler to keep all the alarms running.

The web app user interface:

![TBD](./imgs/PiAlarm/Webapp.png)

### Others Features

- Using IFTTT, I have a recipe that sends a web request whenever I leave my apartment and whenever I return. This way, the alarm sits dormant when I'm at work to prevent accidentally waking my neighbors.
- Additionally, the alarm sends me a text alert whenever it turns on, so if needed I can turn it off remotely.
- The display shows the temperature, wind speed, and likelihood of rain, for my bike commute to and from work. The data is aggregated over a three hour window for when I usually leave and would return to show both commutes at once.

## Next Steps

As ongoing project, my next step is solder the components onto perf boards to reduce the overall size. I am also waiting on the delivery of a laser cutter and 3D printer to start building a smaller and more permanent housing!
