import sys
from Organiser import Organiser
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.organiser = Organiser(self.path)
        # add command line argument to turn off the auto clean at start
        self.organiser.arrange_files()
        # recursive file checker
    def on_closed(self, event: FileSystemEvent) -> None:
        return super().on_closed(event)
    def on_created(self, event: FileSystemEvent) -> None:
        if not event.is_directory:
            self.organiser.arrange_file(event.src_path)
    def on_deleted(self, event: FileSystemEvent) -> None:
        print("deleted")
        return super().on_deleted(event)
    def on_modified(self, event: FileSystemEvent) -> None:
        return super().on_modified(event)
    def on_moved(self, event: FileSystemEvent) -> None:
        return super().on_moved(event)
    

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = Handler(path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()