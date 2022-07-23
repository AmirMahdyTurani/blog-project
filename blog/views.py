from django.shortcuts import render
from datetime import date

# Create your views here.

posts_data = [
    {
        'title': 'learning django',
        'slug': 'learning-django',
        'author': 'AmirMahdy',
        'date': date(2022, 4, 3),
        'image': 'django.png',
        'short_description': 'Learning django on AmirMahdy blog.',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae consectetur cum, inventore minima molestiae
            placeat quod recusandae, repellendus reprehenderit sapiente sequi tempore voluptatum. Architecto at aut
            commodi deleniti deserunt dolores esse fuga illo labore, laboriosam, magnam quaerat recusandae repudiandae
            sit velit! Alias aliquam odio repellendus. Architecto, aut cupiditate dicta inventore non qui quos
            recusandae similique sint sit, ullam veniam. A alias asperiores autem beatae cumque deserunt ea earum fugiat
            ipsa nam praesentium quidem quisquam quos reprehenderit temporibus voluptas, voluptatibus! Ad amet
            asperiores assumenda, eaque eligendi esse facilis id impedit, minus, molestiae nesciunt nihil odit officia
            provident quibusdam quis rem repellat sunt tempora veniam. Beatae consectetur corporis deleniti, expedita
            ipsum modi natus odio? Aliquid amet animi, blanditiis commodi consequuntur deserunt dignissimos iste, magnam
            nemo omnis, placeat porro quaerat reprehenderit? Accusamus, animi, dicta et hic laboriosam laudantium magni
            molestiae necessitatibus officia praesentium provident quo ratione, recusandae suscipit vel. Architecto
            dolores iste quibusdam!
        """,
    },
    {
        'title': 'learning python',
        'slug': 'learning-python',
        'author': 'AmirMahdy',
        'date': date(2020, 4, 1),
        'image': 'python.png',
        'short_description': 'Learning python on AmirMahdy blog.',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae consectetur cum, inventore minima molestiae
            placeat quod recusandae, repellendus reprehenderit sapiente sequi tempore voluptatum. Architecto at aut
            commodi deleniti deserunt dolores esse fuga illo labore, laboriosam, magnam quaerat recusandae repudiandae
            sit velit! Alias aliquam odio repellendus. Architecto, aut cupiditate dicta inventore non qui quos
            recusandae similique sint sit, ullam veniam. A alias asperiores autem beatae cumque deserunt ea earum fugiat
            ipsa nam praesentium quidem quisquam quos reprehenderit temporibus voluptas, voluptatibus! Ad amet
            asperiores assumenda, eaque eligendi esse facilis id impedit, minus, molestiae nesciunt nihil odit officia
            provident quibusdam quis rem repellat sunt tempora veniam. Beatae consectetur corporis deleniti, expedita
            ipsum modi natus odio? Aliquid amet animi, blanditiis commodi consequuntur deserunt dignissimos iste, magnam
            nemo omnis, placeat porro quaerat reprehenderit? Accusamus, animi, dicta et hic laboriosam laudantium magni
            molestiae necessitatibus officia praesentium provident quo ratione, recusandae suscipit vel. Architecto
            dolores iste quibusdam!
        """,
    },
    {
        'title': 'learning ml',
        'slug': 'learning-ml',
        'author': 'AmirMahdy',
        'date': date(2020, 4, 2),
        'image': 'ml.png',
        'short_description': 'Learning ml on AmirMahdy blog.',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae consectetur cum, inventore minima molestiae
            placeat quod recusandae, repellendus reprehenderit sapiente sequi tempore voluptatum. Architecto at aut
            commodi deleniti deserunt dolores esse fuga illo labore, laboriosam, magnam quaerat recusandae repudiandae
            sit velit! Alias aliquam odio repellendus. Architecto, aut cupiditate dicta inventore non qui quos
            recusandae similique sint sit, ullam veniam. A alias asperiores autem beatae cumque deserunt ea earum fugiat
            ipsa nam praesentium quidem quisquam quos reprehenderit temporibus voluptas, voluptatibus! Ad amet
            asperiores assumenda, eaque eligendi esse facilis id impedit, minus, molestiae nesciunt nihil odit officia
            provident quibusdam quis rem repellat sunt tempora veniam. Beatae consectetur corporis deleniti, expedita
            ipsum modi natus odio? Aliquid amet animi, blanditiis commodi consequuntur deserunt dignissimos iste, magnam
            nemo omnis, placeat porro quaerat reprehenderit? Accusamus, animi, dicta et hic laboriosam laudantium magni
            molestiae necessitatibus officia praesentium provident quo ratione, recusandae suscipit vel. Architecto
            dolores iste quibusdam!
        """,
    },
{
        'title': 'learning django',
        'slug': 'learning-django',
    'author': 'AmirMahdy',
        'date': date(2020, 6, 3),
        'image': 'django.png',
        'short_description': 'Learning django on AmirMahdy blog.',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae consectetur cum, inventore minima molestiae
            placeat quod recusandae, repellendus reprehenderit sapiente sequi tempore voluptatum. Architecto at aut
            commodi deleniti deserunt dolores esse fuga illo labore, laboriosam, magnam quaerat recusandae repudiandae
            sit velit! Alias aliquam odio repellendus. Architecto, aut cupiditate dicta inventore non qui quos
            recusandae similique sint sit, ullam veniam. A alias asperiores autem beatae cumque deserunt ea earum fugiat
            ipsa nam praesentium quidem quisquam quos reprehenderit temporibus voluptas, voluptatibus! Ad amet
            asperiores assumenda, eaque eligendi esse facilis id impedit, minus, molestiae nesciunt nihil odit officia
            provident quibusdam quis rem repellat sunt tempora veniam. Beatae consectetur corporis deleniti, expedita
            ipsum modi natus odio? Aliquid amet animi, blanditiis commodi consequuntur deserunt dignissimos iste, magnam
            nemo omnis, placeat porro quaerat reprehenderit? Accusamus, animi, dicta et hic laboriosam laudantium magni
            molestiae necessitatibus officia praesentium provident quo ratione, recusandae suscipit vel. Architecto
            dolores iste quibusdam!
        """,
    },
    {
        'title': 'learning python',
        'slug': 'learning-python',
        'author': 'AmirMahdy',
        'date': date(2021, 4, 1),
        'image': 'python.png',
        'short_description': 'Learning python on AmirMahdy blog.',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae consectetur cum, inventore minima molestiae
            placeat quod recusandae, repellendus reprehenderit sapiente sequi tempore voluptatum. Architecto at aut
            commodi deleniti deserunt dolores esse fuga illo labore, laboriosam, magnam quaerat recusandae repudiandae
            sit velit! Alias aliquam odio repellendus. Architecto, aut cupiditate dicta inventore non qui quos
            recusandae similique sint sit, ullam veniam. A alias asperiores autem beatae cumque deserunt ea earum fugiat
            ipsa nam praesentium quidem quisquam quos reprehenderit temporibus voluptas, voluptatibus! Ad amet
            asperiores assumenda, eaque eligendi esse facilis id impedit, minus, molestiae nesciunt nihil odit officia
            provident quibusdam quis rem repellat sunt tempora veniam. Beatae consectetur corporis deleniti, expedita
            ipsum modi natus odio? Aliquid amet animi, blanditiis commodi consequuntur deserunt dignissimos iste, magnam
            nemo omnis, placeat porro quaerat reprehenderit? Accusamus, animi, dicta et hic laboriosam laudantium magni
            molestiae necessitatibus officia praesentium provident quo ratione, recusandae suscipit vel. Architecto
            dolores iste quibusdam!
        """,
    },
    {
        'title': 'learning ml',
        'slug': 'learning-ml',
        'author': 'AmirMahdy',
        'date': date(2020, 5, 2),
        'image': 'ml.png',
        'short_description': 'Learning ml on AmirMahdy blog.',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae consectetur cum, inventore minima molestiae
            placeat quod recusandae, repellendus reprehenderit sapiente sequi tempore voluptatum. Architecto at aut
            commodi deleniti deserunt dolores esse fuga illo labore, laboriosam, magnam quaerat recusandae repudiandae
            sit velit! Alias aliquam odio repellendus. Architecto, aut cupiditate dicta inventore non qui quos
            recusandae similique sint sit, ullam veniam. A alias asperiores autem beatae cumque deserunt ea earum fugiat
            ipsa nam praesentium quidem quisquam quos reprehenderit temporibus voluptas, voluptatibus! Ad amet
            asperiores assumenda, eaque eligendi esse facilis id impedit, minus, molestiae nesciunt nihil odit officia
            provident quibusdam quis rem repellat sunt tempora veniam. Beatae consectetur corporis deleniti, expedita
            ipsum modi natus odio? Aliquid amet animi, blanditiis commodi consequuntur deserunt dignissimos iste, magnam
            nemo omnis, placeat porro quaerat reprehenderit? Accusamus, animi, dicta et hic laboriosam laudantium magni
            molestiae necessitatibus officia praesentium provident quo ratione, recusandae suscipit vel. Architecto
            dolores iste quibusdam!
        """,
    },
]


def get_date(epost):
    return epost['date']


def index(request):
    sorted_posts = sorted(posts_data, key=get_date)
    latest_posts = reversed(sorted_posts[-3:])
    return render(request, 'blog/index.html', {
        'latest_posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'posts_data': posts_data,
    })


def post(request, slug):
    post = next(post for post in posts_data if post["slug"] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post,
    })
