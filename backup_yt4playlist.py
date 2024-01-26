import subprocess

def get_user_input():
    playlist_urls = input("Podaj linki do playlist z YouTube (oddzielone spacją): ").split()
    output_format = input("Wybierz format wyjściowy (m4a lub opus): ").lower()
    output_directory = input("Podaj katalog docelowy: ")

    return playlist_urls, output_format, output_directory

def download_playlists(playlist_urls, output_format, output_directory):
    for playlist_url in playlist_urls:
        try:
            command = [
                "yt-dlp",
                "-x",
                "--audio-format", output_format,
                "-o", f"{output_directory}/%(title)s.%(ext)s",
                playlist_url
            ]

            print(f"Downloading playlist: {playlist_url}")
            subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"Download successful: {playlist_url}")

        except subprocess.CalledProcessError as e:
            print(f"Error downloading playlist {playlist_url}: {e}")

if __name__ == "__main__":
    playlist_urls, output_format, output_directory = get_user_input()

    # Sprawdzanie poprawności wyboru formatu
    if output_format not in ['m4a', 'opus']:
        print("Nieprawidłowy format wyjściowy. Wybierz m4a lub opus.")
    else:
        download_playlists(playlist_urls, output_format, output_directory)

