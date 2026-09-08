# DCF INPUTS
starting_fcff = 100
growth_rates = [0.08, 0.06, 0.05, 0.04, 0.03]
wacc = 0.10
terminal_growth = 0.03
cash = 50
debt = 300
shares = 50

# Check terminal growth
if terminal_growth >= wacc:
    raise SystemExit("Error: Terminal growth must be less than WACC.")

# Forecast FCFF for Years 1-5
fcff = []
current_fcff = starting_fcff

for growth in growth_rates:
    current_fcff = current_fcff * (1 + growth)
    fcff.append(current_fcff)

# Present value of Years 1-5 FCFF
pv_explicit = 0

for year, cash_flow in enumerate(fcff, start=1):
    pv_explicit += cash_flow / ((1 + wacc) ** year)

# Terminal value at end of Year 5
terminal_value = (
    fcff[-1] * (1 + terminal_growth)
    / (wacc - terminal_growth)
)

# Discount terminal value back 5 years
pv_terminal = terminal_value / ((1 + wacc) ** 5)

# Enterprise and equity value
enterprise_value = pv_explicit + pv_terminal
equity_value = enterprise_value + cash - debt
value_per_share = equity_value / shares

# Terminal value share of enterprise value
terminal_share = pv_terminal / enterprise_value

# OUTPUT
print(f"FCFF Year 1: {fcff[0]:.4f}")
print(f"FCFF Year 2: {fcff[1]:.4f}")
print(f"FCFF Year 3: {fcff[2]:.4f}")
print(f"FCFF Year 4: {fcff[3]:.4f}")
print(f"FCFF Year 5: {fcff[4]:.4f}")
print(f"PV of explicit FCFF: {pv_explicit:.4f}")
print(f"Terminal value, Year 5: {terminal_value:.4f}")
print(f"PV of terminal value: {pv_terminal:.4f}")
print(f"Enterprise value: {enterprise_value:.4f}")
print(f"Equity value: {equity_value:.4f}")
print(f"Value per diluted share: {value_per_share:.4f}")
print(f"PV of TV / enterprise value: {terminal_share:.4f}")