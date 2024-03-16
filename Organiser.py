import sys
import os
import logging
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
        self.path = path
        
        # Creating directories and checking if they are already present 
        for dir in self.directories:
            path_dir = os.path.join(path, dir)

            if not (os.path.exists(path_dir) and os.path.isdir(path_dir)):
                os.mkdir(path_dir)
            else:
                print(f'{dir} directory already exists')

    def arrange_file(self, file):
        if(file.lower().endswith(('.pdf'))):
            self.mv_file(file, 'PDF')
        elif(file.lower().endswith(('.deb'))):
            self.mv_file(file, 'DEB')
        elif(file.lower().endswith(tuple(self.video_extensions))):
            self.mv_file(file, 'VIDEO')
        elif(file.lower().endswith(tuple(self.image_extensions))):
            self.mv_file(file, 'IMAGE')
        elif(file.lower().endswith(tuple(self.document_extensions))):
            self.mv_file(file, 'DOCS')
        elif(file.lower().endswith(tuple(self.archive_extensions))):
            self.mv_file(file, 'ARCHIVES')
        elif(file.lower().endswith(tuple(self.code_extensions))):
            self.mv_file(file, 'SOURCE_CODE')
        elif(file.lower().endswith(tuple(self.executable_extensions))):
            self.mv_file(file, 'EXECUTABLES')
        else:
            self.mv_file(file, 'MISC')

    
    def arrange_files(self):
        # Iterate over files in path
        for file in os.listdir(self.path):
        #    pass
        #for (root, dirs, files) in os.walk(self.path, topdown=True):

            # os.path.abspath() not working
            file = os.path.join(self.path, file)
            if os.path.isfile(file):
                print(file)
                self.arrange_file(file)

    def mv_file(self, src_path, dest_folder):
        #src_path = os.path.join(self.path, filename)
        dest_path = os.path.join(self.path, dest_folder, os.path.basename(src_path))

        try:
            os.rename(src_path, dest_path)
            print(f'[MV]: {src_path} moved to {dest_path}')
        except OSError as e:
            print(f'An error occurred {e}')
        
            