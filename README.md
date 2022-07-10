# Martinloop
Circular Martingale Random Walk generator
This is another quick python program I wrote, inspired by the old Rorschach xscreensaver. I've always wanted to see an animated version of that sort of random walk, but most of the obvious ways to do so lead to very "jumpy" animation due to the linear casulity of the walk: The steps near the beginning affect the entire walk, while the steps at the end only affect a few. To remedy this, I decided to make a sort of bastardization of a Martingale that was "circular", by having each step only affect the next n steps of the path, looping back to the beginning when it gets to the end. As a bonus of it being a closed loop, there's a very easy wat to "fill" it, which I think gives a very aesthetically pleasing result when mirrored in the same fashion as the original Rorschach xscreensaver.
![jgan10](https://user-images.githubusercontent.com/108229050/178139975-1260c8f5-3ffc-440b-952e-8fabe5cc8dc6.gif)
