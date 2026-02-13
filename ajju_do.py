import os
import shutil
import argparse
import subprocess
import sys
from pathlib import Path

# ================= AUTO DEPENDENCY CHECK =================
REQUIRED_PACKAGES = ["yt-dlp", "rich"]

def check_and_install_dependencies():
    missing = []
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing.append(package)

    if missing:
        print("Installing missing packages:", ", ".join(missing))
        for package in missing:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("Dependencies installed successfully.\n")

check_and_install_dependencies()

# Safe imports
import yt_dlp
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn

console = Console()
VERSION = "3.6.0"


# ================= DOWNLOAD FOLDER =================
def get_windows_download_folder():
    downloads_path = Path.home() / "Downloads"
    downloads_path.mkdir(parents=True, exist_ok=True)
    return str(downloads_path)

DEFAULT_DOWNLOAD_PATH = get_windows_download_folder()


# ================= FFMPEG CHECK =================
def ffmpeg_available():
    return shutil.which("ffmpeg") is not None


# ================= LOGO =================
def print_logo():
    logo = rf"""
      █████╗        ██╗      ██╗     ██╗   ██╗
     ██╔══██╗       ██║      ██║     ██║   ██║
     ███████║       ██║      ██║     ██║   ██║
     ██╔══██║       ██║      ██║     ██║   ██║
     ██║  ██║  ███████╗ ███████╗     ╚██████╔╝
     ╚═╝  ╚═╝  ╚══════╝ ╚══════╝      ╚═════╝

                  A  J  J  U
        Yt Downloader PRO v{VERSION}
    """
    console.print(Panel(logo, style="bold cyan"))


# ================= QUALITY SELECTOR =================
def choose_quality():
    console.print("\n[bold cyan]Select Download Quality:[/bold cyan]")
    console.print("1 - Best (Auto)")
    console.print("2 - 1080p")
    console.print("3 - 720p")
    console.print("4 - 480p")
    console.print("5 - Audio Only (MP3)")

    choice = input("Enter choice number: ")

    if choice == "2":
        return "bestvideo[height<=1080]+bestaudio"
    elif choice == "3":
        return "bestvideo[height<=720]+bestaudio"
    elif choice == "4":
        return "bestvideo[height<=480]+bestaudio"
    elif choice == "5":
        return "bestaudio"
    else:
        return "bestvideo+bestaudio"


# ================= DOWNLOAD FUNCTION =================
def download_video(url, format_code, playlist_mode):

    progress = Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
        console=console
    )

    def hook(d):
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            downloaded = d.get("downloaded_bytes", 0)
            if not hasattr(hook, "task"):
                hook.task = progress.add_task("Downloading...", total=total)
            progress.update(hook.task, completed=downloaded)

    ydl_opts = {
        "format": format_code,
        "outtmpl": os.path.join(DEFAULT_DOWNLOAD_PATH, "%(playlist_title)s/%(title)s.%(ext)s") if playlist_mode
                   else os.path.join(DEFAULT_DOWNLOAD_PATH, "%(title)s.%(ext)s"),
        "progress_hooks": [hook],
        "merge_output_format": "mp4",
        "noplaylist": not playlist_mode
    }

    # Audio mode
    if format_code == "bestaudio" and ffmpeg_available():
        ydl_opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]

    with progress:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    console.print("\n[bold green]Download Completed Successfully![/bold green]")
    console.print(f"[cyan]Saved to:[/cyan] {DEFAULT_DOWNLOAD_PATH}")


# ================= CHECK PLAYLIST =================
def is_playlist(url):
    return "playlist" in url or "list=" in url


# ================= MAIN =================
def main():
    parser = argparse.ArgumentParser(prog="ajju")
    parser.add_argument("--version", action="store_true")
    args = parser.parse_args()

    if args.version:
        console.print(f"AJJU v{VERSION}")
        return

    print_logo()

    if not ffmpeg_available():
        console.print("[yellow]Warning: FFmpeg not found. Audio merging may not work.[/yellow]\n")

    console.print("[bold cyan]Step 1:[/bold cyan] Paste the YouTube link below.")
    url = input(">> ")

    console.print("\nPress ENTER to proceed to next step...")
    input()

    playlist_mode = False

    if is_playlist(url):
        choice = input("Playlist detected. Download full playlist? (y/n): ").lower()
        if choice == "y":
            playlist_mode = True

    format_code = choose_quality()

    console.print("\nStarting download...\n")
    download_video(url, format_code, playlist_mode)


if __name__ == "__main__":
    main()
