# Lab 07 — Comparable-Company Policy and Implied Range

## Question to Investigate

My DCF range changes mainly because of the growth, WACC, and terminal-growth assumptions. Before this lab, what I could not fully explain was why another company's P/E multiple should be applied to my target or how sensitive the result would be to removing one peer.

## What P/E Measures

Price-to-earnings, or P/E, is:

> **P/E = price per share / diluted earnings per share**

- **Price per share** measures what investors currently pay for one share of a company.
- **Diluted EPS** measures the GAAP profit attributable to each share after accounting for possible dilution.
- **P/E** shows how much investors are paying for each dollar of the company's earnings.

EPS puts companies of different sizes on a per-share basis, making their valuations easier to compare. A comparable-company valuation adds a market-based reference point to a DCF. The DCF estimates intrinsic value from cash flows and assumptions, while the P/E method shows how the market prices similar companies' earnings.

A lower P/E does **not** automatically mean a better investment. A company may deserve a lower multiple because it has slower expected growth, greater risk, weaker earnings quality, more cyclicality, or a less attractive business mix.

P/E is most useful when the companies have similar operations, growth, risk, accounting, capital needs, and earnings quality. It can mislead when earnings are negative or temporarily unusual, or when the companies have materially different growth prospects. Negative EPS does not produce a meaningful P/E comparison.

## Peer Policy

| Company | Decision | Reason |
|---|---|---|
| AutoNation (AN) | **Use** | AutoNation is a strong operating match because franchised vehicle retail and service/parts are central to its business, making its earnings reasonably comparable with Asbury's. |
| Group 1 Automotive (GPI) | **Qualify** | Group 1 has the same important franchised dealership and service/parts economics, so it is useful. However, its U.S./U.K. geographic footprint and major 2024 acquisition can make its growth and earnings less directly comparable. |
| Asbury Automotive (ABG) | **Exclude as a peer** | Asbury is the target. Including it would make the peer comparison circular. |

Both AN and GPI remain in the calculation. GPI is qualified rather than removed because its business model is still relevant, but its differences should be remembered when interpreting the result.

## Frozen Inputs

| Company | Role | 12/31/2024 Price | FY2024 GAAP Diluted EPS |
|---|---|---:|---:|
| Asbury Automotive (ABG) | Target | $243.03 | $21.50 |
| AutoNation (AN) | Peer | $169.84 | $16.92 |
| Group 1 Automotive (GPI) | Qualified peer | $421.48 | $36.81 |

## Calculation and Validation

The Python calculator produced:

| Check | Result |
|---|---:|
| AutoNation P/E | 10.037825x |
| Group 1 P/E | 11.450149x |
| Peer median P/E | 10.743987x |
| Asbury peer-implied range | $215.81-$246.18 |
| Asbury median-implied price | $231.00 |

The median P/E is the midpoint of the two peer multiples. Multiplying each peer multiple by Asbury's $21.50 diluted EPS produces the low and high values. Multiplying the median multiple by Asbury's EPS produces the $231.00 median-implied price.

## Changed-Peer Result

Before running the removal test, I predicted that removing GPI would lower the implied value because GPI has the higher P/E multiple.

After removing GPI, AutoNation is the only remaining peer:

- Remaining P/E: **10.037825x**
- Remaining implied price: **$215.81**
- Change from the full-peer estimate: **-$15.18**

The result falls because the higher GPI multiple is no longer included. With only AutoNation left, $215.81 is a **reference estimate rather than a range** because one observation cannot provide separate minimum, median, and maximum peer outcomes.

For completeness, removing AutoNation leaves only GPI. That produces a $246.18 reference estimate, which is **+$15.18** compared with the full-peer estimate.

## Interpretation

The comparison does not prove that Asbury is fairly valued. The $215.81-$246.18 range reflects the selected peers and one earnings measure at a specific point in time. It does not directly model Asbury's future cash flows, and the result would change if the peer policy, earnings period, or market prices changed. It should be used as a market cross-check alongside the DCF, not as a replacement for it.

Cash and debt are not added to or subtracted from this P/E result because both price and EPS are equity-level measures.

## Files and Run Command

- Calculator: `lab07_comps.py`
- Checkout: `lab07_checkout.md`

Run in the VS Code terminal with:

```bash
python lab07_comps.py
```

If the Windows terminal uses the Python launcher instead, run:

```bash
py lab07_comps.py
```

## Course Sources

- [Lab 07 — Comparable-Company Policy and Implied Range](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-04/lab-07-comparable-policy.md)
- [Worked Comparable-Company Example](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-04/teach-comps-worked-example.md)
