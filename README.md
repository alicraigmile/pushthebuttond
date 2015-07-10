# About pushthebuttond

(c) 2015 British Broadcasting Corporation. #pushthebutton code and hardware by @alicraigmile.

## Setting up the hardware

### The button

Connect one side of a button to 3.3v, and the other to ground (via a 10Kohm resistor). Next connext the -ve side to GPIO17 (via a 1Kohm resistor).

### The LED

Connect the anode of an LED (+ve end) to GPIO4 and the other end to ground (via a 60ohm resistor).

## Installing

```
git clone...
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

## My story, what's yours?

I use pushbuttond to quickly flip between information dashboards at my desk.

If I quickly need to see the Bitesize Kanban board ... push the button.

Then look at the shaping board, the audience stats, the bug list ... push, push, push the button.

I'd love to hear what you use pushthebuttond for, so get in touch with me here, or on twitter (@alicraigmile).

Cheers,
Ali
