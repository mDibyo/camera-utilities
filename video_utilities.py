#!/usr/bin/env python

__author__ = "Dibyo Majumdar"
__email__ = "dibyo.majumdar@gmail.com"

import cv2


def extract_video_file(input_filename, output_filename, output_fps, output_width):
    capture = cv2.VideoCapture(input_filename)

    # fps handling
    input_fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
    input_fps = 30
    print input_fps
    assert output_fps <= input_fps and input_fps % output_fps == 0, 'invalid output fps'
    frame_modulo = input_fps // output_fps

    # frame size handling
    input_width = capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    assert output_width <= input_width, 'invalid output width'
    size_multiplier = output_width / input_width
    input_height = capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    output_height = int(input_height * size_multiplier)
    output_size = (output_width, output_height)

    writer = cv2.VideoWriter(output_filename, cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'),
                             output_fps, output_size)

    frame_index = 0
    while True:
        retcode, next_frame = capture.read()
        if not retcode:
            break
        if frame_index % frame_modulo == 0:
            output_frame = cv2.resize(next_frame, output_size)
            writer.write(output_frame)
        frame_index += 1

    capture.release()
    writer.release()


if __name__ == '__main__':
    print 'Format: video_utilities.py <input_filename> <output_filename> <output_fps> <output_width>'

    import sys
    argv = sys.argv
    print argv
    assert len(sys.argv) >= 5, 'not enough input arguments'

    input_filename = argv[1]
    output_filename = argv[2]
    output_fps = int(argv[3])
    output_width = int(argv[4])
    extract_video_file(input_filename, output_filename, output_fps, output_width)


