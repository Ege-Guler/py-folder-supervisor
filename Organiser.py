import sys
import os
class Organiser():

    directories = ['PDF', 'VIDEO', 'IMAGE', 'DEB', 'ARCHIVES', 'SOURCE_CODE', 'DOCS', 'EXECUTABLES', 'MISC']

    video_extensions = [
        '.mp4', '.mov', '.avi', '.wmv', 
        '.webm'
    ]
    image_extensions = [
        '.avif', '.gif','.jpg', '.jpeg',
        '.jfif', '.png', '.svg', '.tif', 
        '.webp'
    ]

    document_extensions = [
        '.pdf', '.docx', '.doc', '.txt', 
        '.odt', '.xls', '.xlsx', '.ods', 
        '.ppt', '.pptx', '.odp', '.csv'
    ]
    
    archives_extensions = [
        '.zip'
    ]
    code_extensions = [
        '.py',  # Python
        '.java',  # Java
        '.c', '.cpp', '.h',  # C and C++
        '.s', '.S', '.asm' # assembly
        '.cs',  # C#
        '.js',  # JavaScript
        '.ts',  # TypeScript
        '.html', '.css',  # HTML and CSS
        '.php',  # PHP
        '.rb',  # Ruby
        '.go',  # Go
        '.rs',  # Rust
        '.swift',  # Swift
        '.kt',  # Kotlin
        '.sql',  # SQL scripts
        '.sh',  # Shell scripts
        '.bat',  # Batch files
        '.pl',  # Perl
        '.r',  # R
        '.m',  # MATLAB
        '.json', '.xml', '.yaml', '.yml',  # Data formats
        '.md'  # Markdown   
    ]

    archive_extensions = [
        '.tar', '.gz', '.zip', '.rar', 
        '.7z', '.bz2', '.xz'
    ]

    executable_extensions = [
        '.exe', '.bat', '.cmd', '.sh', 
        '.app', '.jar', '.out'
    ]


    def __init__(self, path) -> None:

        self.path = os.path.abspath(path)
        
        print(f'Setting Up watchdog for {self.path}')
        # Creating directories and checking if they are already present 
        for dir in self.directories:
            path_dir = os.path.join(path, dir)

            if not (os.path.exists(path_dir) and os.path.isdir(path_dir)):
                os.mkdir(path_dir)
            else:
                print(f'{dir} directory already exists')

    def arrange_file(self, file):
        self.mv_file(file, self.find_file_type(file))

    def find_file_type(self, file):
        if(file.lower().endswith(('.pdf'))):
            return 'PDF'
        elif(file.lower().endswith(('.deb'))):
            return 'DEB'
        elif(file.lower().endswith(tuple(self.video_extensions))):
            return 'VIDEO' 
        elif(file.lower().endswith(tuple(self.image_extensions))):
            return 'IMAGE'
        elif(file.lower().endswith(tuple(self.document_extensions))):
            return 'DOCS'
        elif(file.lower().endswith(tuple(self.archive_extensions))):
            return 'ARCHIVES'
        elif(file.lower().endswith(tuple(self.code_extensions))):
            return 'SOURCE_CODE'
        elif(file.lower().endswith(tuple(self.executable_extensions))):
            return 'EXECUTABLES'
        else:
            return 'MISC'
    
    def mv_file(self, src_path, dest_folder):
        #src_path = os.path.join(self.path, filename)
        dest_path = os.path.join(self.path, dest_folder, os.path.basename(src_path))

        try:
            os.rename(src_path, dest_path)
            print(f'[MV]: {src_path} moved to {dest_path}')
        except OSError as e:
            print(f'An error occurred {e}')

    def arrange_file(self, file):
        self.mv_file(file, self.find_file_type(file))
    def walk_on_filtered_directories(self):
        
        for root, dirs, files in os.walk(self.path, topdown=True):
            dirs[:] = [d for d in dirs if d in self.directories]

            yield root, dirs, files
    def initial_clean(self, exclude_misc=True):
        
        # search 'PDF', 'VIDEO', 'IMAGE', 'DEB', 'ARCHIVES', 'SOURCE_CODE', 'DOCS', 'EXECUTABLES', 'MISC' folders for any misplaced file
        for (root, dirs, files) in self.walk_on_filtered_directories(): # (root, dirs, files)
            for file in files:
                file_type = self.find_file_type(file) # what is the type of the current file
                if file_type not in root: # if it is in the wrong folder
                    
                    if file_type == 'MISC' and not exclude_misc:
                        continue
                    src_path = os.path.join(root, file) # files contains only file names
                    self.mv_file(src_path, file_type) # move file to the folder it is supposed to be
        
        # tidy given path(self.pat)
        for file in os.listdir(self.path):
            file = os.path.join(self.path, file)
            if os.path.isfile(file):
                self.arrange_file(file)
