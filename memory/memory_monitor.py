import psutil
import argparse
import time
import datetime


def memory_monitor(pid, out):
    with open(out, "w") as output:
        while True:
            proc = psutil.Process(pid)
            rss, vm = proc.memory_info()
            output.write(str(datetime.datetime.now()) + "; " +
                         str(rss / 1024 / 1024) + "; " +
                         str(vm / 1024 / 1024) + "\n")

            output.flush()
            time.sleep(60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Memory monitor tool')
    parser.add_argument('-p', dest='pid', type=int,
                        help='Process pid', required=True)
    parser.add_argument('-o', dest='output', type=str,
                        help='Output file', required=True)

    args = parser.parse_args()

    memory_monitor(args.pid, args.output)