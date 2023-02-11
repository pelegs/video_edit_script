#!/usr/bin/env python3

import argparse


# Arguments
parser = argparse.ArgumentParser(
    description="Script to edit a two-camera video using ffmpeg"
)
parser.add_argument(
    "-v1", "--vid1", help="Video from 1st camera", required=True
)
parser.add_argument(
    "-v2", "--vid2", help="Video from 2nd camera", required=True
)
parser.add_argument(
    "-t",
    "--timestamps-file",
    help="File with list of timestamps for changing cameras",
    required=True,
)
parser.add_argument("-o", "--output", help="Output filename", required=True)
args = vars(parser.parse_args())


if __name__ == "__main__":
    with open(args['timestamps_file'], "r") as f:
        timestamps = [line.rstrip() for line in f]

    cut_cmd = [
        f"-ss {timestamps[i]} -to {timestamps[i+1]} -i {args['vid1']}"
        if i % 2 == 0 else
        f"-ss {timestamps[i]} -to {timestamps[i+1]} -i {args['vid2']}"
        for i, _ in enumerate(timestamps[:-1])
    ]
    print(cut_cmd)
# "-ss" "$s" "-to" "$t" "-i"
