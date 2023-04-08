import requests, json, sys
videoHash = requests.get(str(sys.argv[1])).text.split('<link rel="video_src" href="https://embed.indavideo.hu/player/video/')[1].split('"')[0]
videoData = requests.get("https://amfphp.indavideo.hu/SYm0json.php/player.playerHandler.getVideoData/" + videoHash + "/12////https://embed.indavideo.hu/player/video/" + videoHash).json()["data"]
videoTokens = videoData["filesh"]
videoFiles = videoData["video_files"]
print(json.dumps({list(videoTokens)[x]: (videoFiles[x] + "&token=" + videoTokens[list(videoTokens)[x]]) for x in range(0, len(videoFiles))}))
