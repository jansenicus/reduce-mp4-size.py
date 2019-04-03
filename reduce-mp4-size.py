#!/usr/bin/python
import os, sys

def resize(filename):

    initial_number=1
    initial_filename = 'output{initial_number}.mp4'.format(**locals())
    initial_size=os.path.getsize(initial_filename)

    retry = 21

    for i in range(retry):

        initial_filename = 'output{initial_number}.mp4'.format(**locals())
        initial_number += 1
        output_filename = 'output{initial_number}.mp4'.format(**locals())
        # command format: 
        # ffmpeg -i output4.mp4 -vcodec libx264 -crf 24 output5.mp4'.format(**locals())
        #
        command = "ffmpeg -i {initial_filename} -vcodec libx264 -crf 24 {output_filename}".format(**locals())
        print(command)
        os.system(command)
        output_size = os.path.getsize(output_filename)
        os.remove(initial_filename)


    print('output size is '+ str("{:.2f}".format(output_size/initial_size * 100)) +'% of the original size')


if __name__ == '__main__':

    try:
        original_filename = sys.argv[1]
        resize(original_filename)
    except:
        print('please specify a file name input')
        print('\nUSAGE:\npython '+ __file__ +' [input filename]\n')
