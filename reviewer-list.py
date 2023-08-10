'''
Copyright (C) 2023 Mo Zhou <cdluminate@gmail.com>
MIT/Expat License

This script will automatically generate HTML code for the list of reviewers.
Usage:
    1. Go to the CMT Chair console. Click Users -> Reviewer -> Manage (more ...)
    2. Click Actions -> Export -> Reviewers. Get the txt file (in fact a tsv file)
    3. `python3 <this_file> <the_tsv_file>`
    4. Copy the generated HTML code.
'''
import pandas as pd
import argparse
import rich
console = rich.get_console()

if __name__ == '__main__':
    ag = argparse.ArgumentParser()
    ag.add_argument('tsv', type=str,
                    help='path to exported reviewer list')
    ag = ag.parse_args()

    df = pd.read_csv(ag.tsv, sep='\t')
    console.print(df)

    console.print("<div class='text-center container lead'>")
    console.print("<ul>")
    for i in range(len(df)):
        first_name = df.loc[i, 'First Name']
        last_name = df.loc[i, 'Last Name']
        organization = df.loc[i, 'Organization']
        completed = df.loc[i, 'Completed']
        if completed < 1:
            continue
        console.print(f'<li>{first_name} {last_name} ({organization})</li>')
    console.print("</ul>")
    console.print("</div>")
