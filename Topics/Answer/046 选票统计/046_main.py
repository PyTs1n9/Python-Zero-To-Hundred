"""046 选票统计。"""


def count_votes(candidates, votes):
    """统计有效票、无效票和获胜者。"""
    result = {candidate: 0 for candidate in candidates}
    invalid = 0
    for vote in votes:
        if vote in result:
            result[vote] += 1
        else:
            invalid += 1

    highest = max(result.values())
    winners = [name for name in candidates if result[name] == highest]
    winner = winners[0] if len(winners) == 1 else winners
    return {"result": result, "invalid": invalid, "winner": winner}


if __name__ == "__main__":
    print(count_votes(["Alice", "Bob"], ["Bob", "Alice", "Bob", "Tom"]))
