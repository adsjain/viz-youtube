# Processes from:
#   id, views, comments, related_video_1, ... , related_video_20
# to:
#   views(id), comments(id), views(related_video_1), comments(related_video_1)
#   ...
#   views(id), comments(id), views(related_video_20), comments(related_video_20)

import csv
import copy
global dict1File
global dict2File

def resetFiles():
    dict1File.seek(0)
    dict2File.seek(0)

def get_video_for_id(id,dictionary):
    resetFiles()
    try:
        while True :
            current_video = dictionary.next()
            if current_video["id"] == id:
                return current_video
    except StopIteration :
        return {}


def get_related_videos(video,dictionaries):

    related_ids = [video["related_1"],video["related_2"],video["related_3"],video["related_4"],video["related_5"],video["related_6"],video["related_7"],video["related_8"],video["related_9"],video["related_10"],video["related_11"],video["related_12"],video["related_13"],video["related_14"],video["related_15"],video["related_16"],video["related_17"],video["related_18"],video["related_19"],video["related_20"]]
    #related_ids = [video["related_1"],video["related_2"],video["related_3"]]
    related_videos = []

    for related_id in related_ids:
        video = get_video_for_id(related_id,dictionaries[1])
        if not video:
            video = get_video_for_id(related_id,dictionaries[0])
        related_videos.append(video)

    return related_videos

if __name__ == '__main__':
    path_to_dir = "../data/datasets/0403/"
    dict1File1 = open(path_to_dir+"0-2.txt", "rb")
    dict1File = open(path_to_dir+"0.txt", "rb")
    dict2File = open(path_to_dir+"1.txt", "rb")
    outputFile = open("data.csv", "w")

    # Dictionaries
    dict1 = csv.DictReader(dict1File, delimiter="\t")
    dict2 = csv.DictReader(dict2File, delimiter="\t")
    videos = csv.DictReader(dict1File1, delimiter="\t")

    counter = 1
    outputFile.write("related_comments,comments,views,related_views\n")

    # try:
    for video in videos:
        related_videos = get_related_videos(video,[dict1,dict2])
        for related_video in related_videos:
            if related_video != {}:
                try:
                    line = related_video['comments']+','+video['comments']+','+video['views']+','+related_video['views']+'\n'
                    outputFile.write(line)
                except TypeError:
                    print related_video
                # print related_video['comments']+'\t'+video['comments']+'\t'+video['views']+'\t'+related_video['views']
        counter += 1
        print str(counter)+"/"+"326"

    # while True :
    #     video = videos.next()
    #     print video
    #     related_videos = get_related_videos(video,[dict1,dict2])
    #
    #
    #     for related_video in related_videos:
    #         if related_video != {}:
    #             print related_video['comments']+'\t'+video['comments']+'\t'+video['views']+'\t'+related_video['views']
    #     counter -= 1
    #
    #     if counter == 0:
    #         break
    #
