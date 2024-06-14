def generate_sources(file):    
    # This script opens up the file and generates a sources list

    # History.csv was generated from Chrome Browser history from the period over which I did the assignment
    # Note: I pruned out personal and non-related sources 
    # This pruning was quite quick because we tend to have a daily pattern of when and what we access online
    # So I pruned out non-assignment links quickly using a spreadsheet.

    import pandas as pd

    # clean up the df
    
    df = pd.read_csv (file, skiprows=0, index_col=0)
    df.columns = ["order", "date","time","title","url","visitCount","typedCount","transition"]
    df.drop(["order", "typedCount", "transition"], axis=1, inplace=True)

    # the file was created using Google Sheets
    # Google Sheets will only export CSV with commas
    # Therefore I had to replace commas with REPLACE-THIS-PLEASE before exporting to CSV
    # I fix that now...

    df.replace({'REPLACE-THIS-PLEASE': ','}, inplace=True, regex=True)

    # drop duplicates

    df = df.drop_duplicates(subset=["url"], keep='first')
    df = df.drop_duplicates(subset=["title"], keep='first')

    # convert the column to numeric so I can query on it

    df['visitCount'] = pd.to_numeric(df['visitCount'])

    # Sort the list by the title

    df.sort_values(by=["title"], inplace=True)

    # list is outputed by order of the Page Title
    # List records access date, url, title, and web site (domain)

    # Not strictly academic references but does acknowledge / cite the sources used

    from IPython.core.display import display, HTML
    from datetime import datetime
    from urllib.parse import urlparse


    for index, row in df.iterrows():
        link = "Available at: <a href='" + str(row['url']) + "'>" + str(row['url']) + "</a>"

        accessDate = datetime.strptime(row['date'], '%m/%d/%Y')

        source = urlparse(row['url']).netloc

        title = "<b>" + str(row['title']) +"</b><br>"


        display(HTML("<b>" + title + "</b>"))
        display(HTML("<i>" + source + "</i>"))
        display(HTML(link))
        display(HTML("<p>Accessed on: " + accessDate.strftime("%d %B %Y") + "</p><br><br>"))