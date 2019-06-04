import os
BASE_DIR = os.path.dirname(__file__)
MOVIE_DIR = os.path.join(BASE_DIR,'视频')
print(MOVIE_DIR)
# os.path.join()
print(os.listdir(MOVIE_DIR))
movie_list = os.listdir(MOVIE_DIR)
for i,m in enumerate(movie_list):
    print(i+1,m)
choice = input('please choice movie number to upload>>>:')
if choice.isdigit():
    choice = int(choice)
    if choice in range(1,len(movie_list)+1):
        movie_path = os.path.join(MOVIE_DIR,movie_list[choice-1])
        print(movie_path)