#!/bin/python3
if __name__ == 'main':
    import encode_util
    import argparse
    prog_name = "nicotamai"
    version = "0.1.0"
    writer = "sesameoil"
    license = "CC0 1.0 Universal. See Also LICENSE, or "\
        "<https://creativecommons.org/publicdomain/zero/1.0/legalcode>"

    parser = argparse.ArgumentParser(prog=prog_name,
                                     description="Nicotamai encode or decode"
                                     "IN_FILE, or standard input,"
                                     "to OUT_FILE, or standard output.",
                                     usage="usage: %(prog)s [OPTION]... [IN_FILE] [OUT_FILE]",
                                     epilog=f"Writter: {writer}.\nLicence: {license}.",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--decode', action='store_true',
                        help='decode data')
    parser.add_argument('IN_FILE', type=argparse.FileType('r'),
                        help='Input. When IN_FILE is -, read standard input')
    parser.add_argument('OUT_FILE', type=argparse.FileType('w'),
                        help='Output. When OUT_FILE is -, write standard output')
    parser.add_argument('-v', '--version', action='version',
                        version=(f"%(prog)s {version}\n\nWritter: {writer}.\nLicence: {license}."))

    args = parser.parse_args()
    if args.decode:
        with args.IN_FILE.read() as nicotamai:
            byts = encode_util.decode(nicotamai)
            with args.OUT_FILE.buffer as buffer_OUT_FILE:
                buffer_OUT_FILE.write(byts)
    else:
        with args.IN_FILE.buffer as buffer_IN_FILE:
            byts = buffer_IN_FILE.read()
            with args.OUT_FILE as OUT_FILE:
                nicotamai = encode_util.encode(byts)
                OUT_FILE.write(nicotamai + '\n')
