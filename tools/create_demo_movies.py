import argparse
import os
import csv
import base64

demo_movie_base64 = 'AAAAHGZ0eXBpc29tAAACAGlzb21pc28ybXA0MQAAAAhmcmVlAAAAGm1kYXQAAAGzABAHAAABthBgUYI9t+8AAAMNbW9vdg' \
                    'AAAGxtdmhkAAAAAMXMvvrFzL76AAAD6AAAACoAAQAAAQAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAA' \
                    'AAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAABhpb2RzAAAAABCAgIAHAE/////+/wAAAiF0cmFrAA' \
                    'AAXHRraGQAAAAPxcy++sXMvvoAAAABAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAABAAAAAAAA' \
                    'AAAAAAAAAABAAAAAAAgAAAAIAAAAAAG9bWRpYQAAACBtZGhkAAAAAMXMvvrFzL76AAAAGAAAAAEVxwAAAAAALWhkbHIAAA' \
                    'AAAAAAAHZpZGUAAAAAAAAAAAAAAABWaWRlb0hhbmRsZXIAAAABaG1pbmYAAAAUdm1oZAAAAAEAAAAAAAAAAAAAACRkaW5m' \
                    'AAAAHGRyZWYAAAAAAAAAAQAAAAx1cmwgAAAAAQAAAShzdGJsAAAAxHN0c2QAAAAAAAAAAQAAALRtcDR2AAAAAAAAAAEAAA' \
                    'AAAAAAAAAAAAAAAAAAAAgACABIAAAASAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGP//AAAA' \
                    'XmVzZHMAAAAAA4CAgE0AAQAEgICAPyARAAAAAAMNQAAAAAAFgICALQAAAbABAAABtYkTAAABAAAAASAAxI2IAMUARAEUQw' \
                    'AAAbJMYXZjNTMuMzUuMAaAgIABAgAAABhzdHRzAAAAAAAAAAEAAAABAAAAAQAAABxzdHNjAAAAAAAAAAEAAAABAAAAAQAA' \
                    'AAEAAAAUc3RzegAAAAAAAAASAAAAAQAAABRzdGNvAAAAAAAAAAEAAAAsAAAAYHVkdGEAAABYbWV0YQAAAAAAAAAhaGRscg' \
                    'AAAAAAAAAAbWRpcmFwcGwAAAAAAAAAAAAAAAAraWxzdAAAACOpdG9vAAAAG2RhdGEAAAABAAAAAExhdmY1My4yMS4x'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', nargs='?', default='demo/', help='Output demo files to directory')
    parser.add_argument('-i', '--input', nargs='?', default='random-movie-list.csv', help='Input csv file with movie names')
    parser.add_argument('-d', '--delimiter', nargs='?', default=',', help='Csv file delimiter')
    args = parser.parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    if not args.output.endswith('/') or args.output.endswith('\\'):
        args.output = args.output + '/'
    try:
        with open(args.input, 'r') as movielist:
            read_csv = csv.reader(movielist, delimiter=args.delimiter)
            for row in read_csv:
                movie = " ".join(row)
                fh = open(args.output + str(movie) + '.mp4', 'wb')
                fh.write(base64.b64decode(demo_movie_base64))
                fh.close()
    except FileNotFoundError:
        print('Input file ´' + args.input + '´ not found.')


if __name__ == '__main__':
    main()
