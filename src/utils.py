import os
import fnmatch


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]


def should_ignore(path, ignore_patterns):
    return any(fnmatch.fnmatch(path, pattern) for pattern in ignore_patterns)


def get_folders_files(path, ignore_patterns):
    folders_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        # Filter directories and files based on ignore patterns
        dirnames[:] = [d for d in dirnames if not should_ignore(os.path.join(dirpath, d), ignore_patterns)]
        filenames[:] = [f for f in filenames if not should_ignore(os.path.join(dirpath, f), ignore_patterns)]
        for filename in filenames:
            folders_files.append(os.path.join(dirpath, filename))
    return folders_files


def is_file(path):
    return os.path.isfile(path)
