# importing vlc module 
import vlc 

# importing pafy module 
import pafy 

url = "https://www.youtube.com/watch?v=x4W2HhqXM9s&ab_channel=LogicalSpot"

video = pafy.new(url) 
best = video.getbest() 
media = vlc.MediaPlayer(best.url) 
media.play() 

while True:
    pass