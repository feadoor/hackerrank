def best_teams(contestants):
    topics_count, teams_count = 0, 0
    for (ix, contestant_1) in enumerate(contestants):
        for contestant_2 in contestants[ix + 1::]:
            topics = bin(contestant_1 | contestant_2).count("1")
            if topics > topics_count:
                topics_count, teams_count = topics, 1
            elif topics == topics_count:
                teams_count += 1
    return topics_count, teams_count

def read_binary_integer():
    return int(raw_input(), 2)

def main():
    n_contestants, _ = map(int, raw_input().strip().split(' '))
    contestants = [read_binary_integer() for _ in xrange(n_contestants)]
    topics, teams = best_teams(contestants)
    print topics
    print teams

if __name__ == "__main__":
    main()