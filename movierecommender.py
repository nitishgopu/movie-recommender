
import urllib
import os
import zipfile
import pandas as pd

# Downloading the Dataset and saving to Directory

moviedataset_url = "http://files.grouplens.org/datasets/movielens/ml-latest.zip"

cur_path = os.getcwd()

dataset_path = os.path.join(cur_path,'datasets')

os.chdir(dataset_path)

if os.path.exists('data.zip'):
    print "Dataset already exists"
else:
    dataset = urllib.urlretrieve(moviedataset_url, dataset_path+'/data.zip')

data_path = os.path.join(dataset_path,'data.zip')


if os.path.exists('ml-latest'):
    print "Extraction Done"
else:
    with zipfile.ZipFile(data_path, "r") as z:
        z.extractall(dataset_path)

#Get path of extracted data
all_data_path = os.path.join(dataset_path,'ml-latest')


#Read all CSV Files

ratings_file_csv = os.path.join(all_data_path,'ratings.csv')
movies_file_csv = os.path.join(all_data_path, 'movies.csv')
tags_file_csv = os.path.join(all_data_path, 'tags.csv')
links_file_csv = os.path.join(all_data_path, 'links.csv')
genome_tags_csv = os.path.join(all_data_path, 'genome-tags.csv')
genome_scores_csv = os.path.join(all_data_path, 'genome-scores.csv')



df_ratings = pd.read_csv(ratings_file_csv)
df_movies = pd.read_csv(movies_file_csv)
df_tags = pd.read_csv(tags_file_csv)
df_links = pd.read_csv(links_file_csv)
pd.set_option('display.max_columns', 5)
print df_ratings.head()
print df_movies.head()
print df_tags.head()
print df_links.head()




#dataset = urllib.urlretrieve(moviedataset_url, '/Users/gopu/Desktop/datasets/dataset.zip')

#print type(dataset)