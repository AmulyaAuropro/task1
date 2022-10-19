import requests
from pprint import pprint
username = "AmulyaAuropro"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint(user_data)

OUTPUT:
        {'avatar_url': 'https://avatars.githubusercontent.com/u/111051079?v=4',
 'bio': None,
 'blog': '',
 'company': None,
 'created_at': '2022-08-11T09:25:30Z',
 'email': None,
 'events_url': 'https://api.github.com/users/AmulyaAuropro/events{/privacy}',
 'followers': 0,
 'followers_url': 'https://api.github.com/users/AmulyaAuropro/followers',
 'following': 0,
 'following_url': 'https://api.github.com/users/AmulyaAuropro/following{/other
_user}',
 'gists_url': 'https://api.github.com/users/AmulyaAuropro/gists{/gist_id}',
 'gravatar_id': '',
 'hireable': None,
 'html_url': 'https://github.com/AmulyaAuropro',
 'id': 111051079,
 'location': None,
 'login': 'AmulyaAuropro',
 'name': None,
 'node_id': 'U_kgDOBp6BRw',
 'organizations_url': 'https://api.github.com/users/AmulyaAuropro/orgs',
 'public_gists': 0,
 'public_repos': 3,
 'received_events_url': 'https://api.github.com/users/AmulyaAuropro/received_e
vents',
 'repos_url': 'https://api.github.com/users/AmulyaAuropro/repos',
 'repos_url': 'https://api.github.com/users/AmulyaAuropro/repos',
 'site_admin': False,
 'starred_url': 'https://api.github.com/users/AmulyaAuropro/starred{/owner}{/repo}',
 'subscriptions_url': 'https://api.github.com/users/AmulyaAuropro/subscriptions',
 'twitter_username': None,
 'type': 'User',
 'updated_at': '2022-08-11T09:25:30Z',
 'url': 'https://api.github.com/users/AmulyaAuropro'}




{
  "login": "AmulyaAuropro",
  "id": 111051079,
  "node_id": "U_kgDOBp6BRw",
  "avatar_url": "https://avatars.githubusercontent.com/u/111051079?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/AmulyaAuropro",
  "html_url": "https://github.com/AmulyaAuropro",
  "followers_url": "https://api.github.com/users/AmulyaAuropro/followers",
  "following_url": "https://api.github.com/users/AmulyaAuropro/following{/other_user}",
  "gists_url": "https://api.github.com/users/AmulyaAuropro/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/AmulyaAuropro/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/AmulyaAuropro/subscriptions",
  "organizations_url": "https://api.github.com/users/AmulyaAuropro/orgs",
  "repos_url": "https://api.github.com/users/AmulyaAuropro/repos",
  "events_url": "https://api.github.com/users/AmulyaAuropro/events{/privacy}",
  "received_events_url": "https://api.github.com/users/AmulyaAuropro/received_events",
  "type": "User",
  "site_admin": false,
  "name": null,
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": null,
  "twitter_username": null,
  "public_repos": 3,
  "public_gists": 0,
  "followers": 0,
  "following": 0,
  "created_at": "2022-08-11T09:25:30Z",
  "updated_at": "2022-08-11T09:25:30Z"
}
