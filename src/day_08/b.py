# We are given 10 combinations of signals that are on, corresponding to 10 digits.
# However, we don't know which combination corresponds to which digits, as the signals 
# are mismatched from the segments.
# We logically infer the digits, and use them to find out the 4 digit number,
# on the RHS of |.
import time


# This is the function that we call first. We can directly infer
# the signals for digits 1, 7, 4, 8 as they have unique number of segments.
# 1 ({c, f} = 2), 7 ({a, c, f} = 3), 4 ({b, d, c, f} = 4), 8({a, b, c, d, e, f, g} = 7)
def find_unique_length_digits(signals, digit_to_signals):
    for signal in signals:
        match len(signal):
            case 2:
                digit_to_signals[1] = signal
            case 3:
                digit_to_signals[7] = signal
            case 4:
                digit_to_signals[4] = signal
            case 7:
                digit_to_signals[8] = signal


# This function assumes that we have already found digits 4, 7, 8 which can be
# done using the above function.
# Consider the digits which have 5 segments - 2, 3, 5
# For digit 2 {a, c, d, e, g} - {a, b, c, d, f} = {e, g}
# For digit 3 {a, c, d, f, g} - {a, b, c, d, f} = {g}
# For digit 5 {a, b, d, f, g} - {a, b, c, d, f} = {g}
# 2 is the only digit from which when the segments a, b, c, d, f are removed has 2 segments remaining.
# We can find the signals for segments a, b, c, f, f by taking a union of segments from 4, 7.
# Using the above information, we can find the signals for digit 2, and the signal for the segment 'g'.
# We can also find the signal for segments {e, g}, and take the difference to find the segment 'e'
# Using this, we can find the signals for digit 9 (signals(8) - signal(e)).
def find_two_and_nine(signals, digit_to_signals):
    abcdf_signal = digit_to_signals[7] | digit_to_signals[4]
    eg_signal = digit_to_signals[8] - abcdf_signal
    g_signal = set()

    for signal in signals:
        if len(signal) != 5:
            continue
        if len(signal - abcdf_signal) == 2:
            digit_to_signals[2] = signal
        else:
            g_signal = signal - abcdf_signal
    
    e_signal = eg_signal - g_signal
    digit_to_signals[9] = digit_to_signals[8] - e_signal


# This function assumes that only digits 0, 3, 5, 6 are remaining.
# Out of these 0, 6 have 6 segments and 3, 5 have 5 segments.
# Between 0, 6 - 0 has 3 segments in common with 7 while 6 has 2.
# Between 3, 5 - 3 has 3 segments in common with 7 while 5 has 2.
# Thus we can infer the signals for all of the remaining digits.
def find_remaining(signals, digit_to_signals):
    for signal in signals:
        if len(signal) == 6:
            if len(signal & digit_to_signals[7]) == 3:
                digit_to_signals[0] = signal
            else:
                digit_to_signals[6] = signal
        else:
            if len(signal & digit_to_signals[7]) == 3:
                digit_to_signals[3] = signal
            else:
                digit_to_signals[5] = signal


if __name__ == "__main__":
    t_start = time.perf_counter()
    
    ans = 0
    with open("inputs/08.txt") as f:
        for line in f:
            input, output = line.split("|")
            signals = [set(sorted(signal)) for signal in input.strip().split()]

            digit_to_signals = {}
            find_unique_length_digits(signals, digit_to_signals)
            signals = [signal for signal in signals if signal not in digit_to_signals.values()]
            
            find_two_and_nine(signals, digit_to_signals)
            signals = [signal for signal in signals if signal not in digit_to_signals.values()]
            
            find_remaining(signals, digit_to_signals)
            signals_to_digit = {"".join(sorted(digit_signals)): digit for digit, digit_signals in digit_to_signals.items()}
            
            num = 0
            for output_signals in output.strip().split():
                num = 10 * num  + signals_to_digit["".join(sorted(output_signals))]
            ans += num
    print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
