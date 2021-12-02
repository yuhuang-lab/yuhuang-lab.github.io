#This script read in a list of repos of interest (from the repo_file
#input), then for each repo,dump the json obj of it and get all its contributors and their info,
#finally output contirbutors' info into the output file.

# NOTE:
# https://api.github.com/repos/democracyworks/voting-method-works
# https://api.github.com/erpos/opendatateam/croquemort
#https://api.github.com/repos/Project-AsTeR/*
# no longer exists

import requests, json
import os
from pprint import pprint
import csv
import sys
import time


#read in the repo list
#repo_file = "./ovio-covid19-projects.csv"
#repo_file = "./ovio-all-projects-6.csv"
#outpath = "./ovio-covid19-contributors/"
#outpath = "./ovio-all-contributors/"
repo_file = sys.argv[1]
outpath = sys.argv[2]
ID = sys.argv[3]
PW = sys.argv[4]

my_reader = csv.DictReader(open(repo_file))

repo_list = []
for row in my_reader:
    repo_name_with_owner = row["repo_name_with_owner"] # e.g., "reach4help/reach4help"
    repo_list.append(repo_name_with_owner)
 

def main():
    with open("./repo_contributors_count.csv", 'w') as of:
        # get each repo api url
        for repo_name in repo_list:
            url = "https://api.github.com/repos/"+ repo_name
            repo_req = requests.get(url, auth = (ID, PW))
            repo = repo_req.json()
            with open('./repo-json/'+repo_name.replace('/','_')+'.json','w') as out:
                json.dump(repo,out)
                time.sleep(1)

            contributor_url = url+'/contributors'
            req = requests.get(contributor_url, auth = (ID, PW))
            time.sleep(1)

            contributors = req.json() # contributors is a list of json files, each elelment is a json object that represents a contributor
            num_contributors = len(contributors)
            of.write(repo_name+', '+ str(num_contributors)+"\n")

            
            outfile = outpath+repo_name.replace('/','_')+".csv"
            my_writer = csv.writer(open(outfile, 'w'))
            header_line = ['name', 'u_name', 'email', 'url', 'contributions', 'location', 'company', 'public_repos', 'followers', 'following', 'bio']
            my_writer.writerow(header_line)

            print("REPO:"+repo_name) 
            print("c-url:"+contributor_url) 
            #pprint(contributors)
            for c in contributors:
                #print(c)
                try:
                    c_uname = c["login"]
                    c_name, c_email = get_u_info(c)
                    c_num_contribution = c["contributions"]
                    c_uname = c["login"]
                    c_url = "https://api.github.com/users/"+c_uname
                    c_website_req = requests.get(c_url, auth = (ID, PW))
                    c_jobj = c_website_req.json()
                    c_company = c_jobj["company"]
                    c_location = c_jobj["location"]
                    c_bio = c_jobj["bio"]
                    c_num_pub_repos = c_jobj["public_repos"]
                    c_num_followers = c_jobj["followers"]
                    c_num_following = c_jobj["following"]

                    line = [c_name, c_uname, c_email, c_url, c_num_contribution, c_location, c_company, c_num_pub_repos, c_num_followers, c_num_following, c_bio]

                    my_writer.writerow(line)
                except TypeError:
                    continue


def get_u_info(c): # c is a contributor json obj
    c_uname = c["login"]
    event_url = "https://api.github.com/users/"+c_uname+'/events/public'
    event_req = requests.get(event_url, auth = (ID, PW))
    time.sleep(3)
    events = event_req.json()
    #pprint(events)
    email = ""
    name = ""
    #print("!!!!!!!UNAME:"+c_uname)
    for event in events:
        try:
            email = event['payload']['commits'][0]['author']['email'] 
            name = event['payload']['commits'][0]['author']['name'] 
            if email != '' and name != '':
                print(email)
                print(name)
                break
        except (KeyError, IndexError) as e:
            continue
    return [name, email]

if __name__ == '__main__':
    main()
