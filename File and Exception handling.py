import logging
import csv

logging.basicConfig(
    level=logging.DEBUG,
    filename=r"C:\Users\kolla\Downloads\app.log",   # log file not csv!
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def studentrecval(csv_path):

    logging.info("program started")
    valid_record   = []
    invalid_record = []

    # ── open file ──────────────────────────────
    try:
        with open(csv_path, "r", encoding="utf-8") as f:  # fix 1
            reader = csv.DictReader(f)
            rows   = list(reader)                          # fix 2 and 3
        logging.info(f"loaded {len(rows)} rows from {csv_path}")

    except FileNotFoundError:
        logging.error(f"file not found: {csv_path}")
        return
    except PermissionError:
        logging.critical(f"no permission to read: {csv_path}")
        return

    # ── loop through rows ──────────────────────
    for row in rows:
        logging.debug(f"processing row: {row}")

        # check name
        name = row.get("name", "").strip()
        if not name:
            logging.warning(f"row has no name — skipping: {row}")  # fix 4
            invalid_record.append(row)
            continue

        # check score is a number
        try:                                               # fix 5
            score = int(row.get("score", ""))
        except ValueError:
            logging.error(f"invalid score for {name} — skipping")
            invalid_record.append(row)
            continue

        # check score is in range
        if not 0 <= score <= 100:                         # fix 6
            logging.warning(f"{name} score {score} out of range — skipping")
            invalid_record.append(row)
            continue

        # all checks passed — save valid record
        valid_record.append({"name": name, "score": score})  # fix 7
        logging.info(f"valid record saved — {name}: {score}")

    # ── final report ───────────────────────────
    total   = len(rows)
    valid   = len(valid_record)
    invalid = len(invalid_record)

    logging.info(f"REPORT: total={total} valid={valid} invalid={invalid}")

    print(f"\n── Final Report ──")
    print(f"total records  : {total}")
    print(f"valid records  : {valid}")
    print(f"invalid records: {invalid}")
    print(f"see app.log for full details")


studentrecval(r"C:\Users\kolla\Downloads\students.csv")
