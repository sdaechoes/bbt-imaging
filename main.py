import argparse

from os.path import join

import cv2


def get_frames(video_filename):
    """Extract video frames

    Keyword Arguments:
    @param video_filename: The input video file name
    @type video_filename: str

    @returns: The video frames
    @rtype: list
    """
    # Initializing the video decoder
    vhandler = cv2.VideoCapture(video_filename)

    # Reading frames
    v_frames = []
    while True:
        ret, frame = vhandler.read()
        if ret:
            v_frames.append(frame)
        else:
            break

    # Releasing the video
    vhandler.release()

    return v_frames


def save_images(images, out_dir):
    """Save a batch of images to disk

    Keyword Arguments:
    @param images: The images
    @type images: list
    @param out_dir: Output directory
    @type out_dir: str
    """
    for i, img in enumerate(images):
        name = join(out_dir, 'image_%d.jpg' % i)
        cv2.imwrite(name, img)


def main():
    """Main function"""
    # Param declaration
    ap = argparse.ArgumentParser()
    ap.add_argument('-o', '--out_dir', required=False, default='.',
                    help='Output directory')
    ap.add_argument('-i', '--input_video', required=True, help='Input video')
    args = ap.parse_args()

    imgs = get_frames(args.input_video)
    print('Total frames detected: %d' % len(imgs))

    save_images(imgs, args.out_dir)


if __name__ == '__main__':
    main()
