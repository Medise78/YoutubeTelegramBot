from pytube import YouTube


def test():
    url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'

    youtube = YouTube(url)

    video = youtube.streams.get_highest_resolution()

    video.download(output_path="/home/medise/Documents")


test()
