import sys
from Organiser import Organiser
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler, LoggingEventHandler

class Handler(LoggingEventHandler):
    def __init__(self, path, logger):
        super().__init__(logger=logger)
        self.path = path
        self.organiser = Organiser(self.path)
        # add command line argument to turn off the auto clean at start
        self.organiser.initial_clean()
        # recursive file checker
    # def on_closed(self, event: FileSystemEvent) -> None:
    #     return super().on_closed(event)
    def on_created(self, event: FileSystemEvent) -> None:
        super().on_created(event)

        # exclude directories and hidden files
        if not event.is_directory and not os.path.basename(event.src_path).startswith('.'):
            self.organiser.arrange_file(event.src_path)


    def on_deleted(self, event: FileSystemEvent) -> None:
        super().on_deleted(event)
    def on_modified(self, event: FileSystemEvent) -> None:
        super().on_modified(event)
    def on_moved(self, event: FileSystemEvent) -> None:
        super().on_moved(event)
        if not event.is_directory and not os.path.basename(event.dest_path).startswith('.'):
            self.organiser.arrange_file(event.dest_path)

    

if __name__ == "__main__":
    logger = logging.getLogger('pywatch') # config logger
    # logging config
    logging.basicConfig(filename='pywatch.log', 
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)
    
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = Handler(path, logger)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()