import os
from pytube import YouTube

def get_downloads_folder():
    """Get the path to the user's downloads folder."""
    home = os.path.expanduser("~")
    return os.path.join(home, "Downloads")

def download_video(url):
    try:
        my_video = YouTube(url)

        print("********************* Video Title ************************")
        print(my_video.title)

        print("******************** Thumbnail Image *********************")
        print(my_video.thumbnail_url)

        print("******************** Available Resolutions ****************")
        for stream in my_video.streams:
            print(stream)

        selected_stream = my_video.streams.get_highest_resolution()

        # Get the path to the user's downloads folder
        downloads_folder = get_downloads_folder()

        print("******************** Downloading Video *******************")
        # Set the download path to the downloads folder
        download_path = os.path.join(downloads_folder, f"{my_video.title}.mp4")
        selected_stream.download(download_path)

        print(f"******************** Download Complete! ******************\nSaved to: {download_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the YouTube Video Downloader!")

    while True:
        video_url = input("Enter the YouTube video URL (type 'exit' to quit): ")

        if video_url.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        download_video(video_url)

if __name__ == "__main__":
    main()
