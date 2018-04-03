import glob, os, argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Batch Renamer')
    parser.add_argument('--dir', type=str, required=True, default='./',
                        help='Directory for things to be renamed')
    parser.add_argument('--pattern', type=str, required=False, default='*',
                        help='pattern to choose')
    parser.add_argument('--prefix', type=str, required=False, default='',
                        help='prefix to add to the filename')
    parser.add_argument('--postfix', type=str, required=False, default='',
                        help='postfix to add to the filename')
    return parser.parse_args()


def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, os.path.join(dir, titlePattern % title + ext))


if __name__ == '__main__':
    args = parse_args()
    tp = str(args.prefix) + "%s" + str(args.postfix)
    rename(args.dir, args.pattern, tp)
