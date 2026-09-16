"""Lab 07: Comparable-Company P/E Analysis (standard library only)."""

from statistics import median


# -------------------- EDITABLE INPUTS --------------------
target = {
    "ticker": "ABG",
    "company": "Asbury Automotive",
    "price": 243.03,
    "diluted_eps": 21.50,
}

peers = [
    {
        "ticker": "AN",
        "company": "AutoNation",
        "price": 169.84,
        "diluted_eps": 16.92,
    },
    {
        "ticker": "GPI",
        "company": "Group 1 Automotive",
        "price": 421.48,
        "diluted_eps": 36.81,
    },
]
# ---------------------------------------------------------


def positive_number(value):
    """Return True only for a positive int or float."""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def clean_ticker(value):
    """Standardize a ticker so duplicates can be detected."""
    return str(value).strip().upper()


def usable_peers(target_data, peer_data):
    """Exclude the target, duplicates, and peers without meaningful P/E inputs."""
    target_ticker = clean_ticker(target_data.get("ticker", ""))
    seen = set()
    valid = []

    for peer in peer_data:
        ticker = clean_ticker(peer.get("ticker", ""))

        if not ticker:
            print("Excluded peer with missing ticker.")
        elif ticker == target_ticker:
            print(f"Excluded {ticker}: the target cannot be its own peer.")
        elif ticker in seen:
            print(f"Excluded duplicate peer: {ticker}.")
        else:
            seen.add(ticker)
            price = peer.get("price")
            eps = peer.get("diluted_eps")

            if not positive_number(price) or not positive_number(eps):
                print(f"{ticker} P/E: not meaningful (price and EPS must be positive).")
            else:
                valid.append({**peer, "ticker": ticker, "pe": price / eps})

    return valid


def print_implied_prices(valid, target_eps):
    """Print the full-peer result and return its unrounded median-implied price."""
    if not positive_number(target_eps):
        print("Implied prices: not meaningful (target EPS must be positive).")
        return None

    if not valid:
        print("No usable peers; no estimate.")
        return None

    multiples = [peer["pe"] for peer in valid]
    median_pe = median(multiples)
    median_price = median_pe * target_eps

    print(f"Peer median P/E: {median_pe:.6f}x")

    if len(valid) == 1:
        print(f"Reference estimate: ${median_price:.2f} (one valid peer; no range)")
    else:
        minimum_price = min(multiples) * target_eps
        maximum_price = max(multiples) * target_eps
        print(f"Implied price range: ${minimum_price:.2f}-${maximum_price:.2f}")
        print(f"Median-implied price: ${median_price:.2f}")

    return median_price


def print_leave_one_out(valid, target_eps, full_median_price):
    """Remove each peer once and compare the new estimate with the full-peer estimate."""
    print("\nLEAVE-ONE-OUT RESULTS")

    if full_median_price is None or not positive_number(target_eps):
        print("Leave-one-out calculations: not meaningful.")
        return

    for removed_peer in valid:
        remaining = [peer for peer in valid if peer is not removed_peer]
        print(f"Remove {removed_peer['ticker']}:")

        if not remaining:
            print("  No peers remain; no estimate.")
            continue

        remaining_median_pe = median(peer["pe"] for peer in remaining)
        remaining_price = remaining_median_pe * target_eps
        change = remaining_price - full_median_price

        print(f"  Remaining median P/E: {remaining_median_pe:.6f}x")
        print(f"  Remaining median-implied price: ${remaining_price:.2f}")
        print(f"  Change from full-peer estimate: {change:+.2f}")

        if len(remaining) == 1:
            print("  One valid peer remains: reference estimate, no range.")


def main():
    target_ticker = clean_ticker(target.get("ticker", ""))
    target_price = target.get("price")
    target_eps = target.get("diluted_eps")

    print("LAB 07 - COMPARABLE-COMPANY P/E ANALYSIS")
    print(f"Target: {target.get('company', '')} ({target_ticker})")

    if positive_number(target_price) and positive_number(target_eps):
        print(f"Target current P/E: {target_price / target_eps:.6f}x")
    else:
        print("Target current P/E: not meaningful (price and EPS must be positive).")

    print("\nVALID PEER MULTIPLES")
    valid = usable_peers(target, peers)

    for peer in valid:
        print(f"{peer['company']} ({peer['ticker']}): {peer['pe']:.6f}x")

    print("\nFULL-PEER RESULT")
    full_median_price = print_implied_prices(valid, target_eps)
    print_leave_one_out(valid, target_eps, full_median_price)


if __name__ == "__main__":
    main()
