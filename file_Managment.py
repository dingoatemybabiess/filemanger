import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileManager:
    def __init__(self, base_path=None):
        self.base_path = base_path or os.getcwd()

    def list_files(self, path=None):
        path = path or self.base_path
        return os.listdir(path)

    def create_folder(self, folder_name, path=None):
        path = path or self.base_path
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        return folder_path

    def delete_file(self, file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)
            return True
        return False

    def delete_folder(self, folder_path):
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            return True
        return False

    def move_file_with_retry(self, src, dest, retries=5, delay=1):
        for i in range(retries):
            try:
                shutil.move(src, dest)
                print(f"Moved {src} to {dest}")
                return True
            except PermissionError:
                print(f"File {src} is in use, retrying in {delay} seconds...")
                time.sleep(delay)
        print(f"Failed to move {src} after {retries} retries.")
        return False

    def copy(self, src, dst):
        if os.path.isfile(src):
            shutil.copy2(src, dst)
        elif os.path.isdir(src):
            shutil.copytree(src, dst)
        return dst

    def rename(self, src, new_name):
        dst = os.path.join(os.path.dirname(src), new_name)
        os.rename(src, dst)
        return dst

    def organize_downloads(self, downloads_path, rules):
        fm = self  # reference for inner class

        class Handler(FileSystemEventHandler):
            def on_created(self, event):
                if not event.is_directory:
                    file_ext = os.path.splitext(event.src_path)[1].lower()
                    for folder, extensions in rules.items():
                        if file_ext in extensions:
                            dest_folder = os.path.join(downloads_path, folder)
                            os.makedirs(dest_folder, exist_ok=True)
                            dest_path = os.path.join(dest_folder, os.path.basename(event.src_path))
                            fm.move_file_with_retry(event.src_path, dest_path)
                            break

        event_handler = Handler()
        observer = Observer()
        observer.schedule(event_handler, downloads_path, recursive=False)
        observer.start()
        print("Monitoring downloads folder...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def organize_existing_files(self, downloads_path, rules):
        for filename in os.listdir(downloads_path):
            file_path = os.path.join(downloads_path, filename)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                for folder, extensions in rules.items():
                    if file_ext in extensions:
                        dest_folder = os.path.join(downloads_path, folder)
                        os.makedirs(dest_folder, exist_ok=True)
                        dest_path = os.path.join(dest_folder, filename)
                        self.move_file_with_retry(file_path, dest_path)
                        break


# Example usage:
if __name__ == "__main__":
    fm = FileManager()
    rules = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Setups": [".exe", ".msi"],
        "Documents": [".pdf", ".docx", ".txt", ".md"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Archives": [".zip", ".rar", ".7z"],
        "Music": [".mp3", ".wav", ".flac"],
        "Notbooks": [".ipynb"],
        "dev": [".py", ".js", ".html", ".css", ".json", ".xml", ".c", ".cpp", ".java", ".rb", ".go", ".rs"]
    }
    downloads_folder = os.path.expanduser("C:/Users/ghoni/Downloads")
    fm.organize_existing_files(downloads_folder, rules)
    fm.organize_downloads(downloads_folder, rules)
# Note: To stop the monitoring, you can interrupt the program (e.g., Ctrl+C in terminal).