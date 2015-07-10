# About pushthebuttond

## My story

There's a lot of information online which I need to get at regularly in my job. And so I use _pushbuttond_ running on a Raspberry Pi to quickly flip between information dashboards on a spare monitor at my desk.

If I quickly need to see the BBC Bitesize Kanban board ... I push the button.

If I then need to see the shaping board, or our audience stats, or our list of bugs (shh!) ... I push, push, push the button.

I'd love to hear what you use _pushthebuttond_ for, so please get in touch with me. I'm [@alicraigmile](https://twitter.com/alicraigmile) on twitter too.

Cheers,
Ali

## Setting up the hardware

### The button

Connect one side of a button to 3.3v, and the other to ground (via a 10Kohm resistor). Next connext the -ve side to GPIO17 (via a 1Kohm resistor).

### The LED

Connect the anode of an LED (+ve end) to GPIO4 and the other end to ground (via a 60ohm resistor).

### Testing the hardware

When you've installed everything (see below), run the script called [blink](bin/blink) to test the LED.

## Installing

```
git clone https://github.com/alicraigmile/pushthebuttond.git
cd pushthebuttond
sudo ./install.sh 
```

## Starting the daemon

```
sudo service pushthebuttond start
```

## Stopping the daemon

```
sudo service pushthebuttond stop
```

## Checking if the service is running

```
service pushthebuttond status
```

## Operating instructions

When the service is running, pushing the button will cause the job (default: loop-dashboards) to run.

When a job is running the LED will light. 

When it completes, the LED will flash twice.

That's about it! 

## Changing the job which runs

You'll need to edit the [sbin/pushthebuttond] script to change the job which runs. I've supplied a couple of options:

* [loop-dashboards](bin/loop-dashboards) - launch chromium browser in kiosk mode. A push of the button loops through a series of web addresses specified in the script (default)
* [speak-the-time]([bin/speak-the-time)-- um, it tells you the time.  
* [launch-xeyes](bin/launch-xeyes) - each push of the button adds a new set of eyes to follow you around the room

## Custom jobs## Custom jobs

Write a shell script of your own, and as long as it's somewhere sensible (e.g. /usr/local/bin) then _pushthebuttond_ will be able to find it and run it.

_pushthebuttond_ could:

* Play you some music
* Tweet something
* Save a bookmark for you
* Take a photo from an attached webcam
* Tell your CI environment to start a build or deploy your website

What would you have it do? 
