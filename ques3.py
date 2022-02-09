import pymongo


def insert_comment():
    comment = dict()
    comment['name'] = input('Enter your name: ')
    comment['email'] = input('Enter your email: ')
    comment['text'] = input('Enter the text: ')
    comment['date'] = ''
    comment['movie_id'] = '5a9427648b0beebeb6958089'
    return comment


def insert_movie():
    movie = dict()
    movie['plot'] = input('Enter the plot: ')
    movie['genres'] = input('Enter the genres: ')
    movie['runtime'] = input('Enter the runtime: ')
    movie['cast'] = input('Enter the cast: ')
    movie['num_mflix_comments'] = ''
    movie['title'] = input('Enter the title: ')
    movie['fullplot'] = input('Enter the fullplot: ')
    movie['countries'] = input('Enter the countries: ')
    movie['released'] = ''
    movie['directors'] = input('Enter the directors: ')
    movie['rated'] = input('Enter the rated: ')
    movie['awards'] = input('Enter the awards: ')
    movie['lastupdated'] = ''
    movie['year'] = ''
    movie['imdb'] = input('Enter the imdb: ')
    movie['type'] = input('Enter the type: ')
    movie['tomatoes'] = input('Enter the tomatoes: ')
    return movie


def insert_theater():
    theater = dict()
    theater['theaterId'] = input('Enter the theaterId: ')
    theater['location'] = input('Enter the location: ')
    return theater


def insert_user():
    user = dict()
    user['name'] = input('Enter the name: ')
    user['email'] = input('Enter the email: ')
    user['password'] = input('Enter the password: ')
    return user


if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mflix_db = client['sample_mflix']
    comments = mflix_db['comments']
    movies = mflix_db['movies']
    theaters = mflix_db['theaters']
    users = mflix_db['users']

    print('Choose a collection to insert data:')
    print('\t a) Comments Collection')
    print('\t b) Movies Collection')
    print('\t c) Theaters Collection')
    print('\t d) Users Collection')
    print('Enter your choice(a/b/c): ')
    choice = input()
    while choice not in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']:
        print('Please choose a valid choice(a/b/c): ')
        choice = input()

    if choice == 'a':
        doc = insert_comment()
        comments.insert_one(doc)
        print('Comment Inserted!')
    elif choice == 'b':
        doc = insert_movie()
        movies.insert_one(doc)
        print('Movie Inserted!')
    elif choice == 'c':
        doc = insert_theater()
        theaters.insert_one(doc)
        print('Theatre inserted!')
    else:
        doc = insert_user()
        users.insert_one(doc)
        print('User inserted!')





