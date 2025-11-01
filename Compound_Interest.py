"""
Amount = P(1 + R/100) ** T
CI = Amount - P
"""

P = float(input("Enter the Principle Amount: "))
R = float(input("Enter the Rate of Interest: "))
T = float(input("Enter the Time Duration: "))
Amount = P*(1 + R/100) ** T
CI = Amount - P
print("CI", round(CI))