#README

###JSON config file for dmxSocket python server config.json
universe: dmx universe  *(default = 1)* --will have to match the universe that OLA is looking for.  
channel:  dmx channel   *(default = 1)*  
vid1:     file path                   -- notice the videos file folder is also called out  
vid *x*:   file path                   -- there are 20 slots for videos  

###Notes

>each video is triggered at 5% dmx value increments  
- 0% = Blackout
- 5% = video 1
- 10% = video 2
- *etc.*

Any value in between will have no effect. Videos are locked from retriggering as the DMX value is continuously sent. 
Videos will be retriggered if the percentage is changed and then you return to the previous value 5% -> 6% -> 5%.  
Videos are not protected from retriggering if they are already playing. 




