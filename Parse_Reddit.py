import zstandard as zstd
import  json
import pandas as pd
from datetime import datetime

# reads in zst files downloaded from https://files.pushshift.io/reddit/comments/
# only retains data for subreddits I specify: eg. ('wallstreetbets', 'dogecoin')
# from the json, creates a separate dataframe for each specified subreddit
# writes out dataframe as .csv


def main():
    subreddits = ['dogelon', 'dogecoin']

    filtered_subreddits = {}

    for subreddit  in subreddits:
        filtered_subreddits.update({subreddit : []})

    your_filename = "RC_2021-06.zst"

    print(f"Extracting from {your_filename}...")
    with open(your_filename, 'rb') as fh:
        dctx = zstd.ZstdDecompressor(max_window_size=2147483648)
        with dctx.stream_reader(fh) as reader:
            previous_line = ""
            while True:
                chunk = reader.read(2**24)  # 16mb chunks
                if not chunk:
                    break

                string_data = chunk.decode('utf-8')
                lines = string_data.split("\n")
                for i, line in enumerate(lines[:-1]):
                    if i == 0:
                        line = previous_line + line
                    object = json.loads(line)

                    subreddit = object['subreddit']
                    if subreddit.lower() in subreddits:
                        filtered_subreddits.get(subreddit).append(object)
                        # filtered_subreddits.append(object)

                previous_line = lines[-1]

    
    for key, obj_list in filtered_subreddits.items():
        df = pd.DataFrame(obj_list)
        df.to_csv(f"{key}.csv", index=False)


if __name__ == '__main__':
    main()
    