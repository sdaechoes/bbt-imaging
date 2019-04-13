import argparse

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def extract_subclip(video, start, end, output):
    """Extract video subclip"""
    ffmpeg_extract_subclip(video, start, end, targetname=output)


def __main():
    """Main function"""

    # Parameters declaration and parsing
    ap = argparse.ArgumentParser()
    ap.add_argument('-o', '--out_video', required=False,
                    default='.', help='Output video')
    ap.add_argument('-i', '--input_video', required=True, help='Input video')
    ap.add_argument('-s', '--start', required=True,
                    help='Start time in seconds')
    ap.add_argument('-e', '--end', required=True, help='End time in seconds')
    args = ap.parse_args()

    extract_subclip(args.input_video, float(args.start), float(args.end),
                    args.out_video)


if __name__ == '__main__':
    __main()
