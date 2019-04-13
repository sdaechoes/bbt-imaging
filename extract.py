import argparse

from os.path import join

from utils import extract_frames, get_unique_frames, save_images


def __main():
    """Main function"""

    # Parameters declaration and parsing
    ap = argparse.ArgumentParser()
    ap.add_argument('-of', '--out_dir', required=False,
                    default='.', help='Output directory')
    ap.add_argument('-i', '--input_video', required=True, help='Input video')
    ap.add_argument('-t', '--threshold', required=False, default=50,
                    help='The threshold to decide if two frames are the same')
    args = ap.parse_args()

    frames = extract_frames(args.input_video)
    print('Total frames extracted: %d' % len(frames))

    save_images(frames, join(args.out_dir, 'all'))

    frames = get_unique_frames(frames, int(args.threshold))
    print('Unique frames: %d' % len(frames))

    save_images(frames, join(args.out_dir, 'uniques'))


if __name__ == '__main__':
    __main()
