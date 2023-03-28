#                                     ***** download Youtube Vidio File ***** 
from pytube import YouTube 

class YoutubeDowload:
 
       def videodownlaod(self,YoutubeURL): 
         try:
            youtube_1 = YouTube(YoutubeURL)
            # print(youtube_1.title)
            # print(youtube_1.thumbnail_url)
            videos = youtube_1.streams.all() # only video files
            vid = list(enumerate(videos))
            for element in vid:
                print(element)
            
            strm = int(input("enter : "))
            videos[strm].download()
            print(" Your video download successfully :",youtube_1.title)

         except Exception as e:
            print(e) 


Object=YoutubeDowload()

link1 = "https://www.youtube.com/watch?v=Hvkt1s5Y7DY"
Object.videodownlaod(link1)   # video function call