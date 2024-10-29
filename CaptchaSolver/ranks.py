ranks_rates: dict[str, float] = {           # rank = rate per captcha
    'unranked': 0.0005,
    'bronze': 0.001,
    'silver': 0.0012,
    'gold': 0.0015,
    'platinum': 0.002,
    'diamond': 0.0025,
    'master': 0.004
}

ranks_points: dict[str, int] = {            # required points for rank
    'unranked': 0,
    'bronze': 1,
    'silver': 2,
    'gold': 3,
    'platinum': 4,
    'diamond': 5,
    'master': 6
}