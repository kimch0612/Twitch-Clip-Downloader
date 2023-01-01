import json
import youtube_dl

err = 0
ferr = 0

while True:
    if __name__ == "__main__":
        file_path = input("파일 이름 입력: ")
        file_extend = file_path.split('.')[-1]
     
        if file_extend == 'json':
            with open(file_path, 'r', encoding='UTF-8') as file:
                data = json.load(file)
            clip_link = list(map(lambda x:[x['url'],x['title'],x['created_at'],x['gamename']], data))
          
            for item in clip_link:
                time = item[2].split("T")[0]
                title = item[1].replace("%", "").replace("/","_").replace("\\","").replace("?","").replace("*", "").replace("<","").replace(">","").replace("|","").replace(":","-").replace("\"","").replace("?", "").replace("？", "").replace("！", "!").replace("*", "").replace("\n", "")
                game = item[3].replace("%", "").replace("/","_").replace("\\","").replace("?","").replace("*", "").replace("<","").replace(">","").replace("|","").replace(":","-").replace("\"","").replace("?", "").replace("？", "").replace("！", "!").replace("*", "").replace("\n", "")
                err = 0
            
                while True:
                    if err == 5:
                        ferr += 1
                        break
                    else:
                        try:
                            ydl_opts = {
                                'outtmpl': f'({time} {game}) {title}.mp4',
                                'format': 'bestvideo/best'
                                }
                            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([item[0]])
                            break
                        except:
                            err += 1
                            continue
            break

print("건너뛰기한 파일의 개수는 총 %s개입니다.", ferr)