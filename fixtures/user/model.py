from attrs import define


@define
class UserModel:
    login: str
    name: str
    id: int
    location: str
    public_repos: int
    public_gists: int
    followers: int
    following: int
