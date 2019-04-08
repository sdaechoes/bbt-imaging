import argparse

from os.path import join

import cv2

from fhandle import extract_frames, get_unique_frames


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


def __main():
    """Main function"""

    # Parameters declaration and parsing
    ap = argparse.ArgumentParser()
    ap.add_argument('-of', '--out_dir', required=False,
                    default='.', help='Output directory')
    ap.add_argument('-i', '--input_video', required=True, help='Input video')
    args = ap.parse_args()

    frames = extract_frames(args.input_video)
    print('Total frames detected: %d' % len(frames))

    save_images(frames, join(args.out_dir, 'all'))

    frames = get_unique_frames(frames)
    print('Unique frames: %d' % len(frames))

    save_images(frames, join(args.out_dir, 'uniques'))


if __name__ == '__main__':
    __main()
