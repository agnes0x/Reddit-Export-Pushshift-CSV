# Reddit Data Analysis 

## Intro
Export your selected subreddits from [Pushshift's archive of Reddit](https://files.pushshift.io/reddit/) into dataframes as well as .csv outputs

The resulting dataset is rich in detail and can also be aggregated on the minute-level, which is why it's such a popular datasource in various fields of research.

### Use cases
There's a wide range of use cases: Use [sentiment analysis](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=reddit+sentiment+analysis&btnG=&oq=reddit+) to [uncover social or political attitudes](https://scholar.google.com/scholar?hl=en&as_sdt=2005&sciodt=0%2C5&cites=7671696188192149307&scipsc=1&q=reddit+social+politics&btnG=) or build [stock or crypto trading algorithms](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=reddit+stock+prediction&btnG=). Discover pain points & unmet needs to tackle as a sartup, similar to how [symptoms of long Covid were mined](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=long+covid+symptoms+reddit&btnG=). For more inspiration search among articles citing [PushShift's service.](https://scholar.google.com/scholar?hl=en&as_sdt=2005&sciodt=0%2C5&cites=7671696188192149307&scipsc=1&q=reddit&btnG=)

## Getting Started
You'll need python, plenty of storage space and ~~patience~~ time.   

### Download
Download the .zst compressed JSON files of:

[comments](https://files.pushshift.io/reddit/comments)

[posts](https://files.pushshift.io/reddit/submissions)

### Extract subreddits
Within Parse_Reddit.py, update [this line](https://github.com/agnes0x/Reddit-Export-Pushshift-CSV/blob/aa699a23a4604a9c6843596f5178f582d2d8fa36/Parse_Reddit.py#L20) with your download's filename, and add the case-sensitive name of selected subreddits to [this line](https://github.com/agnes0x/Reddit-Export-Pushshift-CSV/blob/32a15d82fb6a8de8a1f335c0f78f32b0c67ddfe9/Parse_Reddit.py#L13). Run the code & it will generate separate .csv for each subreddit. 

Be patient! Processing the newest 30GB monthly comment datatumps may take between 1-2hrs depending on your setup. 

### Processing data 
Prepare the extracted data for analysis e.g. drop unnecessary columns.

### Aggregate data
