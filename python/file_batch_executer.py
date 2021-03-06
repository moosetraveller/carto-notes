#!c:/program files/arcgis/pro/bin/python/envs/arcgispro-py3/python.exe
# -*- coding: utf-8 -*-

# Just a training script to get familiar with the ABC package.
#
# Author: Thomas Zuberbuehler (thomas.zuberbuehler@gmail.com)

import os
from abc import ABC

class FileBatchExecuter:
    def __init__(self, directories, recursive=True):
        self.directories = directories
        self.recursive = recursive

    def run(self, fileOperation):
        for directory in self.directories:
            for path, directories, files in os.walk(directory):
                for f in files:
                    fileOperation.handleFile(path, f, os.path.join(path, f))
                for d in directories:
                    fileOperation.handleDirectory(path, f, os.path.join(path, d))
        fileOperation.summarize()

class FileOperation(ABC):
    def handleFile(self, path, file, fullPath):
        pass
    def handleDirectory(self, path, directory, fullPath):
        pass
    def summarize(self):
        pass

class FileNamePrinter(FileOperation):
    def __init__(self):
        self.inc = 0
    def handleFile(self, path, file, fullPath):
        print (fullPath)
        self.inc = self.inc+1
    def summarize(self):
        print ("{} files".format(self.inc))

class TextFileFinder(FileOperation):
    def __init__(self):
        self.inc = 0
    def handleFile(self, path, file, fullPath):
        if fullPath.endswith(".txt"):
            print (fullPath)
            self.inc = self.inc+1
    def summarize(self):
        print ("{} files".format(self.inc))

class DirNamePrinter(FileOperation):
    def handleDirectory(self, path, file, fullPath):
        print (fullPath)

executer = FileBatchExecuter(["C:\\OSGeo4W64", "C:\\Windows"])
# executer.run(FileNamePrinter())
# executer.run(TextFileFinder())
executer.run(DirNamePrinter())
