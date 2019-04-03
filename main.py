import os
lyrics_list=os.listdir("Lyrics")

cleaned_lyrics_list_of_list=[]

for i in range(len(lyrics_list)):
	select=lyrics_list[i]
	select=select.strip('.txt')
	select=select.replace('-',' ')
	select=select.split('~')
	cleaned_lyrics_list_of_list.append(select)	

for i in range(len(lyrics_list)):
	a=cleaned_lyrics_list_of_list[i][0]
	b=int(a)
	cleaned_lyrics_list_of_list[i][0]=b

from operator import itemgetter
sorted_lyrics=sorted(cleaned_lyrics_list_of_list,key=itemgetter(0))


total_output_list=[]
for i in range(len(sorted_lyrics)):
	song_output={}
	song_output['id']=sorted_lyrics[i][0]
	song_output["artist"]=sorted_lyrics[i][1]
	song_output["title"]=sorted_lyrics[i][2]
	song_output['kid_safe']=0
	song_output['love']=0
	song_output['mood']=0
	song_output['length']=0
	song_output['complexity']=0
	total_output_list.append(song_output)



final_output={'characterizations':total_output_list}
