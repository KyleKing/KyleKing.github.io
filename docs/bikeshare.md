# Stationless Bikeshare

## Summary

In the University of Maryland Gemstone Research Program, I worked with 12 students to prototype a stationless bikeshare. The bikeshare is a combination of a wireless Zigbee communication system, smart lock, and related technology that allows users to flexibly rent and return bikes anywhere on campus. I served in many roles to help shape the design of the project, but primarily lead the development of the web application and wireless access point.

In April 2016 we presented our thesis and have since released our [complete thesis document](https://www.gitbook.com/book/kyleking/gemstone-team-bikes-2016-thesis/details) along with the [annotated source code](https://github.com/KyleKing/TeamBIKES) behind our project.

Our team:

![TBD](./imgs/Bikeshare/bikeshare-06.jpg)

## Stationless Bikeshare

Bikeshares allow users to access a fleet of bikes spread throughout an urban area. They promote healthy lifestyles and sustainability among commuters, casual riders, and tourists. However, the central pillar of modern systems, the bike station, cannot be easily integrated into a compact college campus. Fixed stations lack the flexibility to meet the needs of college students who make quick, short-distance trips. Additionally, the necessary cost of implementing and maintaining each station prohibits increasing the number of stations for user convenience. Therefore, the team developed a stationless bikeshare based on a smartlock permanently attached to bicycles in the system. The smartlock system design incorporates several innovative approaches to provide usability, security, and reliability that overcome the limitations of a station centered design. A focus group discussion allowed the team to receive feedback on the early lock, system, and website designs, identify improvements and craft a pleasant user experience. The team designed a unique, two-step lock system that is intuitive to operate while mitigating user error. To ensure security, user access is limited through near field communications (NFC) technology connected to a mechatronic release system. The said system relied on a NFC module and a servo working through an Arduino microcontroller coded in the Arduino IDE. To track rentals and maintain the system, each bike is fitted with an XBee module to communicate with a scalable ZigBee mesh network. The network allows for bidirectional, real-time communication with a Meteor.js web application, which enables user and administrator functions through an intuitive user interface available on mobile and desktop. The development of an independent smartlock to replace bike stations is essential to meet the needs of the modern college student. With the goal of creating a bikeshare that better serves college students, Team BIKES has laid the framework for a system that is affordable, easily adaptable, and implementable on any university expressing an interest in bringing a bikeshare to its campus.

RedBar Bikes Commercial (Click to Watch on Youtube):

[![Commerical](./imgs/Bikeshare/RedBarBikesCommercial.png)](https://www.youtube.com/watch?v=tg4aXH1SqxQ)

## The Technology

To use our system, a user can load our website's campus map and tap any available bike icon to instantly reserve the bike. The reservation guarantees the user a bike at the rack they selected, but they can simply pick up any bike that they see. Once they arrive at a bike, the user taps their RedBars NFC card, which sends an encrypted request through our distributed ZigBee mesh network, to the nearest wireless access point, and to the website backend for confirmation. When approved the mechatronic lock releases the rental pin. The user rotates the lock into riding position and is free to go to any where they would like.

![TBD](./imgs/Bikeshare/Mesh_Single.png)

Each individual bike has an Arduino/Xbee unit, which communicates with the distributed XBee routers, that send information back to a centralized wireless access point, a Raspberry Pi "coordinator"

Network Diagram: With the additional of a few coordinators, the system can quickly expand:

![TBD](./imgs/Bikeshare/Mesh_System.png)

The bike lock was designed to be locked only to proper bike hoops, the standard bike rack on campus. The lock sits on the seat post and although not shown, is now designed to be rotated away from the bike to lock. There is additionally a pin inside the lock box that immobilizes one of the cuffs. Through paper sketching, CAD design, and 3D printed parts, we've been able to gain rapid feedback on the design and make many iterations.

Our Smart Lock Concept:

![TBD](./imgs/Bikeshare/Lock_and_Electronics.png)

The final functional prototype:

![TBD](./imgs/Bikeshare/cover.jpg)

Animation depicting the lock actuation aspects:

![TBD](./imgs/Bikeshare/LockAnimation.gif)

Actual lock prototype in use:

![TBD](./imgs/Bikeshare/LockInUse.gif)

## The Website

I put together the coordinator and website. The coordinator connected to the ZigBee network then relayed information back and forth to the remote database to determine if access should be allowed or denied. The information would then be distributed throughout the network in real time.

Authentication Demonstration (1/8 speed):

![TBD](./imgs/Bikeshare/Access.gif)

I didn't start as the team's web developer. I built my first website in December of 2013 with static HTML and CSS files. A few months later, I began teaching myself more advanced website development with the goal of solving one of our leading issues, inventory management and system coordination. I researched many different frameworks, such as Node/MEAN, Firebase, Native iOS, and more, but selected Meteor for its cross-platform support, optimistic user interface, and growing package library. I was equally excited to be part of a up and coming platform and contribute to a growing community.

### Iterate over user feedback

We ran a focus group midway through our development to receive feedback on our business model, website, and lock design. We received feedback on all aspects of our project that helped guide our development. This focus group and the constant feedback from friends, coworkers, and classmates have helped push through three major user interface overhauls, prioritize feature requests, and reduce bloat.

From all the feedback, several new features emerged to meet user needs. One such feature was for bike reservations that would guarantee a bike's position when a user was leaving class. Extending the real time map, I designed a simple user experience that any available bike icon could be tapped to request a reservation. Adding a cron task, the reservation can thus be timed out reliably freeing up a bike if the user decides against renting.

### Website Screen Shots

Interactive Website Map:

![TBD](./imgs/Bikeshare/WS_map.png)

An example user profile:

![TBD](./imgs/Bikeshare/WS_user.png)

The archived about page:

![TBD](./imgs/Bikeshare/WS_about.png)
