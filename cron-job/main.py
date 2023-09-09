from time import sleep


def main():
    sleep(5)


if '__main__' == __name__:
    print("CRON JOB START")
    main()
    print("CRON JOB END")
