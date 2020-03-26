

def extract_title(titles):
    title = []
    for line in titles:
        title.append(line.text)
    return title


def extract_rank(ranks):
    rank = []
    for line in ranks:
        rank.append(line.text[0:-1])
    return rank


def extract_score_comments(subtext):
    score = []
    comments = []
    for line in subtext:
        if 'points' in line.text:
            score.append(int(line.text.split(' ')[0][1:]))
        else:
            score.append(None)
        if 'comments' in line.text:
            comments.append(int(line.text.split(' ')[-2].split('\xa0')[0]))
        else:
            comments.append(None)
    return score, comments
