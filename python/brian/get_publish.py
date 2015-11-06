import os
import re
import argparse


def get_publish(seq, step, offset):
    """
    scrapes the dir argument path and retrieves the latest publishes.
    which can be of-set with the offset argument
    """
    latest_publishes = set()
    root = r'Z:\Projects\the_space_between_us\sequences'    
        
    seq_dir = os.path.join(root, seq)

    if not os.path.isdir(seq_dir):
        raise RuntimeError("You have not specified a valid sequence code")


    shots = [shot for shot in os.listdir(seq_dir) if re.search(r'[A-Z]{2}[0-9]{3}_[0-9]{3}', shot)]

    for shot in shots:
        shot_dir = os.path.join(seq_dir, shot)

        if not any(step.lower() in s.lower() for s in os.listdir(shot_dir)):
            print "%s contains no valid pipeline step." % shot
            continue

        maya_dir = os.path.join(shot_dir, step, "Publish\\maya\\")

        try:
            publish_files = os.listdir(maya_dir)
        except WindowsError:
            continue

        publishes = [x for x in publish_files if x.endswith(".ma") and re.search(r'v[0-9]{3}', x)]

        if not publishes:
            continue

        index = max(-1 - int(offset), -len(publishes))
        file_path = os.path.join(maya_dir, sorted(publishes)[index])
        latest_publishes.add(file_path)

    return latest_publishes


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Get the latest publishes of the specified type")
    parser.add_argument("sequence",  help="the sequence name")
    parser.add_argument("step", help="the pipeline step name name; for example 'anm' or 'lighting'")
    parser.add_argument("--offset", metavar="-o", type=int, default = 0, 
                        help="offset the version number to fetch by this value. "
                             "offset of 1 gets the second to last publish.")

    args = parser.parse_args()

    publish_list = get_publish(args.sequence, args.step, args.offset)
    print publish_list