first, pygame module needs to be imported. then, it needs to be initialized. 

following that, a screen can be made. the screen is nothing more than a surface?

after the screen, a while True loop keeps the program running indefinitely, or at least, until it's broken. this lets the screen stay active for longer than a single run. 

the line pygame.display.update() updates the display surface. according to guide don't really need to think too hard about it, but i think it updates all surfaces at the same time? 

since the while loop's condition is simply true, the loop will technically never end, so creating an escape method is important. 

cleanly exiting the program requires the sys module. exit() kills the program. 

frame rate is important. animation speed depends on how fast the game is being updated, ie more frames per second mean more things happening per second, so handling that is important. const frame rates are easy. 

capping frames is very easy, just tell pc to pause betwixt frames. however, increasining min frames is very hard since it's hardware dependent. 

surface is a thing in pygame. the main window is a type of surface. regular surfaces are different. ig it's some sort of "thing" to display stuff on. regular surface are analogous to the papers and graphs you stick on a display board for the science fair lmao. 

pygame.Surface() makes a surface. 1 argument, a tuple with 2 objects, width + height.

blit stands for block image transfer and is needed to put a surface on another surface. two args, the surface to display and the position. i think this also accepts rects. 

pygame windows follow a coordinate system more or less. top left is origin, right is pos x, down is +y. no idea why, it's like the first quadrant except flipped upside down. this reminds me of a transformation in linear algebra. 

rendering images. first item in the code is first displayed, so items later rendered are rendered on top of the previous ones. i was going to compare this to a sort of data struct, but FIFO and FILO both sort of make sense. First item being first out means first item in list is first rendered, ie queue, but the way the images layer on each other is more reminiscent of a stack, with first item rendered being the last one out, ie the first item is at the bottom. 

as i typed that out, I realized it's probably a stack structure.

first step to creating text is making a font available for use. then you write the actual text to a surface, and blit the surface onto the screen, 

makeing a font, pygame.font.Font(). two args, font type, and size. 



































