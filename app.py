import csv
import sys

import click
import containerlog

logger = containerlog.get_logger("magic")
containerlog.set_level(containerlog.INFO)


def lowest_temp(filepath: str):
    lowest = sys.maxsize
    pair = (lowest, lowest)

    with open(filepath) as f:
        reader = csv.reader(f, delimiter=",")
        line = 0
        for row in reader:
            if line == 0:
                line += 1
            else:
                temp = float(row[2])
                if temp < lowest:
                    lowest = temp
                    pair = (int(row[0]), float(row[1]))

                line += 1

    return pair


def most_fluctuation(filepath: str):
    m = {}

    dataset = remap(filepath)
    for k, v in dataset.items():
        m[k] = total_fluc_degree(v["temp"])

    return max(m, key=m.get)


def most_fluctuation_in_range(filepath: str, start: float, end: float):
    m = {}

    dataset = remap(filepath)
    for k, v in dataset.items():
        try:
            idx_start = v["date"].index(start)
            idx_end = v["date"].index(end)
            if idx_start < idx_end:
                m[k] = total_fluc_degree(v["temp"][idx_start:idx_end])
            else:
                continue

        except ValueError as e:
            logger.debug("failed to find indexes", error=e)
            continue

    try:
        return max(m, key=m.get)
    except ValueError as e:
        logger.debug("no date range found", error=e)
        return -1


def remap(filepath):
    m = {}

    with open(filepath) as f:
        reader = csv.reader(f, delimiter=",")
        line = 0
        for row in reader:
            if line == 0:
                line += 1
            else:
                station_id = int(row[0])
                if station_id not in m:
                    m[station_id] = {
                        "date": [],
                        "temp": [],
                    }

                m[station_id]["date"].append(float(row[1]))
                m[station_id]["temp"].append(float(row[2]))

                line += 1

    return m


def total_fluc_degree(values):
    if len(values) == 1:
        return values[0]

    total = 0
    p0, p1 = 0, 1
    while p1 < len(values):
        diff = abs(values[p1] - values[p0])
        total += diff
        p0 += 1
        p1 += 1

    return total


@click.command()
@click.option("--filepath", default="data.csv", help="Dataset filepath")
def run(filepath):
    station_id, date = lowest_temp(filepath)
    logger.info(f"Station #{station_id} reported the lowest temperature on {date}")

    station_id = most_fluctuation(filepath)
    logger.info(
        f"Station #{station_id} experienced the most amount of temperature fluctuation across all dates"
    )

    start_date = 2000.375
    end_date = 2001.375
    station_id = most_fluctuation_in_range(filepath, start_date, end_date)
    if station_id != -1:
        logger.info(
            f"Station #{station_id} experienced the most amount of temperature fluctuation for {start_date} to {end_date}"
        )
    else:
        logger.info(f"No station found for {start_date} to {end_date}")


if __name__ == "__main__":
    run()
