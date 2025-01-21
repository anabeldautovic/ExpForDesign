import numpy as np
from scipy.stats import ttest_ind

def compare_results(paper_results, our_results):
    negligible_count = 0
    noticeable_count = 0
    for key in paper_results.keys():
        if key in our_results:
            paper_value = paper_results[key]
            our_value = our_results[key]
            difference = our_value - paper_value

            print(f"n_topics={key[0]}, alpha_word={key[1]}, alpha_ent={key[2]}")
            print(f"  Paper Result: {paper_value:.4f}")
            print(f"  Our Result: {our_value:.4f}")
            print(f"  Difference: {difference:.4f}")
            if abs(difference) > 1e-6:  # Change the threshold if needed
                print("  The difference is noticeable.")
                noticeable_count += 1
            else:
                print("  The difference is negligible.")
                negligible_count += 1
                
    print(f"Number of negligible differences: {negligible_count}")
    print(f"Number of noticeable differences: {noticeable_count}")

