import pandas as pd

from explorers import (
    pathfinder,
    architect,
)
from analysts import (
    analyst,
    technical,
    speed,
    memory,
    content,
    security
)

# * difference between explorers and analysts:
# * analysts are page by page
# * explorers are domain wide

def call_explorer(choice, url, filename):

    if choice == "pathfinder":
        finder = pathfinder.Pathfinder(url)
        data = finder.explore()

        df = pd.Series(data=data, name="url")
        filename = "storage/explorers/{}.csv".format(filename)
        df.to_csv(filename)

    elif choice == "architect":
        archy = architect.Architect()
        headers = ["robots","favicons","discover","sitemaps","json_ld","open_graph"]
        data = {}

        # Simplified some of the array results to transpose into df
        # Robots
        robots = archy.robots(url)
        if robots:
            data["robots"] = True
        else:
            data["robots"] = False

        data["favicons"] = archy.favicons(url)
        data["discover"] = archy.discover(url)
        data["sitemaps"] = archy.sitemaps(url)
        data["json_ld"] = archy.json_ld(url)
        data["open_graph"] = archy.open_graph(url)

        df = pd.DataFrame.from_dict(data = data, orient="index")
        filename = "storage/explorers/{}.csv".format(filename)
        df.to_csv(filename)

def call_analyst(source, filename, choice):

    # Recall and read csv
    df = pd.read_csv("storage/explorers/"+source+".csv")
    urls = df["url"].tolist()

    # Set up analyst
    _featheranalyst = analyst.FeatherAnalyst()

    if choice == "speed":
        speedAnalyst = speed.Speed(_featheranalyst)
        headers = ["front_end", "back_end"]
        data = {}
        for url in urls:
            front_end = speedAnalyst.front_end(url)
            back_end = speedAnalyst.back_end(url)
            data[url] = [front_end,back_end]

    elif choice == "memory":
        memAnalyst = memory.Memory(_featheranalyst)
        headers = ["size"]
        data = {}
        for url in urls:
            data[url] = memAnalyst.size(url)

    elif choice == "technical":
        techAnalyst = technical.Technical()
        headers = ["robots","json_ld","open_graph","canonical","social_tags"]
        data = {}
        for url in urls:
            row = []
            row.append(techAnalyst.robots(url))
            row.append(techAnalyst.json_ld(url))
            row.append(techAnalyst.open_graph(url))
            row.append(techAnalyst.canonical(url))
            row.append(techAnalyst.social_tags(url))
            data[url] = row

    elif choice == "content":
            contentAnalyst = content.Content()
            headers = ["slug","hreflang","byline","title","desc","images","videos"]
            data = {}
            for url in urls:
                row = []
                row.append(contentAnalyst.slug(url))
                row.append(contentAnalyst.lang(url))
                row.append(contentAnalyst.byline(url))
                row.append(contentAnalyst.title(url))
                row.append(contentAnalyst.desc(url))
                row.append(contentAnalyst.images(url))
                row.append(contentAnalyst.videos(url))
                data[url] = row

    df = pd.DataFrame.from_dict(data = data, orient="index", columns=headers)
    filename = "storage/analysts/{}.csv".format(filename)
    df.to_csv(filename)
    
def run():

    services = ["Explorer","Analyst"]
    explorers = ["Pathfinder","Architect"]
    analysts = ["Technical","Content","Speed","Memory","Security"]

    print("""
    Welcome Mr. de Villiers
    ***********************
    """)
    for service in services:
        print("*",service)

    service = input("Service: ").lower()

    while service != "quit":
        print("\n")
        if service == "explorer":
            for explorer in explorers:
                print("*",explorer)
            explorer = input("Explorer: ").lower()
            url = input("URL: ")
            filename = input("Filename: ")

            # Call and save
            call_explorer(explorer, url, filename)
            print("Saved in storage as: ", filename+".csv")

        elif service == "analyst":
            for analyst in analysts:
                print("*",analyst)
            
            # Selection
            analyst = input("Analyst: ").lower()
            source = input("Source: ").lower()
            filename = input("Filename: ").lower()

            call_analyst(source,filename,analyst)
            print("Saved in storage as: ", filename+".csv")
                
        service = input("Service: ")

if __name__ == "__main__":
    run()