import sys
import mmdb_utils


if __name__ == "__main__":
    session_key = sys.stdin.readline().strip()
    try:
        mmdb_utils.MaxMindDatabaseUtil(session_key)
    except Exception as e:
        sys.stderr.write("Error: {}".format(e))
