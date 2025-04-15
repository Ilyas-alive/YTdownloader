import os
import yt_dlp

def download_video(link, mode):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ffmpeg_path = os.path.join(script_dir, "ffmpeg", "bin", "ffmpeg.exe")
        common_opts = {
            'ffmpeg_location': ffmpeg_path,
            'no_warnings': True,
            'concurrent_fragments': 5,
            'limit_rate': '5M',
        }

        if "playlist?list=" in link:
            print("1. Audio\n2. Video")
            media_type = input("Choose media type: ")

            if media_type == '1':
                print("1. Best\n2. Medium\n3. Low")
                audio_quality = input("Choose audio quality: ")
                if audio_quality == '1':
                    format_option = 'bestaudio/best'
                elif audio_quality == '2':
                    format_option = 'bestaudio[abr<=128k]'
                elif audio_quality == '3':
                    format_option = 'bestaudio[abr<=64k]'
                else:
                    print("Invalid choice.")
                    return
            elif media_type == '2':
                print("1. FHD\n2. 720p\n3. 480p\n4. 360p\n5. 144p")
                video_quality = input("Choose video quality: ")
                if video_quality == '1':
                    format_option = 'bestvideo[height<=1080]+bestaudio/best'
                elif video_quality == '2':
                    format_option = 'bestvideo[height<=720]+bestaudio/best'
                elif video_quality == '3':
                    format_option = 'bestvideo[height<=480]+bestaudio/best'
                elif video_quality == '4':
                    format_option = 'bestvideo[height<=360]+bestaudio/best'
                elif video_quality == '5':
                    format_option = 'bestvideo[height<=144]+bestaudio/best'
                else:
                    print("Invalid choice.")
                    return
            else:
                print("Invalid choice.")
                return

            ydl_opts = {
                **common_opts,
                'format': format_option,
                'outtmpl': os.path.join(script_dir, '%(playlist_index)s-%(title)s.%(ext)s'),
            }

        elif "@" in link:
            print("1. Audio\n2. Video")
            media_type = input("Choose media type: ")
            print("How many videos to download?")
            video_count = input("Enter number: ")
            print("1. Latest\n2. Oldest")
            sort_order = input("Choose sort order: ")

            reverse_download = (sort_order == '2')
            if media_type == '1':
                print("1. Best\n2. Medium\n3. Low")
                audio_quality = input("Choose audio quality: ")
                if audio_quality == '1':
                    format_option = 'bestaudio/best'
                elif audio_quality == '2':
                    format_option = 'bestaudio[abr<=128k]'
                elif audio_quality == '3':
                    format_option = 'bestaudio[abr<=64k]'
                else:
                    print("Invalid choice.")
                    return
            elif media_type == '2':
                print("1. FHD\n2. 720p\n3. 480p\n4. 360p\n5. 144p")
                video_quality = input("Choose video quality: ")
                if video_quality == '1':
                    format_option = 'bestvideo[height<=1080]+bestaudio/best'
                elif video_quality == '2':
                    format_option = 'bestvideo[height<=720]+bestaudio/best'
                elif video_quality == '3':
                    format_option = 'bestvideo[height<=480]+bestaudio/best'
                elif video_quality == '4':
                    format_option = 'bestvideo[height<=360]+bestaudio/best'
                elif video_quality == '5':
                    format_option = 'bestvideo[height<=144]+bestaudio/best'
                else:
                    print("Invalid choice.")
                    return
            else:
                print("Invalid choice.")
                return

            ydl_opts = {
                **common_opts,
                'format': format_option,
                'outtmpl': os.path.join(script_dir, '%(title)s.%(ext)s'),
                'playlistend': int(video_count),
                'playlistreverse': reverse_download,
            }

        else:
            print("1. Audio\n2. Video")
            media_type = input("Choose media type: ")
            if media_type == '1':
                print("1. Best\n2. Medium\n3. Low")
                audio_quality = input("Choose audio quality: ")
                if audio_quality == '1':
                    format_option = 'bestaudio/best'
                elif audio_quality == '2':
                    format_option = 'bestaudio[abr<=128k]'
                elif audio_quality == '3':
                    format_option = 'bestaudio[abr<=64k]'
                else:
                    print("Invalid choice.")
                    return
            elif media_type == '2':
                print("1. FHD\n2. 720p\n3. 480p\n4. 360p\n5. 144p")
                video_quality = input("Choose video quality: ")
                if video_quality == '1':
                    format_option = 'bestvideo[height<=1080]+bestaudio/best'
                elif video_quality == '2':
                    format_option = 'bestvideo[height<=720]+bestaudio/best'
                elif video_quality == '3':
                    format_option = 'bestvideo[height<=480]+bestaudio/best'
                elif video_quality == '4':
                    format_option = 'bestvideo[height<=360]+bestaudio/best'
                elif video_quality == '5':
                    format_option = 'bestvideo[height<=144]+bestaudio/best'
                else:
                    print("Invalid choice.")
                    return
            else:
                print("Invalid choice.")
                return

            ydl_opts = {
                **common_opts,
                'format': format_option,
                'outtmpl': os.path.join(script_dir, '%(title)s.%(ext)s'),
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        link = input("Enter the YouTube link: ")
        download_video(link, 'pro')

if __name__ == "__main__":
    main()
